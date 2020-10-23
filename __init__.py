from flask import Flask
from flask_sqlalchemy 	import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['WTF_CSRF_ENABLED'] = True

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://username:password@localhost:5432/db_name"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:1234@localhost:5432/vb_learn"

db = SQLAlchemy(app)

from app.Article.views 		import *
from app.Login.views		import *