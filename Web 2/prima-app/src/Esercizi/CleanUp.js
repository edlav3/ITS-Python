import React, { useEffect, useState } from 'react'

const CleanUp = () => {
    
    const [size, setSize,]=useState(window.innerWidth); /* qui
    stiamo dicendo di inizializzare la variabile size alla larghezza della pagina*/
    
    const dimensione=()=>{
        setSize(window.innerWidth)
    }
    useEffect(()=>{
        window.addEventListener("resize", dimensione());
        return(()=>{
            window.removeEventListener("resize", dimensione())
        });// questo return è un CleanUp, lo sfruttiamo in modo che in ogni listener
        // (cronologia di eventi), non ci sia una lista troppo lunga
        // in quanto, grazie a questa riga, ad ogni modifica sovrascrive il listner precedente
    })
    return (
        <h1>Dimensione: {size}</h1>
    )
}

export default CleanUp