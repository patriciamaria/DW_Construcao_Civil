from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'Something unique and secret!'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbcons.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 

db = SQLAlchemy(app)

from ConsApp import views, models

from flask_admin import Admin

admin = Admin(app, name='SITE', template_mode='bootstrap3')
from flask_admin.contrib.sqla import ModelView
admin.add_view(ModelView(models.Usuario, db.session))
admin.add_view(ModelView(models.Endereco, db.session))
admin.add_view(ModelView(models.Reserva, db.session))
admin.add_view(ModelView(models.Produto, db.session))
admin.add_view(ModelView(models.Categoria, db.session))
