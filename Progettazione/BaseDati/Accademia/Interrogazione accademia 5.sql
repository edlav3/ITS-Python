--1. Quali sono il nome, la data di inizio e la data di fine dei WP del progetto di nome ‘Pegasus’?
select distinct
    wp.nome,
    wp.inizio,
    wp.fine
from
    Progetto pr,
    WP wp
where
    pr.id = wp.progetto
    and pr.nome = 'Pegasus';

--2. Quali sono il nome, il cognome e la posizione degli strutturati che hanno almeno
--una attività nel progetto ‘Pegasus’, ordinati per cognome decrescente?
select distinct
    p.nome,
    p.cognome,
    p.posizione
from
    Persona p,
    Progetto pr,
    AttivitaProgetto a
where
    a.persona = p.id
    and a.progetto = pr.id
    and pr.nome = 'Pegasus'
order by
    cognome desc;

--3. Quali sono il nome, il cognome e la posizione degli strutturati che hanno più di
--una attività nel progetto ‘Pegasus’?
select distinct
    pers.nome,
    pers.cognome,
    pers.posizione
from
    Persona pers,
    AttivitaProgetto ap1,
    AttivitaNonProgettuale ap2 Progetto prog
where
    prog.nome = 'Pegasus'
    and ap1.persona = = pers.id
    and ap2.persona = pers.id
    and ap1.progetto = prog.id
    and ap2.progetto = prog.id
    and ap1.id <> ap2.id;

--4. Quali sono il nome, il cognome e la posizione dei Professori Ordinari che hanno
--fatto almeno una assenza per malattia?
select distinct
    pe.nome,
    pe.cognome,
    pe.posizione
from
    persona pe,
    Assenza a
where
    pe.id = a.persona
    and pe.posizione = 'Professore Ordinario'
    and a.tipo = 'Malattia';

--5. Quali sono il nome, il cognome e la posizione dei Professori Ordinari che hanno
--fatto più di una assenza per malattia?
select distinct
    p.nome,
    p.cognome,
    p.posizione
from
    Persona p,
    Assenza a1,
    Assenza a2
where
    p.id = a1.persona
    and p.id = a2.persona
    and a1.tipo = 'Malattia'
    and a2.tipo = 'Malattia'
    and a1.giorno <> a2.giorno
    and p.posizione = 'Professore Ordinario';

--6. Quali sono il nome, il cognome e la posizione dei Ricercatori che hanno almeno
--un impegno per didattica
--7. Quali sono il nome, il cognome e la posizione dei Ricercatori che hanno più di un impegno per didattica?
--8. Quali sono il nome e il cognome degli strutturati che nello stesso giorno hanno sia
--attività progettuali che attività non progettuali?
select distinct
    p.nome,
    p.cognome
from
    persona p,
    AttivitaProgetto ap,
    AttivitaNonProgettuale anp
where
    ap.giorno = anp.giorno
    and ap.persona = p.id
    and anp.persona = p.id;

--9. Quali sono il nome e il cognome degli strutturati che nello stesso giorno hanno sia
--attività progettuali che attività non progettuali? Si richiede anche di proiettare il
--giorno, il nome del progetto, il tipo di attività non progettuali e la durata in ore di
--entrambe le attività
select distinct
    p.nome,
    p.cognome,
    anp.giorno,
    anp.tipo,
    ap.tipo,
    anp.oreDurata,
    ap.oreDurata
from
    AttivitaNonProgettuale anp,
    AttivitaProgetto ap,
    persona p
where
    anp.giorno = ap.giorno
    and anp.persona = p.id
    and ap.persona = p.id;

--10. Quali sono il nome e il cognome degli strutturati che nello stesso giorno sono
--assenti e hanno attività progettuali?
select distinct
    pe.nome,
    pe.cognome
from
    Assenza az,
    AttivitaProgetto att,
    persona pe
where
    pe.id = att.persona
    and pe.id = az.persona
    and az.giorno = att.giorno;

--11. Quali sono il nome e il cognome degli strutturati che nello stesso giorno sono
--assenti e hanno attività progettuali? Si richiede anche di proiettare il giorno, il
--nome del progetto, la causa di assenza e la durata in ore della attività progettuale.
select distinct
    pe.nome,
    pe.cognome,
    a.giorno,
    pr.nome,
    a.tipo,
    ap.oreDurata
from
    Persona pe,
    Assenza a,
    AttivitaProgetto ap,
    Progetto pr
where
    pe.id = a.persona
    and pe.id = ap.persona
    and a.giorno = ap.giorno
    and ap.progetto = pr.id;

--12. Quali sono i WP che hanno lo stesso nome, ma appartengono a progetti diversi?
select distinct
    wp1.nome
from
    wp wp1,
    wp wp2
where
    wp1.nome = wp2.nome
    and wp1.progetto <> wp2.progetto;