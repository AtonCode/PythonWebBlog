from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    text = { 'content': 'Welcome to Aton Code' }  
    Titleparagraf ={'content': 'This website is for coders'}
    paragrafOne= {'content': ' '}
   
    return render_template("index.html", paragrafOne= paragrafOne, title = '| The Aton Code Blog',text = text,  Titleparagraf=Titleparagraf)

 
    
if __name__ == "__main__":
    app.run()