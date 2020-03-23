import os
from markupsafe import escape
from werkzeug.utils import secure_filename
from flask import Flask ,render_template, redirect, url_for, flash, request, send_from_directory


app = Flask(__name__)



@app.route('/')
def index():
    text = { 'content': 'Welcome to Aton Code' }  
    Titleparagraf ={'content': 'This website is for coders'}
    paragrafOne= {'content': ' '}
   
    return render_template("index.html", paragrafOne= paragrafOne, title = '| The Aton Code Blog',text = text,  Titleparagraf=Titleparagraf)

    
if __name__ == "__main__":
    app.run()