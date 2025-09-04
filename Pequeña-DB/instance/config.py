from flask_sqlalchemy import SQLAlchemy

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///salon_event.db'  
    # Usa SQLite como base de datos
    SQLALCHEMY_TRACK_MODIFICATIONS = False  
    # Desactiva advertencias sobre el uso de memoria

db = SQLAlchemy()