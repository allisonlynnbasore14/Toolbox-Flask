"""
Simple "Hello, World" application using Flask
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return 'Index page'
    #return render_template('index.html')

@app.route('/tuna')
def tuna():
	return '<h2> Tuna is good<h2>'

@app.route('/profile/<username>')
def profile(username):
	return 'Hey there %s' %username



if __name__ == '__main__':
    app.run(debug=True)

