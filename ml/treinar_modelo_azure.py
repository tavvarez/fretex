from azureml.core import Workspace, Experiment, ScriptRunConfig, Environment;

ws = Workspace.from_config();

experiment = Experiment(workspace=ws, name='treinar-modelo-fretes');

env = Environment.from_conda_specification(name='env-ml', file_path='environment.yml');
src = ScriptRunConfig(source_directory='ml', script='treinar-modelo.py', environment=env);

run = experiment.submit(src);
run.wait_for_completion(show_output=True);