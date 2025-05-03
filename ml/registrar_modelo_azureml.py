from azureml.core import Workspace, Model;

ws = Workspace.from_config();
container_name = "modelov1";
blob_name = "modelo_random_forest.pkl";

model_path = "ml/modelo_random_forest_azure.pkl";
model = Model.register(workspace=ws,
                       model_path=model_path,
                       model_name="modelo_random_forest",
                       description="Modelo Random Forest preditor de atrasos de frete",
                       tags={"tipo": "random_forest", "projeto": "fretex"});

print(f"modelo registrado: {model.name} (version: {model.version})");