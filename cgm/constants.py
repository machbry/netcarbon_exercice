import os
from pathlib import Path
from pytz import timezone

from dotenv import load_dotenv

load_dotenv()

DATA_FOLDER = Path(__file__).parents[1] / 'data'
CATALOGS_FOLDER = DATA_FOLDER / 'catalogs'
COGS_FOLDER = DATA_FOLDER / 'cogs'

CATALOGS_FOLDER.mkdir(exist_ok=True, parents=True)
COGS_FOLDER.mkdir(exist_ok=True, parents=True)

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

SERVER_TIMEZONE = timezone('Europe/Paris')
