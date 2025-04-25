import pandas as pd;
import os;
from sqlalchemy import create_engine;
from dotenv import load_dotenv;

load_dotenv();

server =  os.getenv('AZURE_SQL_SERVER');
database = os.getenv('AZURE_SQL_DATABASE');
username = os.getenv('AZURE_SQL_USERNAME');
password = os.getenv('AZURE_SQL_PASSWORD');
driver = os.getenv('AZURE_SQL_DRIVER');

csv_path = 'data/fretes_simulados.csv';

df = pd.read_csv(csv_path, sep=';');

connection_string = f'mssql+pyodbc://{username}:{password}@{server}:1433/{database}?driver={driver.replace(" ", "+")}';
engine = create_engine(connection_string);

df.to_sql('fretes', con=engine, if_exists='append', index=False);
print("Dados inseridos com sucesso na Azure SQL");