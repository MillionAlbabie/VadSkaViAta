import os
from dotenv import load_dotenv, find_dotenv

# Hitta och ladda .env-filen automatiskt
load_dotenv(find_dotenv())

class Config:
    """Bas-konfiguration för Flask-appen"""
    
    # Flask grundinställningar
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # MySQL Databas-konfiguration
    DB_HOST = os.environ.get('DB_HOST') or 'localhost'
    DB_PORT = os.environ.get('DB_PORT') or '3306'
    DB_NAME = os.environ.get('DB_NAME') or 'vadskaviaeta'
    DB_USER = os.environ.get('DB_USER') or 'root'
    DB_PASSWORD = os.environ.get('DB_PASSWORD') or ''
    
    # Bygg database URL för SQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    
    # SQLAlchemy inställningar
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False  # Sätt till True för att se SQL-queries i konsolen
    
    # Session-inställningar
    SESSION_COOKIE_SECURE = os.environ.get('SESSION_COOKIE_SECURE', 'False').lower() == 'true'
    SESSION_COOKIE_HTTPONLY = os.environ.get('SESSION_COOKIE_HTTPONLY', 'True').lower() == 'true'
    SESSION_COOKIE_SAMESITE = os.environ.get('SESSION_COOKIE_SAMESITE', 'Lax')
    
    # JWT-inställningar (om du vill använda API-autentisering)
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or SECRET_KEY
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # 1 timme
    
    # Applikationsinställningar
    APP_NAME = os.environ.get('APP_NAME', 'VadSkaViAta')
    APP_VERSION = os.environ.get('APP_VERSION', '1.0.0')
    
    # Mail-inställningar (för användarregistrering)
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'True').lower() == 'true'
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    
    # Loggning
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')
    LOG_FILE = os.environ.get('LOG_FILE', 'app.log')


class DevelopmentConfig(Config):
    """Utvecklingsmiljö-konfiguration"""
    DEBUG = True
    SQLALCHEMY_ECHO = True  # Visa SQL-queries i utveckling
    

class ProductionConfig(Config):
    """Produktionsmiljö-konfiguration"""
    DEBUG = False
    SQLALCHEMY_ECHO = False
    SESSION_COOKIE_SECURE = True
    

class TestingConfig(Config):
    """Test-miljö-konfiguration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # In-memory databas för tester
    WTF_CSRF_ENABLED = False


# Konfigurations-mappning
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}


def get_config():
    """Returnerar rätt konfiguration baserat på miljövariabler"""
    env = os.environ.get('FLASK_ENV', 'development')
    return config.get(env, config['default'])