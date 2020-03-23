import os
from markupsafe import escape
from werkzeug.utils import secure_filename
from flask import Flask ,render_template, redirect, url_for, flash, request, send_from_directory


app = Flask(__name__)



# Rutas Erros 404
@app.errorhandler(404)
def page_not_found(error):
    titlePage = '| Page Not Found 404'
    return render_template('page_not_found.html', titlePage= titlePage), 404
# Fin Rutas Erros 404


# Rutas index
@app.route('/')
def index():
    text = { 'content': 'Welcome to Aton Code' }  
    Titleparagraf ={'content': 'This website is for coders'}
    paragrafOne= {'content': ' '}
   
    return render_template("index.html", paragrafOne= paragrafOne, title = '| The Aton Code Blog',text = text,  Titleparagraf=Titleparagraf)
# Fin Rutas index


# Ruta Interactiva
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)
# Fin Ruta Interactiva
 

if __name__ == "__main__":
    app.run()