import re
from datetime import datetime
from collections import defaultdict, Counter

# --- CONFIGURATION ---
FILE_PATH = 'traffico_http.txt'  # Insert your filename here
INTERFACE_FILTER = "docker0" # Filter to avoid duplicates (veth vs docker0)


def parse_tcpdump_logs(filename):
    # Dictionary to store pending requests: { client_port: {start_time, url} }
    pending_requests = {}
    
    # List to store completed transactions: (url, response_time_ms)
    completed_requests = []
    
    # Counter for most visited pages
    page_counts = Counter()

    print(f"Reading file: {filename}...")

    with open(filename, 'r') as file:
        for line in file:
            # 1. Filter: Use only lines from 'docker0' to avoid double counting packets
            if INTERFACE_FILTER not in line:
                continue

            # 2. Extract Timestamp (e.g., 11:45:04.262676)
            # We look for the pattern at the start of the line
            time_match = re.search(r'^(\d{2}:\d{2}:\d{2}\.\d{6})', line)
            if not time_match:
                continue
            
            timestamp_str = time_match.group(1)
            current_time = datetime.strptime(timestamp_str, "%H:%M:%S.%f")

            # 3. DETECT REQUEST (GET)
            # Pattern: IP source.port > dest.http ... GET /page
            # Example: IP proxy.60454 > ... GET /info_page_1.html
            if "GET /" in line:
                # Regex to find the client port (the number after the dot in source IP)
                # and the URL
                req_match = re.search(r'IP .*?\.(\d+) > .*? HTTP: GET (/\S+)', line)
                
                if req_match:
                    client_port = req_match.group(1)
                    url = req_match.group(2)
                    
                    # Store the request start time
                    pending_requests[client_port] = {
                        'start_time': current_time,
                        'url': url
                    }
                    
                    # Count the visit
                    page_counts[url] += 1

            # 4. DETECT RESPONSE (HTTP 200 OK)
            # Pattern: IP dest.http > source.port ... HTTP/1.1 200 OK
            elif "HTTP/1.1 200 OK" in line:
                # Regex to find the client port (destination in the response)
                res_match = re.search(r'IP .*? > .*?\.(\d+): .*? HTTP', line)
                
                if res_match:
                    client_port = res_match.group(1)
                    
                    # Check if we have a pending request for this port
                    if client_port in pending_requests:
                        request_data = pending_requests.pop(client_port)
                        start_time = request_data['start_time']
                        url = request_data['url']
                        
                        # Calculate duration
                        duration = (current_time - start_time).total_seconds() * 1000 # convert to ms
                        
                        completed_requests.append({
                            'url': url,
                            'time_ms': duration
                        })

    return page_counts, completed_requests

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    try:
        counts, times = parse_tcpdump_logs(FILE_PATH)

        print("\n" + "="*40)
        print(" TOP VISITED PAGES")
        print("="*40)
        # Sort by most common
        for page, count in counts.most_common():
            print(f"{count:4} visits: {page}")

        print("\n" + "="*40)
        print(" AVERAGE RESPONSE TIMES (ms)")
        print("="*40)
        
        # Calculate average time per page
        page_times = defaultdict(list)
        for req in times:
            page_times[req['url']].append(req['time_ms'])
            
        for page, time_list in page_times.items():
            avg_time = sum(time_list) / len(time_list)
            print(f"{page:<25} : {avg_time:.2f} ms")

    except FileNotFoundError:
        print("Error: File not found. Make sure 'dump.txt' is in the same folder.")
    except Exception as e:
        print(f"An error occurred: {e}")