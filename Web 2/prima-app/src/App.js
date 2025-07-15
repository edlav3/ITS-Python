import { useState } from "react";
import "./App.css";
import CleanUp from "./Esercizi/CleanUp";
import { anagrafica } from "./data/dati";
import CambiaNome from "./Esercizi/CambiaNome"
import Clock from "./Clock";
import Componente1 from "./Componente1";
import Stampanumeri from "./Esercizi/StampaNumeri";
import Tabellina from "./Esercizi/Tabellina";
import Stampanumerimoltiplicati from "./Esercizi/Tabellina";
import LoginForm from "./Esercizi/LoginForm";
/*function getDate(date){
   return date.toLocaleDateString() + " " + new Date().toLocaleTimeString()
      }*/

   function App() {
    return (
      <div className="App">
        <h1>Esercizi React</h1>
        <LoginForm/>
        <CambiaNome/>
        </div>
    );
}
  
export default App;