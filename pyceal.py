from flask import Flask, render_template , url_for, request
from forms import ID_Form, LoginForm
app = Flask(__name__, template_folder='templates')

app.config['SECRET_KEY'] = '65dd8a8a9be421c2b8a4f3fdcc42f36a'

@app.route("/")
def root_page():
    return render_template ('root_page.html')

@app.route("/id_generator")
def id_gen():
    form = ID_Form()
    return render_template ('id_generator.html', form=form)

# @app.route("/login")
# def id_gen():
#     form = LoginForm()
#     return render_template ('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)