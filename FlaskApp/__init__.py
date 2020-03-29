# Libreias
from flask import Flask
from flask import render_template
from jinja2 import Template 
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request
from werkzeug.security import generate_password_hash,check_password_hash


# Constantes Globales 
app = Flask(__name__)

app.secret_key = "secretkey"
app.config['MONGO_URI'] = "mongodb://127.0.0.1:27017/Users"
mongo=PyMongo(app)



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

        id = mongo.db.user.insert_one({ "name":_name,"email":_email,"password":_hashed_passwword})

        resp = jsonify("name: ",_name,"email: ",_email)

        resp.status_code = 200

        return resp
    else:
        return page_not_found()


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