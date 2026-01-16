-- 1. Quanti sono gli strutturati di ogni fascia?
select
    posizione,
    count(posizione)
from
    persona
group by
    posizione;

-- 2. Quanti sono gli strutturati con stipendio ≥ 40000?
select
    count(persona)
from
    persona
where
    persona.stipendio >= 40000;

-- 3. Quanti sono i progetti già finiti che superano il budget di 50000?
select
    count(progetto)
from
    progetto
where
    progetto.fine < CURRENT_DATE
    and progetto.budget > 5000;

-- 4. Qual è la media, il massimo e il minimo delle ore delle attività relative al progetto ‘Pegasus’?
select
    avg(oreDurata),
    max(oreDurata),
    min(oreDurata)
from
    progetto,
    AttivitaProgetto
where
    progetto.nome = 'Pegasus'
    and progetto.id = attivitaprogetto.progetto;

-- 5. Quali sono le medie, i massimi e i minimi delle ore giornaliere dedicate al progetto
-- ‘Pegasus’ da ogni singolo docente?
select
    att.persona,
    avg(att.oreDurata),
    max(att.oreDurata),
    min(att.oreDurata)
from
    progetto p,
    attivitaprogetto att
where
    p.nome = 'Pegasus'
    and att.progetto = p.id
group by
    att.persona;

-- 6. Qual è il numero totale di ore dedicate alla didattica da ogni docente?
select
    att.persona,
    sum(att.oreDurata)
from
    AttivitaNonProgettuale att
where
    att.tipo = 'Didattica'
group by
    att.persona;

-- 7. Qual è la media, il massimo e il minimo degli stipendi dei ricercatori?
select
    avg(p.stipendio),
    max(p.stipendio),
    min(p.stipendio)
from
    persona p
where
    p.posizione = 'Ricercatore';

-- 8. Quali sono le medie, i massimi e i minimi degli stipendi dei ricercatori, dei professori
-- associati e dei professori ordinari?
select
    p.posizione avg(p.stipendio),
    max(p.stipendio),
    min(p.stipendio)
from
    persona p
where
    p.posizione = 'Ricercatore'
    or p.posizione = 'Professore Ordinario'
    or p.posizione = 'Professore Associato'
group by
    p.posizione;

-- 9. Quante ore ‘Ginevra Riva’ ha dedicato ad ogni progetto nel quale ha lavorato?
select
    att.tipo,
    sum(att.oreDurata)
from
    persona p,
    attivitaprogetto att
where
    att.persona = p.id
    and p.nome = 'Ginevra'
    and p.cognome = 'Riva'
group by
    att.tipo;

-- 10. Qual è il nome dei progetti su cui lavorano più di due strutturati?
select
    p.nome
from
    progetto p,
    attivitaprogetto att
where
    p.id = att.progetto
group by
    p.nome
having
    count(distinct att.persona) > 2;

-- 11. Quali sono i professori associati che hanno lavorato su più di un progetto?
select
    pe.nome,
    pe.cognome
from
    persona pe,
    attivitaprogetto att,
    progetto pr
where
    pr.id = att.progetto
    and att.persona = pe.id
    and pe.posizione = 'Professore Associato'
group by
    pe.nome,
    pe.cognome
having
    count(distinct att.progetto) > 1;