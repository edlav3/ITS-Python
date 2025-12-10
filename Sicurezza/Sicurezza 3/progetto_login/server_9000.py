from flask import Flask, make_response, redirect, request
from pathlib import Path

app = Flask(__name__)
STATIC_DIR = Path("static")

# ---------------------------
# Helper: serve file HTML
# ---------------------------
def serve_html(filename: str):
    path = STATIC_DIR / filename
    if not path.exists():
        return make_response("<h1>404 - File non trovato</h1>", 404)

    html = path.read_text(encoding="utf-8")
    resp = make_response(html, 200)
    resp.headers["Content-Type"] = "text/html; charset=utf-8"
    return resp

# ---------------------------
# Pagina pubblica
# ---------------------------
@app.route("/")
def home():
    return serve_html("home.html")

# ---------------------------
# Protezione: verifica cookie
# ---------------------------
def require_login(path):
    session = request.cookies.get("sessionid")
    if session is None:
        # redirect verso identity manager
        return redirect(f"http://localhost:10000/login?next={path}", code=302)
    return None

# ---------------------------
# Pagina protetta
# ---------------------------
@app.route("/area")
def area():
    check = require_login("/area")
    if check:
        return check
    return serve_html("area.html")

# ---------------------------
# Pagina di errore (se serve)
# ---------------------------
@app.route("/errore")
def errore():
    return serve_html("errore.html")

# ---------------------------
# Avvio server
# ---------------------------
if __name__ == "__main__":
    STATIC_DIR.mkdir(exist_ok=True)
    app.run(host="0.0.0.0", port=9000, debug=True)
