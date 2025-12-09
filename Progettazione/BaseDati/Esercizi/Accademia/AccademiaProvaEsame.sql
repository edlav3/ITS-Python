1.
select
    nome
from
    progetto
where
    progetto.fine > '2023-12-31';

2.
select
    posizione,
    count(id)
from
    persona
group by
    posizione;

3.
select
    p.id,
    p.nome
from
    persona p,
    assenza a
where
    p.id = a.persona
    and a.tipo = 'Malattia';

4.
select
    tipo,
    count(id)
from
    assenza a,
group by
    tipo;

5.
select
    max(stipendio)
from
    persona
where
    persona.posizione = 'Professore Ordinario';

6.
select
    id,
    tipo,
    oreDurata
from
    AttivitaProgetto ap
where
    ap.persona = 1
    and ap.progetto = 4
order by
    oreDurata desc;

7.
select
    p.nome,
    p.cognome,
    a.tipo,
    count(*)
from
    assenza a,
    persona p
where
    a.persona = p.id
group by
    p.nome,
    p.cognome,
    a.tipo;

8.
with
    mspo (
        select
            max(stipendio) as max_stipendio
        from
            personawhere posizione = 'Professore Ordinario'
    )
select
    *
from
    persona p,
    mspo
where
    p.stipendio = mspo.max_stipendio