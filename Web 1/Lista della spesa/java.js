function aggiungiCarrello() {
    var prodotto = document.getElementById("prodotto").value;

    if (prodotto.trim() !== "") {
        var lista = document.getElementById("listaspesa");
        var inserito = document.createElement("li");
        inserito.textContent = prodotto;
        lista.appendChild(inserito);
        document.getElementById("prodotto").value = ""; // pulisce il campo
    } else {
        alert("Nessun prodotto inserito");
    }
}

function eliminaCarrello(){
    document.getElementById("listaspesa").innerHTML = "";
}