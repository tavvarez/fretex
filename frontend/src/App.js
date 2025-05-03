import React, { useState} from 'react';
import './App.css';

function App() {
  const [formData, setFormData] = useState({
    tipo_veiculo: '',
    UF_origem: '',
    UF_destino: '',
    transportadora: '',
    valor_frete:''
  });

  const [resultado, setResultado] = useState('');
  const handleChange = (e) => {
    setFormData({...formData, [e.target.name]: e.target.value});
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://127.0.0.1:8000/predict', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
          tipo_veiculo: formData.tipo_veiculo,
          UF_origem: formData.UF_origem,
          UF_destino: formData.UF_destino,
          transportadora: formData.transportadora,
          valor_frete: parseFloat(formData.valor_frete)
        })
      });
      const data = await response.json();
      console.log("Tipo da resposta: ", typeof data);
      console.log("Resposta da api: ", data);
      setResultado(data.previsao || data.erro);
    } catch (error) {
        setResultado('Erro ao conectar na api.');
    }
  };

  return(
    <div className="App">
      <h1>Previsão de Atraso de Entrega</h1>
      <form onSubmit={handleSubmit}>
        <input type="text" name="tipo_veiculo" placeholder="Tipo de Veículo" onChange={handleChange} required />
        <input type="text" name="UF_origem" placeholder="UF Origem" onChange={handleChange} required />
        <input type="text" name="UF_destino" placeholder="UF Destino" onChange={handleChange} required />
        <input type="text" name="transportadora" placeholder="Transportadora" onChange={handleChange} required />
        <input type="number" name="valor_frete" placeholder="Valor do Frete" onChange={handleChange} required />
        <button type="submit">Prever</button>
      </form>
      {resultado && <p>Resultado: {resultado}</p>}
    </div>
  );

}

export default App;