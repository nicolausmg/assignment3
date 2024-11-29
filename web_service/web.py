from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome Maider! This is our Web App! We have created two pages, this is the homepage."

@app.route('/about')
def about():
    return "About: We have used Flask to create this very simple web app for Assignment 3, we hope you like it!."

if __name__ == '__main__':
    app.run(debug=True)
