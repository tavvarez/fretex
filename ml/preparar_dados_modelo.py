import pandas as pd;
from dotenv import load_dotenv;
import sys;
import os;
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..')));
from etl.db_connection import get_engine;
from sklearn.model_selection import train_test_split;
from sklearn.preprocessing import LabelEncoder;

engine = get_engine();

query = os.getenv('QUERY');
df = pd.read_sql_query(query, engine);

# coluna 'atraso': 1 se atrasou, 0 se no prazo ou adiantada
df['atraso'] = df['dias_atraso'].apply(lambda x: 1 if x > 0 else 0);

# features (Veiculo, UF origem e destino, transportadora e valor do frete)
features = ['tipo_veiculo', 'UF_origem', 'UF_destino', 'transportadora', 'valor_frete'];
X = df[features];
y = df['atraso'];

# transformar texto em numero
le = LabelEncoder();

for col in ['tipo_veiculo', 'UF_origem', 'UF_destino', 'transportadora']:
    X[col] = le.fit_transform(X[col]);

#treino e testes
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42);

print(f"Tamanho do treino: {X_train.shape[0]} linhas");
print(f"Tamanho do teste: {X_test.shape[0]} linhas");