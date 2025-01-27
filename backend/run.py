from waitress import serve
from app import app  # Remplacez "app" par le nom de votre application Flask si différent

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
