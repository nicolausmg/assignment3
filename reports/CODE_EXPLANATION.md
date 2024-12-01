Dear Maider,

We wanted to share our experience working on this part of the assignment where we had to create a website using the python library flask. As we had limited prior experience with Flask, we relied on two key resources to learn and build our web application: ChatGPT and the Flask official documentation (https://flask.palletsprojects.com/en/stable/quickstart/#rendering-templates). 

Chat guided us through the structure and best practices of a Flask application, as well as to help us solve specific problems we encountered. The official documentation helped ius understand how to set up routes, render templates and manage other functionalities.

Here is what we learned about the code we wrote:

1.	from flask import Flask:
Flask provides tools to handle HTTP requests, routing and more.
2.	app = Flask(__name__):
This creates an instance of the Flask class. The __name__ variable is used to tell Flask where to look for templates.
3.	@app.route('/'):
Anything with an @ in front is a decorator (something that modifies the behaviour of a function). In this case, it is a route decorator that maps a URL (/) to a specific function. In our case, it connects the root URL (homepage) to the home() function.
4.	def home()::
This function defines what happens when someone visits the root URL. The string returned by this function is displayed on the webpage.
5.	@app.route('/about'):
Similar to the root route, this maps the /about URL to the about() function.
6.	return:
Whatever string is returned by the route function is what is displayed on the corresponding webpage.
7.	if __name__ == '__main__'::
This ensures that the application only runs when the file is executed directly, not when it is imported as a module in another Python script.
8.	app.run(debug=True):
This starts the Flask development server and enables debugging, this means that Flask automatically detects code changes and reloads the server. This is especially helpful during development as you don’t need to manually restart the server after every change.