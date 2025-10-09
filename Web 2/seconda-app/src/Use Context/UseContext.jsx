import React, { useContext, useState } from "react";

/*
Obiettivo: creare un 'contesto', che possiamo immaginare come un 'wrapper'
che ci permette di avvolgere e impacchetare componenti.
E' come se creassimo un componente che contiene componenti.
*/


const data = [
    { id: 1, name: "Andrea" },
    { id: 2, name: "Mirko" },
    { id: 3, name: "Antonio" },
    { id: 4, name: "Anna" },
  ];
  
  const AppContex= React.createContext()
  
  const MainComponent = () => {
    const [people, setPeople] = useState(data);
  
    const removePeople = (id) => setPeople(people.filter((el) => el.id !== id));
    
    return (
      <AppContex.Provider value={{people,removePeople}}>
      <div>
        <h3>Passaggio di Proprietà a cascata </h3>
        <Elenco people={people} removePeople={removePeople} />
      </div>
      </AppContex.Provider>
    );
  };
  
  const Elenco = () => {
      const context= useContext(AppContex)
      console.log("context",context)
      const {people,removePeople}=context
    return (
      <div>
        {people.map((el, index) => {
          return <Persona key={index} {...el} removePeople={removePeople} />;
        })}
      </div>
    );
  };
  
  const Persona = ({ id, name }) => {
      const {removePeople}=useContext(AppContex)
    return (
      <div className="item">
        <h5> {name} </h5>
        <button className="button delete-button" onClick={() => removePeople(id)}>
          {" "}
          x{" "}
        </button>
      </div>
    );
  };
  
  export default MainComponent

/*
E' come se avessi messo People e RemovePeople dentro ad una 'scatola'
*/