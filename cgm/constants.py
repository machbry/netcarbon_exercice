import os

from dotenv import load_dotenv

load_dotenv()

CGM_POSTGRES_HOSTNAME = os.environ.get('CGM_POSTGRES_HOSTNAME')
CGM_POSTGRES_PORT = os.environ.get('CGM_POSTGRES_PORT')
CGM_POSTGRES_DB = os.environ.get('CGM_POSTGRES_DB')
CGM_POSTGRES_USER = os.environ.get('CGM_POSTGRES_USER')
CGM_POSTGRES_PASSWORD = os.environ.get('CGM_POSTGRES_PASSWORD')

CGM_POSTGRES_DB_URL = (
        "postgresql://"
        + CGM_POSTGRES_USER
        + ":"
        + CGM_POSTGRES_PASSWORD
        + "@"
        + CGM_POSTGRES_HOSTNAME
        + ":"
        + CGM_POSTGRES_PORT
        + "/"
        + CGM_POSTGRES_DB
)

SRID = os.environ.get('SRID')