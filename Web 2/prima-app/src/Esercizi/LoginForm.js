import React from 'react'
import { useState } from 'react'

const LoginForm = () => {
    const [input, setInput] = useState({ // rinominato da persone a input
        nome: "",
        cognome: ""
    });

    const [persone, setPersone] = useState([]); // persone ora è un array

    const gestioneDati = (e) => {
        e.preventDefault();
        if (input.nome && input.cognome) {
            setPersone([
                ...persone,
                { ...input }
            ]);
            setInput({ nome: "", cognome: "" }); // reset campi
        } else {
            alert("Inserisci tutti i dati");
        }
        console.log(e);
    };

    const handlerChange = (e) => {
        setInput({ ...input, [e.target.name]: e.target.value }); // corretto e.targetvalue -> e.target.value
    };

    const animale = {
        "razza": "gatto",
        "zampe": "4"
    };
    let strRazza = "razza";
    const animale2 = {
        ...animale,
        [strRazza]: "cane"
    };
    console.log(animale2.razza);

    return (
        <div className="container">
            <form className="row g-3" onSubmit={gestioneDati}>
                <div className="col-md-6">
                    <label htmlFor="nome">Nome</label>
                    <input
                        type="text"
                        id="nome"
                        className="form-control"
                        required
                        name="nome"
                        value={input.nome}
                        onChange={handlerChange}
                    ></input>
                </div>
                <div className="col-md-6">
                    <label htmlFor="cognome">Cognome</label>
                    <input
                        type="text"
                        id="cognome"
                        className="form-control"
                        required
                        name="cognome"
                        value={input.cognome}
                        onChange={handlerChange}
                    ></input>
                </div>
                <button className="btn btn-success">Login</button>
            </form><br></br>
            <div>
                {
                    persone.map((p, index) => {
                        return (<p key={index}>{p.nome} {p.cognome}</p>)
                    })
                }
            </div>
        </div>
    )
}

export default LoginForm