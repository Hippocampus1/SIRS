from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# read configuration files
from global_config import BaseConfig
app.config.from_object(BaseConfig)

db = SQLAlchemy(app)
