import { useState } from "react";
import App from "../App";

const CambiaNome = () => {
  const [name, setName] = useState("Roberto");

  const cambia = () => {
    if (name === "Roberto") {
      setName("Mario");
    } else {
      setName("Roberto");
    }
  };
  
  return (
    <div>
      <h3>{name}</h3>
      <button className="btn btn-dark" onClick={cambia}>
        Cambia Nome
      </button>
    </div>
  );
};

export default CambiaNome;