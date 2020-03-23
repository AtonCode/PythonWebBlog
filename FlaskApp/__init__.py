from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    titlePage = '| The Aton Code Blog'
    text = { 'content': 'Welcome to Aton Code' }  
    Titleparagraf ={'content': 'The WarGames Movie'}
    paragrafOne= {'content': 'Movie in Sapnish'}
   
    return render_template("index.html", paragrafOne= paragrafOne, titlePage=titlePage,text = text,  Titleparagraf=Titleparagraf)

app.debug = True 
if __name__ == "__main__":
    app.run()