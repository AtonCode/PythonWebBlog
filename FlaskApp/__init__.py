from flask import Flask
from flask import render_template

app = Flask(__name__)


# Rutas Erros 404
@app.errorhandler(404)
def page_not_found(error):

    titlePage = '| Page Not Found 404'
    text = { 'content': 'Ups! This Page Not Found 404' }  
    Titleparagraf ={'content': 'Return to main page'}
    paragrafOne= {'content': 'Good Search'}

    return render_template(
        
        'page_not_found.html',
         titlePage= titlePage,
         paragrafOne= paragrafOne,
         text = text,
         Titleparagraf=Titleparagraf,
    
    ), 404
# Fin Rutas Erros 404


# Rutas index
@app.route('/')
def index():

    titlePage = '| The Sacristán. Alejandro Blog'
    text = { 'content': 'Welcome to Sacristán. Alejandro Blog' }  
    Titleparagraf ={'content': 'Recomdeate Blogs'}
    paragrafOne= {'content': 'Blogs Score'}
   
    return render_template(

        "index.html",
        titlePage= titlePage, 
        paragrafOne= paragrafOne,
        text = text,
        Titleparagraf=Titleparagraf,
       
        )

# Rutas About
@app.route('/about')
def about():

    titlePage = '| About'
    text = { 'content': 'About' }  
    Titleparagraf ={'content': 'Me'}
    paragrafOne= {'content': 'I am'}
   
    return render_template(

        "about.html",
        titlePage= titlePage, 
        paragrafOne= paragrafOne,
        text = text,
        Titleparagraf=Titleparagraf,
       
        )
    
# Fin Rutas About


# Rutas Hobbies
@app.route('/hobbies')
def hobbies():

    titlePage = '| Hobbies'
    text = { 'content': 'Hobbies' }  
    Titleparagraf ={'content': 'My Hobbies'}
    paragrafOne= {'content': 'I am'}
   
    return render_template(

        "hobbies.html",
        titlePage= titlePage, 
        paragrafOne= paragrafOne,
        text = text,
        Titleparagraf=Titleparagraf,
       
        )
    
# Fin Rutas Hobbies


# Rutas Apps
@app.route('/apps')
def Apps():

    titlePage = '| Apps'
    text = { 'content': 'Apps' }  
    Titleparagraf ={'content': 'Recomendate Apps'}
    paragrafOne= {'content': 'Apps'}
   
    return render_template(

        "apps.html",
        titlePage= titlePage, 
        paragrafOne= paragrafOne,
        text = text,
        Titleparagraf=Titleparagraf,
       
        )
    
# Fin Rutas Apps


if __name__ == "__main__":
    app.run()