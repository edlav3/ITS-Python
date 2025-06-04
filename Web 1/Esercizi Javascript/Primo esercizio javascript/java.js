function controllaCampo() {
  const campo1 = document.getElementById("nome");
  const campo2 = document.getElementById("cognome")
  const campo4 = document.getElementById("telefono")
  const campo5 = document.getElementById("mail")

  if (campo1.value === "") {
    alert("Il campo Nome e' vuoto");
  }
  if (campo2.value === "") {
      alert("Il campo Cognome e' vuoto")
  }
  if (campo4.value === "") {
      alert("Il campo Telefono e' vuoto")
  }
  if (campo5.value === "") {
      alert("Il campo E-mail e' vuoto")
  }
}

function controllaNumeri(){
    const campo3 = document.getElementById("matricola")
    const valore = campo3.value;
    const soloNumeri = /^\d+$/;
    if (!soloNumeri.test(valore)) {
        alert("Il campo Matricola non puo' contenere lettere");
    }
}

function controllaRegione(){
    const scelta = document.getElementById("regione")
    const regioneScelta = scelta.value;
    if (regioneScelta === "") {
        alert("Inserisci una regione")
    }
}