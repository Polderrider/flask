from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from coreyblog.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'   # login route directs login manager to this route when a page needs a login
login_manager.login_message_category = 'info'

mail = Mail()



def create_app(config_class=Config):
    """ moves creation of app inside the function """
    # creates app
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    # blueprints
    from coreyblog.users.routes import users    # sourced from blueprint file /users/routes.py
    from coreyblog.posts.routes import posts    # sourced from blueprint file /posts/routes.py
    from coreyblog.main.routes import main      # sourced from blueprint file /main/routes.py
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)

    return app