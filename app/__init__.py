from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialisera extensions
db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_class):
    """Application factory för Flask-appen"""
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialisera extensions med app
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Du måste logga in för att komma åt denna sida.'
    
    # Registrera blueprints (routes)
    from app.routes import main
    app.register_blueprint(main.bp)
    
    # Skapa databastabeller
    with app.app_context():
        db.create_all()
    
    return app