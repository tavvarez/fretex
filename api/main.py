from fastapi import FastAPI;
from pydantic import BaseModel;
import joblib;
from azureml.core import Workspace, Model
import pandas as pd;
from fastapi.middleware.cors import CORSMiddleware;
import os;

app = FastAPI();

ws = Workspace.from_config(path="config.json")

registered_model = Model(ws, name="modelo_random_forest-v3")

model_path = registered_model.download(target_dir="/tmp", exist_ok=True)
model_bundle = joblib.load(model_path)
model = model_bundle["model"]

le_tipo_veiculo = model_bundle['encoder_tipo_veiculo']
le_UF_origem = model_bundle['encoder_UF_origem']
le_UF_destino = model_bundle['encoder_UF_destino']
le_transportadora = model_bundle['encoder_transportadora']

mapeamento_tipo_veiculo = {classe: idx for idx, classe in enumerate(le_tipo_veiculo.classes_)}
mapeamento_UF_origem = {classe: idx for idx, classe in enumerate(le_UF_origem.classes_)}
mapeamento_UF_destino = {classe: idx for idx, classe in enumerate(le_UF_destino.classes_)}
mapeamento_transportadora = {classe: idx for idx, classe in enumerate(le_transportadora.classes_)}


class FreteInput(BaseModel):
    tipo_veiculo: str
    UF_origem: str
    UF_destino: str
    transportadora: str
    valor_frete: float

@app.post("/predict")
def predict_frete(frete: FreteInput):
    try:
        tipo_veiculo_cod = mapeamento_tipo_veiculo.get(frete.tipo_veiculo);
        UF_origem_cod = mapeamento_UF_origem.get(frete.UF_origem);
        UF_destino_cod = mapeamento_UF_destino.get(frete.UF_destino);
        transportadora_cod = mapeamento_transportadora.get(frete.transportadora);

        if None in [tipo_veiculo_cod, UF_origem_cod, UF_destino_cod, transportadora_cod]:
            return {"erro": "valor inválido em uma das variáveis"};
        X_new = pd.DataFrame([{
            'tipo_veiculo': tipo_veiculo_cod,
            'UF_origem': UF_origem_cod,
            'UF_destino': UF_destino_cod,
            'transportadora': transportadora_cod,
            'valor_frete': frete.valor_frete
        }])

        y_pred = model.predict(X_new)[0];

        resultado = "Entrega Atrasada" if y_pred == 1 else "Entrega no prazo";

        return {"previsao": resultado};
    except Exception as e:
        return {
            "status": "teste" ,
            "erro": str(e)
        };

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)