import { useState } from 'react';
import './App.css';
import { anagrafica } from './data/dati';
import Clock from './Clock';
import Componente1 from './Componente1';
import Stampanumeri from './Esercizi/StampaNumeri';
import Tabellina from './Esercizi/Tabellina';
import Stampanumerimoltiplicati from './Esercizi/Tabellina';
/*function getDate(date){
   return date.toLocaleDateString() + " " + new Date().toLocaleTimeString()
      }*/



function App() {
  let name = "Pippo"

  const [name1, setName1] = useState(name);

  const cambiaNome = () => {
    console.log(name);
    name = "Mario"
    setName1(name)
    console.log(name);
  };
  const elimina = (id) => {
    const newAnag = persone.filter(p => p.id !== id);
    setPersone(newAnag);
  };

  const [persone, setPersone] = useState({
    id:"1",
    nome:"Martino",
    cognome:"Valdinoci",
    età:50
  });

  const compleanno=()=>{
    let anni=persone.età+1;

    setPersone({
      ...persone,
      età:anni
    })
  }
  return (
    <>
      <div className="App">
        <h1>{name1}</h1>
        <button onClick={cambiaNome} className="btn btn-primary">
          Cambia Nome
        </button>
        {
          persone.map((p) => {
            return (<div><span>{p.name} {p.cognome}</span>
            <button onClick={() => {
              elimina(p.id);
            }}>
              elimina</button></div>)
          })
        }
        <button onClick={compleanno} className='btn btn-primary'>
          compleanno
        </button>
      </div>
    </>
  )

  /*let nome="Edoardo";
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
      getDate(new Date())
    }
    </h2>
  </div>
);*/
}

  export default App;