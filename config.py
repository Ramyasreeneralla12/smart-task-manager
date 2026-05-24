import os


class Config:

    SECRET_KEY = "smart_secret_key"

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "postgresql://taskdb_zd0i_user:6OsS9VMHOplTdLLlumyDtkPPtE0jOo7k@dpg-d8973uh9rddc73917gp0-a.oregon-postgres.render.com/taskdb_zd0i"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
