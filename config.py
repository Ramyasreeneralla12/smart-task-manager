import os

class Config:

    SECRET_KEY = "smart_secret_key"

    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:Ramya%40123@localhost:5432/taskdb"

    SQLALCHEMY_TRACK_MODIFICATIONS = False