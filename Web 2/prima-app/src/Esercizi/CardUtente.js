import React from 'react';

function Saluto({ utente }) {
  return (
    <div>
      <h2>{utente.nome}</h2>
      <p>{utente.email}</p>
      <img src={utente.imgUrl} alt="Avatar utente" />
    </div>
  );
}

export default Saluto;
