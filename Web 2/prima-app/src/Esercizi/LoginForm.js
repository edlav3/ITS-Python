import { useState } from "react";

const LoginForm = () => {
  const [cognome, setCognome] = useState("");
  const [nome, setNome] = useState("");
  const gestioneDati = (e) => {
    e.preventDefault();
    console.log(e);
    if (nome && cognome){
        setNome("")
        setCognome("")
    }else{
        alert("Inserisci tutti i campi")
    }
  };

  return (
    <div className="container">
      <form className="row g-3" onSubmit={gestioneDati}>
        <div className="col-md-6">
          <label htmlFor="nome">Nome</label>
          <input
            type="text"
            id="nome"
            className="form-control"
            value={nome}
            onChange={(event) => setNome(event.target.value)}
          ></input>
        </div>
        <div className="col-md-6">
          <label htmlFor="cognome">Cognome</label>
          <input
            type="text"
            id="cognome"
            value={cognome}
            onChange={(event) => setCognome(event.target.value)}
          ></input>
        </div>

        <button className="btn btn-success">Login</button>
      </form>
    </div>
  );
};

export default LoginForm;
