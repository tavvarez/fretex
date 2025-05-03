import pandas as pd;
from db_connection import get_engine;
import plotly.express as px;
import plotly.graph_objects as go;
from dotenv import load_dotenv;
import os;

engine = get_engine();

query = os.getenv('QUERY');
df = pd.read_sql(query, engine);

atrasadas = len(df[df['dias_atraso'] > 0]);
no_prazo = len(df[df['dias_atraso'] <= 0]);

fig_pizza = px.pie(
    names=['No prazo', 'Atrasadas'],
    values=[no_prazo, atrasadas],
    title='Entrega no prazo vs atradas',
    color_discrete_sequence=["#4CAF50", "#F44336"]
)
fig_pizza.show();

frete_medio = df.groupby('tipo_veiculo')['valor_frete'].mean().sort_values().reset_index();
fig_barras_veiculo = px.bar(
    frete_medio,
    x='tipo_veiculo',
    y='valor_frete',
    title='Frete medio p/ tipo de veiculo',
    color='tipo_veiculo',
    text_auto='.2s'
)
fig_barras_veiculo.update_layout(showlegend=False);
fig_barras_veiculo.show();


top_transportadoras = df['transportadora'].value_counts().head(10).reset_index();
top_transportadoras.columns = ['transportadora', 'quantidade']
fig_barras_transportadoras = px.bar(
    top_transportadoras,
    x='transportadora',
    y='quantidade',
    title='top 10 transportadoras',
    color='transportadora',
    text_auto=True
)
fig_barras_transportadoras.update_layout(showlegend=False);
fig_barras_transportadoras.show();