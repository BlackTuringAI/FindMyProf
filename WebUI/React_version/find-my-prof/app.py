from flask import Flask, render_template, request, redirect, url_for

import os
from pathlib import Path
import shutil


def build_react():
    tp = Path(__file__).parent/'templates'
    if tp.exists():
        shutil.rmtree(str(tp))
    tp.mkdir()
    
    st = Path(__file__).parent/'static'
    if st.exists():
        shutil.rmtree(str(st))
        
    # just in case
    build = Path(__file__).parent/'build'
    if build.exists():
        shutil.rmtree(str(build))
    
    os.chdir(str(Path(__file__).parent/'src'))
    os.system("npm run build")
    
    react_st = build/'static'
    shutil.move(str(react_st), str(Path(__file__).parent))
    
    for i in build.iterdir():
        shutil.move(str(i), str(Path(__file__).parent/'templates'))
    
    os.rmdir(str(build))
    return


app = Flask(__name__)

@app.route("/hi")
def hello_world():
    return "Hi JusJus"
@app.route("/<username>")
def Greet(username):
    return "Hi" + username

@app.route("/search", methods=['GET'])
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
    return render_template('index.html', page_name="Home")


if __name__ == '__main__':
    if os.environ.get('WERKZEUG_RUN_MAIN') != 'true':
        build_react()
        
    app.run(port = 8080, debug=True)
