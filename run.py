#!/usr/bin/env python3
"""
VadSkaViAta - Flask Application Starter
Huvudfil för att starta Flask-appen
"""

import os
from app import create_app
from config import get_config

# Skapa Flask-app med rätt konfiguration
app = create_app(get_config())

@app.cli.command()
def init_db():
    """Initialisera databasen med tabeller"""
    from app.models import db
    db.create_all()
    print("Databas initialiserad!")

@app.cli.command()
def seed_db():
    """Lägg till testdata i databasen"""
    from app.models import db, User, Food
    from werkzeug.security import generate_password_hash
    
    # Skapa testanvändare
    test_user = User(
        username='testuser',
        email='test@example.com',
        password_hash=generate_password_hash('password123')
    )
    
    # Skapa testmaträtter
    test_foods = [
        Food(
            name='Pasta Carbonara',
            description='Klassisk italiensk pasta med ägg, bacon och parmesan',
            cuisine_type='italiensk',
            difficulty_level='medium',
            cooking_time=30,
            ingredients='Pasta, ägg, bacon, parmesan, svartpeppar',
            instructions='1. Koka pasta. 2. Stek bacon. 3. Blanda ägg med parmesan. 4. Kombinera allt.'
        ),
        Food(
            name='Köttbullar med potatismos',
            description='Klassiska svenska köttbullar med krämig potatismos',
            cuisine_type='svensk',
            difficulty_level='easy',
            cooking_time=45,
            ingredients='Köttfärs, potatis, mjölk, smör, lök, ägg',
            instructions='1. Forma köttbullar. 2. Stek köttbullar. 3. Koka potatis. 4. Mosa potatis med mjölk och smör.'
        ),
        Food(
            name='Pad Thai',
            description='Thailändsk nudelsoppa med räkor och jordnötter',
            cuisine_type='thailändsk',
            difficulty_level='hard',
            cooking_time=25,
            ingredients='Risnudlar, räkor, ägg, jordnötter, fisksås, lime',
            instructions='1. Blötlägg nudlar. 2. Stek räkor. 3. Rör ihop sås. 4. Woka allt tillsammans.'
        )
    ]
    
    try:
        db.session.add(test_user)
        db.session.add_all(test_foods)
        db.session.commit()
        print("Testdata tillagd!")
    except Exception as e:
        print(f"Fel vid tillägg av testdata: {e}")
        db.session.rollback()

@app.cli.command()
def reset_db():
    """Återställ databasen (radera allt och skapa om)"""
    from app.models import db
    db.drop_all()
    db.create_all()
    print("Databas återställd!")

@app.shell_context_processor
def make_shell_context():
    """Gör modeller tillgängliga i Flask shell"""
    from app.models import db, User, Food, UserFavorite
    return {
        'db': db,
        'User': User,
        'Food': Food,
        'UserFavorite': UserFavorite
    }

if __name__ == '__main__':
    # Kontrollera att alla miljövariabler är satta
    config = get_config()
    
    print(f"Startar {config.APP_NAME} v{config.APP_VERSION}")
    print(f"Miljö: {os.environ.get('FLASK_ENV', 'development')}")
    print(f"Databas: {config.DB_NAME} på {config.DB_HOST}:{config.DB_PORT}")
    
    # Starta Flask-appen
    app.run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 5000)),
        debug=config.DEBUG
    )