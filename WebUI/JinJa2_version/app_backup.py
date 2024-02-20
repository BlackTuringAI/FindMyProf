from flask import Flask, render_template, redirect, url_for, request, flash, jsonify, Markup

app = Flask(__name__)

@app.route("/hi")
def hello_world():
    return "Hi JusJus"

@app.route("/<username>")
def Greet(username):
    return "Hi" + username

@app.route("/", methods=['GET', 'POST'])
def home_page():

    return render_template('home.html', UI=UI)

if __name__ == '__main__':
    app.run(port = 8080, debug=True)
