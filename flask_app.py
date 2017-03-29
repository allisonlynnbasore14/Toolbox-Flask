"""
Flask Code.
"""


from flask import Flask, request, render_template, url_for, flash, redirect
app = Flask(__name__)

@app.route('/profile', methods = ['GET', 'POST'])
def profile():

	if request.method == 'POST':
		age = request.form['age']
		firstname = request.form['firstname']
		lastname = request.form['lastname']
		Ninja = request.form['Ninja']
		if age == '' or firstname == '' or lastname == '' or Ninja == '':
			return render_template("profileERROR.html")
		return render_template("profile.html", age= age, firstname = firstname, lastname = lastname, Ninja = Ninja)
	

	return render_template("Toolbox.html")




if __name__ == "__main__":
	app.run()
