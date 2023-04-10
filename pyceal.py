from flask import Flask, render_template , url_for

app = Flask(__name__, template_folder='templates')

@app.route("/")
def root_page():
    return "<h2> Root Page </h2>"

@app.route("/id_generator")
def id_gen():
      return render_template ('id_generator.html')

if __name__ == '__main__':
    app.run(debug=True)