import pandas as pd;
from db_connection import get_engine;

csv_path = 'data/fretes_simulados.csv';
df = pd.read_csv(csv_path, sep=';');

engine = get_engine()

df.to_sql('fretes', con=engine, if_exists='append', index=False);
print("Dados inseridos com sucesso na Azure SQL");