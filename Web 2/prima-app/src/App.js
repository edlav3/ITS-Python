import './App.css';
import Clock from './Clock';
import Componente1 from './Componente1';
import Stampanumeri from './Esercizi/StampaNumeri';
import Tabellina from './Esercizi/Tabellina';
import Stampanumerimoltiplicati from './Esercizi/Tabellina';
/*function getDate(date){
   return date.toLocaleDateString() + " " + new Date().toLocaleTimeString()
      }*/


function App() {

  let nome="Edoardo";
  return (
    <div className="App">
      <Stampanumeri></Stampanumeri>
      <h2>-------------------</h2>
      <Tabellina numero="15"></Tabellina>
      <h1>Primo Elemento {nome}</h1>
      <Componente1>Edoardo</Componente1>
      <Componente1/>
      <br></br>
      <h2>
      {
        new Date().toLocaleDateString() + " " + new Date().toLocaleTimeString()
      }
      <br></br>
      <br></br>
      Importo il componente clock <Clock timezone="0" country="Italia"></Clock>
      <br></br>
      {/*
      getDate(new Date())*/
      }
      </h2>
    </div>
  );
}

export default App;