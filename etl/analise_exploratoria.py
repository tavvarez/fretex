import pandas as pd;
from db_connection import get_engine;
import matplotlib.pyplot as plt;
import seaborn as sns;
from dotenv import load_dotenv;
import os;

engine = get_engine();

query = os.getenv('QUERY');
df = pd.read_sql(query, engine);

print("Total de fretes: ", len(df));

fretes_no_prazo = len(df[df['dias_atraso'] <= 0]);
fretes_totais = len(df);
print(f"Entregas no prazo: {fretes_no_prazo/fretes_totais:.2%}");

frete_medio = df.groupby('tipo_veiculo')['valor_frete'].mean();
print("\nFrete médio por tipo de veículo:");
print(frete_medio);

top_transportadoras =  df['transportadora'].value_counts().head(5);
print("\nTop 5 transportadoras:");
print(top_transportadoras);

atrasadas = len(df[df['dias_atraso'] > 0]);
no_prazo = len(df[df['dias_atraso'] <= 0]);

labels = ['No prazo', 'Atrasadas'];
sizes = [no_prazo, atrasadas];

plt.figure(figsize=(6,6));
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=["#4CAF50", "#F44336"]);
plt.title('Entrega no prazo vs Atrasadas');
plt.axis('equal');
plt.show()

frete_medio_dois = df.groupby('tipo_veiculo')['valor_frete'].mean().sort_values();

plt.figure(figsize=(8,5));
sns.barplot(x=frete_medio_dois.index, y=frete_medio_dois.values, palette="Blues_d");
plt.title('Frete médio p/ veículo');
plt.xlabel('tipo de veículo');
plt.xlabel('valor médio do frete em reais');
plt.xticks(rotation = 45);
plt.show();

top_transportadoras = df['transportadora'].value_counts().head(5);

plt.figure(figsize=(8,5));
sns.barplot(x=top_transportadoras.index, y=top_transportadoras.values, palette="Greens_d");
plt.title('Top 5 Transportadoras');
plt.xlabel('Transportadora');
plt.ylabel('Quantidade de Fretes');
plt.xticks(rotation=45);
plt.show();