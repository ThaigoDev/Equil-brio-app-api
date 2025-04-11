import os

class Config:
    SECRET_KEY = 'secreto123'  # Troque isso depois!
    SQLALCHEMY_DATABASE_URI = 'sqlite:///empreguei.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
