import { useState } from "react";
import "./App.css";

import CambiaNome from "./Esercizi/CambiaNome"
import LoginForm from "./Esercizi/LoginForm";
import CardUtente from "./Esercizi/CardUtente"
/*function getDate(date){
   return date.toLocaleDateString() + " " + new Date().toLocaleTimeString()
      }*/

   function App() {
    return (
      <div className="App">
        <h1>Esercizi React</h1>
        <CardUtente/>
        <LoginForm/>
        <CambiaNome/>
        </div>
    );
}
  
export default App;