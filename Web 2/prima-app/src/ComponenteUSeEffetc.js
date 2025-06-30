import React from "react";

const Esempio=()=>{
    const[count, setCount]=useState(0);
    useEffect(()=>{
        console.log("Ho chiamato UseEffetct")
        if (count<1){
            document.title="nessun titolo"
        }
        else{
            document.title="ho trovato qualcosa"
        }
    });
    console.log("Sono fuori dallo UseEffect")
    return (
        <>
        <div>Esempio</div>
        <button onClick={() => setCount(count+1)}>Incrementa</button>&nbsp;
        </>
    );
};

export default Esempio;