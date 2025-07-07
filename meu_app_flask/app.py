from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Olá, mundo! Meu app Flask está no ar."

if __name__ == '__main__':
    app.run(debug=True)
