# Libreias
from flask import Flask
from flask import render_template

# Constantes Globales 
app = Flask(__name__)


# Rutas Erros 404
@app.errorhandler(404)
def page_not_found(error):

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


# Rutas Index
@app.route('/')
def index():

    TitlePage ='| The Sacristan Blog'
    MainTitle = { 'content': 'Welcome to Sacristan Blog' }  
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
    ParagrafOne= {'content': 'I am'}
   
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
    Titleparagraf ={'content': 'My Hobbies'}
    ParagrafOne= {'content': 'I am'}
   
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
    ParagrafOne= {'content': 'Apps'}
   
    return render_template(

        "apps.html",
        TitlePage= TitlePage,
        MainTitle= MainTitle ,
        Titleparagraf=Titleparagraf,
        ParagrafOne= ParagrafOne
       
    )
    
# Fin Rutas Apps

 
 #app.debug= True
if __name__ == "__main__":
    app.run()