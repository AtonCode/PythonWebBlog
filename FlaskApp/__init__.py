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



# Rutas Index
@app.route('/')
def index():

    titlePage ='| The Sacristan. Alejandro Blog'
    text = { 'content': 'Welcome to Sacristan. Alejandro Blog' }  
    Titleparagraf ={'content': 'Recommended blogs'}
    paragrafOne= {'content': 'Blogs '}
   
    return render_template(

        "index.html", 
        paragrafOne= paragrafOne, 
        titlePage = titlePage,
        text = text,
        Titleparagraf=Titleparagraf
        
        )
# Fin Rutas Index


# Rutas About
@app.route('/about')
def about():

    titlePage = '| About'
    text = { 'content': 'About' }  
    Titleparagraf ={'content': 'Who I am'}
    paragrafOne= {'content': 'I am'}
   
    return render_template(

        "about.html",
        titlePage= titlePage, 
        paragrafOne= paragrafOne,
        text = text,
        Titleparagraf=Titleparagraf
        
       
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
        Titleparagraf=Titleparagraf
       
        )
    
# Fin Rutas Hobbies


# Rutas Apps
@app.route('/apps')
def Apps():

    titlePage = '| Apps'
    text = { 'content': 'Apps' }  
    Titleparagraf ={'content': 'Recommended Apps'}
    paragrafOne= {'content': 'Apps'}
   
    return render_template(

        "apps.html",
        titlePage= titlePage, 
        paragrafOne= paragrafOne,
        text = text,
        Titleparagraf=Titleparagraf
       
        )
    
# Fin Rutas Apps

 
    
if __name__ == "__main__":
    app.run()