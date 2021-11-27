from flask import Flask, render_template,request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config['RECAPTCHA_USE_SSL']= False
app.config['RECAPTCHA_PUBLIC_KEY']= '6LcQIGEdAAAAAE6GelsofZ-4kbRP_alrV3rlrIgQ'
app.config['RECAPTCHA_PRIVATE_KEY']='6LcQIGEdAAAAAAJ03C5W6zcjuV4VRxzHIOrIw61G'
app.config['RECAPTCHA_OPTIONS'] = {'theme':'white'}
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models