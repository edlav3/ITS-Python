-- 1. Quanti sono gli strutturati di ogni fascia?

select posizione, count(posizione) 
from persona
group by posizione;

-- 2. Quanti sono gli strutturati con stipendio ≥ 40000?

select count(persona)
from persona
where persona.stipendio >= 40000;

-- 3. Quanti sono i progetti già finiti che superano il budget di 50000?

select count(progetto)
from progetto
where progetto.fine < CURRENT_DATE and progetto.budget > 5000;

-- 4. Qual è la media, il massimo e il minimo delle ore delle attività relative al progetto ‘Pegasus’?

select avg(oreDurata), max(oreDurata), min(oreDurata)
from progetto, AttivitaProgetto
where progetto.nome = 'Pegasus' and progetto.id = attivitaprogetto.progetto;
