from flask import Flask

app = Flask(__name__)

@app.route("/")

def home():
    return "home"

@app.route("/second")
def second():
    return "second route"

@app.route("/third")
def third():
    return "third route"

if __name__ == "__main__":
    app.run()
