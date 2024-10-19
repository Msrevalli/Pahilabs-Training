from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

# Wrap the WSGI app with ProxyFix middleware
app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
