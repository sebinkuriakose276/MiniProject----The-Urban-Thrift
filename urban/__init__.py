from flask import Flask,redirect,url_for
from flask_sqlalchemy   import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urban.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view="login"
login_manager.login_message_category="info"
@login_manager.unauthorized_handler
def unauthorized_callback():
    # Redirect the user to the login page or display an error message
    return redirect(url_for('auth.login'))


# blueprint for auth routes in our app
from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

# blueprint for non-auth parts of app
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

# def create_app():
#     app = Flask(__name__)

#     app.config['SECRET_KEY'] = 'secret-key-goes-here'
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urban.db'

#     db.init_app(app)

#     login_manager = LoginManager()
#     login_manager.login_view = 'auth.login'
#     login_manager.init_app(app)



      

#     return app