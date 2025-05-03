import pandas as pd;
import os;
import sys;
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..')));
from etl.db_connection import get_engine;
from sklearn.model_selection import train_test_split;
from sklearn.preprocessing import LabelEncoder;
from sklearn.tree import DecisionTreeClassifier;
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report;

#conexão Azure Database
engine = get_engine();
query = os.getenv('QUERY');
df = pd.read_sql_query(query, engine);

df['atraso'] = df['dias_atraso'].apply(lambda x: 1 if x > 0 else 0);

features = ['tipo_veiculo', 'UF_origem', 'UF_destino', 'transportadora', 'valor_frete'];
X = df[features];
y = df['atraso'];

le = LabelEncoder();
for col in ['tipo_veiculo', 'UF_origem', 'UF_destino', 'transportadora']:
    X[col] = le.fit_transform(X[col]);

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42);

#treinamento
model = DecisionTreeClassifier(random_state=42);
model.fit(X_train, y_train);

#avaliação
y_pred = model.predict(X_test);

#acuracia
acc = accuracy_score(y_test, y_pred);
print(f"Acurácia do Modelo: {acc:.2%}")

# matriz de confusão
print("\nMatriz de Confusão:")
print(confusion_matrix(y_test, y_pred))

# relatorio de classificação
print("\nRelatório de Classificação:")
print(classification_report(y_test, y_pred))
