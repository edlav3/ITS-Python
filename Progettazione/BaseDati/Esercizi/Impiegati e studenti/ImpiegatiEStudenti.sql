create domain PosInteger as integer check (value >= 0);

create domain Stringa as varchar(100);

create type TipoRuolo as enum (
    'Segratario',
    'Direttore',
    'Progettista',
    'Impiegato'
);

create type Genere as enum ('M', 'F');

create domain CodiceFiscale as char(16) check (
    value ~ '^[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z]$'
);

create domain Reale as real check (value >= 0);

create table
    Persona (
        id PosInteger primary key,
        nome Stringa not null,
        cognome Stringa not null,
        nascita date not null,
        genere Genere not null,
        maternita PosInteger,
        check (
            (
                genere = 'F'
                and maternita is not null
            )
            or (
                genere = 'M'
                and maternita is null
            )
        ),
        posMilitare Stringa,
        check (
            (
                genere = 'M'
                and posMilitare is not null
            )
            or (
                genere = 'F'
                and posMilitare is null
            )
        ),
        is_studente boolean not null,
        matricola PosInteger unique,
        check (
            (
                is_studente
                and matricola is not null
            )
            or (
                not is_studente
                and matricola is null
            )
        ),
        is_impiegato boolean not null,
        stipendio Reale,
        check (
            (
                is_impiegato
                and stipendio is not null
            )
            or (
                not is_impiegato
                and stipendio is null
            )
        )
    );

create table
    Ruolo (
        persona PosInteger not null,
        foreign key (persona) references Persona (id),
        ruolo TipoRuolo not null,
        primary key (persona, ruolo),
        is_responsabile boolean,
        check (
            (
                is_responsabile
                and ruolo = 'Progettista'
            )
            or (
                not is_responsabile
                and ruolo <> 'Progettista'
            )
        )
    );

create table
    Progetto (
        id PosInteger not null,
        persona PosInteger not null,
        nome Stringa not null
    );

create table
    CF (
        persona PosInteger not null,
        foreign key (persona) references Persona (id),
        codice_fiscale CodiceFiscale not null,
        primary key (persona, codice_fiscale)
    );

INSERT INTO
    Persona (
        id,
        nome,
        cognome,
        nascita,
        genere,
        is_studente,
        is_impiegato
    )
VALUES
    (
        1,
        'Anna',
        'Rossi',
        '1990-05-12',
        'F',
        false,
        true
    ),
    (
        2,
        'Marco',
        'Bianchi',
        '1985-11-23',
        'M',
        false,
        true
    ),
    (
        3,
        'Giulia',
        'Verdi',
        '2000-02-10',
        'F',
        true,
        false
    ),
    (4, 'Luca', 'Neri', '1992-08-15', 'M', false, true),
    (
        5,
        'Laura',
        'Gialli',
        '1988-03-30',
        'F',
        false,
        false
    );

INSERT INTO
    Ruolo (persona, ruolo, is_responsabile)
VALUES
    (1, 'Impiegato', false),
    (1, 'Progettista', true),
    (2, 'Segratario', false),
    (3, 'Impiegato', false),
    (4, 'Direttore', true);

INSERT INTO
    CF (persona, codice_fiscale)
VALUES
    (1, 'RSSNNA90E55Z404Y'),
    (1, 'RSSNNA90E55Z405X'),
    (2, 'BNCMRC85S23Z404A'),
    (3, 'VRDGLI00B50Z404Z'),
    (4, 'NRILCU92M15Z404B');

INSERT INTO
    Progetto (id, nome)
VALUES
    (1, 'Sviluppo Software'),
    (2, 'Ricerca e Innovazione');