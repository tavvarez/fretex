# 🚛 FreteX – Análise de Logística e Desempenho de Fretes

Este projeto tem como objetivo simular, analisar e visualizar dados de fretes rodoviários utilizando Python, SQL e Azure, com dashboards interativos.

## 🧰 Tecnologias usadas
- Python (Pandas, Faker, Scikit-learn)
- Azure SQL Database
- SQL (consultas e modelagem)
- Power BI e Streamlit
- Git/GitHub

## 📊 O que você vai encontrar aqui
- Simulação de dados realistas de fretes
- ETL em Python para armazenar dados em banco Azure SQL
- Análises SQL de performance logística
- Modelo preditivo de atraso nas entregas
- Dashboard com indicadores logísticos

## 📁 Estrutura do projeto
(data/, notebooks/, sql/, etl/, ml/, dashboard/)

## 🚀 Como executar
1. Clone este repositório
2. Instale as dependências com `pip install -r requirements.txt`
3. Rode o script `etl/insert_data.py` para carregar os dados simulados
4. Execute as análises ou dashboards à sua escolha

## Algumas consultas do BANCO
1. Quantidade de fretes por UF de origem:
SELECT UF_origem, COUNT(*) AS quantidade_fretes
FROM fretes
GROUP BY UF_origem
ORDER BY quantidade_fretes DESC;

2. Frete médio por tipo de veículo: 
SELECT tipo_veiculo, AVG(valor_frete) AS frete_medio
FROM fretes
GROUP BY tipo_veiculo;

## 📌 Status
Em desenvolvimento 🚧
