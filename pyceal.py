from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h5>Hello, World!</h5>"

@app.route("/about")
def about():
    return "<h5>this is my about page</h5>"


if __name__ == '__main__':
    app.run(debug=True)