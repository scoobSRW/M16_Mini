import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

class Config:
    # Basic app configuration
    DEBUG = True
    SECRET_KEY = os.environ.get("SECRET_KEY", "your-default-secret-key")

    # PostgreSQL configuration
    POSTGRESQL_USR = os.environ.get("POSTGRESQL_USR", "default_user")
    POSTGRESQL_PSW = os.environ.get("POSTGRESQL_PSW", "default_password")
    POSTGRESQL_DB = os.environ.get("POSTGRESQL_DB", "default_db")

    # If POSTGRESQL_URL exists, use it; otherwise, construct the URL from individual components
    POSTGRESQL_URL = os.environ.get(
        "POSTGRESQL_URL",
        f'postgresql://{POSTGRESQL_USR}:{POSTGRESQL_PSW}@'
        'dpg-cufsc1lds78s73foj6sg-a.oregon-postgres.render.com/'
        f'{POSTGRESQL_DB}'
    )

    # SQLAlchemy database URI
    SQLALCHEMY_DATABASE_URI = POSTGRESQL_URL

    # Disable the SQLAlchemy event system which is not needed in most cases
    SQLALCHEMY_TRACK_MODIFICATIONS = False
