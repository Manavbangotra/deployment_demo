from flask import Flask
app=Flask(__name__)

@app.route('/')
def home():
    return "flask heroku app"

if __name__ == 'main':
    app.run()