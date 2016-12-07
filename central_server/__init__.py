import base64

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
# read configuration files
from global_config import BaseConfig
app.config.from_object(BaseConfig)

db = SQLAlchemy(app)
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    from central_server.models.user import User
    return User.get(user_id)


@login_manager.header_loader
def load_user_from_header(header_val):
    import pdb; pdb.set_trace()
    header_val = header_val.replace('Basic ', '', 1)
    try:
        header_val = base64.b64decode(header_val)
    except TypeError:
        pass
    from central_server.models.user import User
    username, password = header_val.split(":")
    return User.query.filter_by(username=username).first()