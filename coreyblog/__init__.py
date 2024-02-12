import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from coreyblog.config import Config



app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'users.login'   # login route directs login manager to this route when a page needs a login
login_manager.login_message_category = 'info'

mail = Mail(app)



from coreyblog.users.routes import users    # sourced from blueprint file /users/routes.py
from coreyblog.posts.routes import posts    # sourced from blueprint file /posts/routes.py
from coreyblog.main.routes import main      # sourced from blueprint file /main/routes.py
app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)


