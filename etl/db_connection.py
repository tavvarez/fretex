import os;
from dotenv import load_dotenv;
from sqlalchemy import create_engine;

def get_engine():
    load_dotenv();

    server =  os.getenv('AZURE_SQL_SERVER');
    database = os.getenv('AZURE_SQL_DATABASE');
    username = os.getenv('AZURE_SQL_USERNAME');
    password = os.getenv('AZURE_SQL_PASSWORD');
    driver = os.getenv('AZURE_SQL_DRIVER');

    connection_string = f'mssql+pyodbc://{username}:{password}@{server}:1433/{database}?driver={driver.replace(" ", "+")}';
    engine = create_engine(connection_string);
    return engine;