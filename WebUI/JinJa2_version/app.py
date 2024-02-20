from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
# app.config['STATIC_FOLDER'] = 'templates/build/static'

@app.route("/hi")
def hello_world():
    return "Hi JusJus"
@app.route("/<username>")
def Greet(username):
    return "Hi" + username

@app.route("/search", methods=['GET', 'POST'])
def search():
    
    return render_template('search.html', page_name="FindYourProf")

@app.route("/search/submit", methods=['GET', 'POST'])
def search_submit():
    # field = request.form['Field-of-research']
    # uni = request.form['University']
    # desciption = request.form['Description']
    # name = request.form['Prof-name']
    return "submitted"

@app.route("/", methods=['GET'])
def home_page():
    # return redirect(url_for('search'))
    return render_template('home.html', page_name="Home")

if __name__ == '__main__':
    app.run(port = 8080, debug=True)
