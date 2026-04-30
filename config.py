class Config:
    SECRET_KEY = "super-secret-key"

    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://root:rootpassword@mysql:3306/mydb"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
