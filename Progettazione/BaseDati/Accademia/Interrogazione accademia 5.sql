/* METODOLOGIA
1) fare prima un select * dalle tabelle che ci interessano;
2) visualizzare le caratteristiche delle righe che dobbiamo ottenere;
3) filtrare i risultati con where
 */
--1. Quali sono il nome, la data di inizio e la data di fine dei WP del progetto di nome ‘Pegasus’?
-- => occorre nome, data inizio e data fine dei wp e il nome del progetto che si trovano in due
-- tabelle diverse
select
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
    pe.nome,
    pe.cognome,
    pe.posizione
from
    Persona pe,
    Progetto pr,
    AttivitaProgetto att
where
    att.persona = pe.id
    and att.progetto = pr.id
    and pr.nome = 'Pegasus'
order by
    pe.cognome desc;

--3. Quali sono il nome, il cognome e la posizione degli strutturati che hanno più di
--una attività nel progetto ‘Pegasus’?
select
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
    and ap1.id <> ap2.id

--4. Quali sono il nome, il cognome e la posizione dei Professori Ordinari che hanno
--fatto almeno una assenza per malattia?
--5. Quali sono il nome, il cognome e la posizione dei Professori Ordinari che hanno
--fatto più di una assenza per malattia?
--6. Quali sono il nome, il cognome e la posizione dei Ricercatori che hanno almeno
--un impegno per didattica?
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
    and anp.persona = p.id

--9. Quali sono il nome e il cognome degli strutturati che nello stesso giorno hanno sia
--attività progettuali che attività non progettuali? Si richiede anche di proiettare il
--giorno, il nome del progetto, il tipo di attività non progettuali e la durata in ore di
--entrambe le attività.
--10. Quali sono il nome e il cognome degli strutturati che nello stesso giorno sono
--assenti e hanno attività pmrogettuali?
--11. Quali sono il nome e il cognome degli strutturati che nello stesso giorno sono
--assenti e hanno attività progettuali? Si richiede anche di proiettare il giorno, il
--nome del progetto, la causa di assenza e la durata in ore della attività progettuale.
--12. Quali sono i WP che hanno lo stesso nome, ma appartengono a progetti diversi?