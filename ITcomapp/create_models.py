print ("[--VB--]: Importing Models")
from app import db

print ("[--VB--]: Add to the database")
print ("[--VB--]: Please wait for a few minutes...")

db.create_all()
print ("[--VB--]: Models are successfully created in your database. Thanks You.")