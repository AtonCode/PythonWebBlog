# Libreias
import os
from flask import send_from_directory
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import Flask
from flask import render_template
from jinja2 import Template 
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request
from werkzeug.security import generate_password_hash,check_password_hash

app = Flask(__name__)

# Constantes Globales 
UPLOAD_FOLDER = '/UPLOAD_FOLDER/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','docx','mp3','mp4','mov'}


app.secret_key = "secretkey"
app.config['MONGO_URI'] ="mongodb://127.0.0.1:27017/Users"
mongo=PyMongo(app)
#"mongodb+srv://Aton:chaman99@py-ekmaa.mongodb.net/Users"


#Ruta de upload new files
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():

    
    TitlePage = '| Upload New Files'
    MainTitle = { 'content': 'Upload New Files' }  
    Titleparagraf ={'content': 'Upload New Files'}
    ParagrafOne= {'content': '2020'}

    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',filename=filename))

    return render_template(

        'transfer.html',
         TitlePage= TitlePage,
         MainTitle= MainTitle ,
         Titleparagraf=Titleparagraf,
         ParagrafOne= ParagrafOne
        )

filename = "../../../../home/username/.bashrc"

#Visualizacion de lo cargado
@app.route('/uploads/<filename>')
def uploaded_file(filename):

   
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


# Rutas Erros 404
@app.errorhandler(404)
def page_not_found(error=None):

    TitlePage = '| Page Not Found 404'
    MainTitle = { 'content': 'Ups! This Page Not Found 404' }  
    Titleparagraf ={'content': 'Return to main page'}
    ParagrafOne= {'content': 'Good Search'}

    return render_template(
        
        'page_not_found.html',
         TitlePage= TitlePage,
         MainTitle= MainTitle ,
         Titleparagraf=Titleparagraf,
         ParagrafOne= ParagrafOne
    
    ), 404
# Fin Rutas Erros 404


# addUsers

@app.route('/add', methods=['POST'])
def add_use():

    _json= request.json
    _name = _json["name"]
    _email = _json["email"]
    _password = _json["password"]
 
    if _name and _email and _password and request.method == 'POST':

        _hashed_passwword = generate_password_hash(_password)

        id = mongo.db.user.insert({ "name":_name,"email":_email,"password":_hashed_passwword})

        resp = jsonify("name: ",_name,"email: ",_email)

        resp.status_code = 200

        return resp
    else:
        return page_not_found()

@app.route('/users')
def users():

    users = mongo.db.user.find()
    resp = dumps(users)
    return resp
@app.route('/users/<id>')
def user(id):

    user = mongo.db.user.find_one({"_id":ObjectId(id)})
    resp = dumps(user)
    return resp

@app.route('/delete/<id>', methods=['DELETE'])
def delate_user(id):

    mongo.db.user.delete_one({"_id":ObjectId(id)})
    resp = jsonify("User Delate")
    resp.status_code = 200
    return resp






# Rutas Index
@app.route('/')
def index():

    TitlePage ='| The AtonCode Blog'
    MainTitle = { 'content': 'Welcome to AtonCode Blog' }  
    Titleparagraf ={'content': 'Recommended blogs'}
    ParagrafOne= {'content': 'Blogs '}
   
    return render_template(

        "index.html", 
        TitlePage= TitlePage,
        MainTitle= MainTitle ,
        Titleparagraf=Titleparagraf,
        ParagrafOne= ParagrafOne
        
    )

# Fin Rutas Index


# Rutas About
@app.route('/about')
def about():

    TitlePage = '| About'
    MainTitle = { 'content': 'About' }  
    Titleparagraf ={'content': 'Who I am'}
    ParagrafOne= {'content': 'Hola a todos,'}
   
    return render_template(

        "about.html",
        TitlePage= TitlePage,
        MainTitle= MainTitle ,
        Titleparagraf=Titleparagraf,
        ParagrafOne= ParagrafOne
               
    )

# Fin Rutas About

# Rutas Hobbies
@app.route('/hobbies')
def hobbies():

    TitlePage = '| Hobbies'
    MainTitle = { 'content': 'Hobbies' }  
    Titleparagraf ={'content': 'Watch Academic Movies'}
    ParagrafOne= {'content': '2020'}
   
    return render_template(

        "hobbies.html",
        TitlePage= TitlePage,
        MainTitle= MainTitle ,
        Titleparagraf=Titleparagraf,
        ParagrafOne= ParagrafOne
       
    )
    
# Fin Rutas Hobbies


# Rutas Apps
@app.route('/apps')
def Apps():

    TitlePage = '| Apps'
    MainTitle = { 'content': 'Apps' }  
    Titleparagraf ={'content': 'Recommended Apps'}
    ParagrafOne= {'content': '2020'}
   
    return render_template(

        "apps.html",
        TitlePage= TitlePage,
        MainTitle= MainTitle ,
        Titleparagraf=Titleparagraf,
        ParagrafOne= ParagrafOne
       
    )
    
# Fin Rutas Apps

# Rutas Tools
@app.route('/tools')
def Tools():

    TitlePage = '| Tools'
    MainTitle = { 'content': 'Tools' }  
    Titleparagraf ={'content': 'Visual Studio Code'}
    ParagrafOne= {
        'content': 'Editor de textos'
        }
   
    return render_template(

        "tools.html",
        TitlePage= TitlePage,
        MainTitle= MainTitle ,
        Titleparagraf=Titleparagraf,
        ParagrafOne= ParagrafOne
       
    )
    
# Fin Rutas Tools

 
 #app.debug= True
if __name__ == "__main__":
    app.run(debug=True)