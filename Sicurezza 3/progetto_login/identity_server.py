from flask import Flask, request, make_response, redirect
from pathlib import Path

app = Flask(__name__)
STATIC_DIR = Path("static")

def serve_html(name):
    path = STATIC_DIR / name
    if not path.exists():
        return make_response("<h1>404</h1>", 404)
    html = path.read_text(encoding="utf-8")
    resp = make_response(html, 200)
    resp.headers["Content-Type"] = "text/html; charset=utf-8"
    return resp

# ---------------------------
# Pagina login
@app.route("/login")
def login():
    nxt = request.args.get("next", "/")
    html = serve_html("login.html").get_data(as_text=True)
    html = html.replace("{{next}}", nxt)
    return make_response(html, 200)

# ---------------------------
# Elaborazione login
@app.route("/dologin", methods=["POST"])
def dologin():
    user = request.form.get("user")
    pw = request.form.get("pw")
    nxt = request.form.get("next", "/")

    # credenziali di esempio
    if user == "admin" and pw == "12345":
        resp = redirect(f"http://localhost:9000{nxt}", code=302)
        resp.set_cookie("sessionid", "abc123", path="/")
        return resp
    return serve_html("fail.html")

# ---------------------------
# Avvio server
if __name__ == "__main__":
    STATIC_DIR.mkdir(exist_ok=True)
    app.run(host="0.0.0.0", port=10000, debug=True)
