from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Olá, mundo! Meu app Flask está no ar."

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
