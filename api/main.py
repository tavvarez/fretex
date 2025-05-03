from fastapi import FastAPI;
from pydantic import BaseModel;
import joblib;
import pandas as pd;
from fastapi.middleware.cors import CORSMiddleware;

app = FastAPI();

model = joblib.load("ml/modelo_random_forest_azure.pkl");

mapeamento_tipo_veiculo = {
    'truck': 0,
    'carreta': 1,
    'vuc': 2                       
    }

mapeamento_UF = {
    'SP': 0,
    'RJ': 1,
    'MG': 2,
    'ES': 3
}

mapeamento_transportadora = {
    'Transportadora A': 0,
    'Transportadora B': 1,
    'Transportadora C': 2,
}

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
        UF_origem_cod = mapeamento_UF.get(frete.UF_origem);
        UF_destino_cod = mapeamento_UF.get(frete.UF_destino);
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