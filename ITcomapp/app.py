from flask 				import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy 	import SQLAlchemy
from datetime 			import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///product.db'

db = SQLAlchemy(app)

class Product(db.Model):
	id 			= db.Column(db.Integer, primary_key=True)
	name 		= db.Column(db.String(30), nullable=False)
	date_created =  db.Column(db.DateTime, default=datetime.utcnow)

	def __repr__(self):
		return '<Name %r>' % self.id




@app.route('/')
def home():
	return render_template("dashboard.html")

@app.route('/category', methods=['GET','POST'])
def category():
	error = None
	if request.method == 'POST':
		if request.form['category'] == '':
			error = ''
		else:
			return redirect(url_for('category'))
	return render_template('category.html')


@app.route('/product', methods=['GET', 'POST'])
def product():
	error = None
	if request.method == 'POST':
		if request.form['productname'] == '':
			error = ''
		else:
			return redirect(url_for('category'))
	return render_template('product.html')
	

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid credentials. Please try again..'
		else:
			return redirect(url_for('product'))
	return render_template('login.html', error=error)


if __name__=='__main__':
	app.run(debug=True)
