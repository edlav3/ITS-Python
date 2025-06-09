const arr1=[1, 23, 4, 5] // lista
console.log(arr1)
console.log(...arr1) // stampa gli oggetti destrutturati

const persona={
    "firts name": "Mario",
    cognome: "Sturniolo",
    indirizzo:{ // dizonario chiave valore
        via: "Cesare Pavese",
        civico: 305
    }
}

console.log(persona.indirizzo.via)

function person(){ // creazione di una classe
    this.cognome="";
    this.indirizzo.via="";
}

const {cognome, indirizzo} = persona
console.log(cognome, indirizzo)

// Script dei react
// <script src="https://unpkg.com/react@18/umd/react.development.js"></script>
// <script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>