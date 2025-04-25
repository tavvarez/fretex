CREATE TABLE fretes (
    id INT IDENTY(1,1) PRIMARY KEY,
    data_prevista DATE,
    data_entrega DATE,
    valor_frete DECIMAL(10,2),
    UF_origem CHAR(2),
    UF_destino CHAR(2),
    transportadora VARCHAR(50),
    tipo_veiculo VARCHAR(20),
    status_entrega VARCHAR(20),
    dias_atraso INT
);