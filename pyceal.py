from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route("/")
def root_page():
    return render_template ('root_page.html')

# @app.route("/id_generator")
# def id_gen():
#      return render_template ('id_generator.html')

if __name__ == '__main__':
    app.run(debug=True)