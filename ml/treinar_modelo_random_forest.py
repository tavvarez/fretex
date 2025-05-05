import joblib
import pandas as pd;
import os;
import sys;

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..')));


from etl.db_connection import get_engine;
from sklearn.model_selection import train_test_split;
from sklearn.preprocessing import LabelEncoder;
from sklearn.ensemble import RandomForestClassifier;
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report;


engine = get_engine();
query = os.getenv('QUERY');
df = pd.read_sql(query, engine);

df['atraso'] = df['dias_atraso'].apply(lambda x: 1 if x > 0 else 0);
feature = ['tipo_veiculo', 'UF_origem', 'UF_destino', 'transportadora', 'valor_frete'];
X = df[feature];
y = df['atraso'];

# le = LabelEncoder();
# for col in  ['tipo_veiculo', 'UF_origem', 'UF_destino', 'transportadora']:
#     X[col] = le.fit_transform(X[col]);
le_tipo_veiculo = LabelEncoder();
le_UF_origem = LabelEncoder();
le_UF_destino = LabelEncoder();
le_transportadora = LabelEncoder();

X['tipo_veiculo'] = le_tipo_veiculo.fit_transform(X['tipo_veiculo'])
X['UF_origem'] = le_UF_origem.fit_transform(X['UF_origem'])
X['UF_destino'] = le_UF_destino.fit_transform(X['UF_destino'])
X['transportadora'] = le_transportadora.fit_transform(X['transportadora'])


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42);
model = RandomForestClassifier(n_estimators=100, random_state=42);
model.fit(X_train, y_train);

print(f"Tipo: {type(model)}")

y_pred = model.predict(X_test);

acc = accuracy_score(y_test, y_pred);
print("acuraccy")
print(f"{acc:.2%}");

print("matrix")
print(confusion_matrix(y_test, y_pred));

print("classificação")
print(classification_report(y_test, y_pred));

joblib.dump({
    'model': model,
    'encoder_tipo_veiculo': le_tipo_veiculo,
    'encoder_UF_origem': le_UF_origem,
    'encoder_UF_destino': le_UF_destino,
    'encoder_transportadora': le_transportadora
}, 'ml/modelo_random_forest_v2.pkl')
print("\nModelo Salvo")

print("Classes tipo_veiculo:", le_tipo_veiculo.classes_)
print("Classes UF_origem:", le_UF_origem.classes_)
print("Classes UF_destino:", le_UF_destino.classes_)
print("Classes transportadora:", le_transportadora.classes_)