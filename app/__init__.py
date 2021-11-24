from flask import Flask, render_template,request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes, models