from ConsApp import db

db.drop_all() 
db.create_all()
print('done.')