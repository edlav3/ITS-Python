create domain PosInteger as integer check (value >= 0);

create domain Stringa as varchar(80);

create domain AnnoComp as integer check (value >= 1900);

create domain CodeIATA as varchar(3) check (value ~ '^[A-Z]{3}$');

create domain CodeVolo as varchar(6) check (value ~ '^[A-Z]{2}[0-9]{4}$');

create table
    Nazione (id PosInteger primary key, nome Stringa);

create table
    Citta (
        id PosInteger primary key,
        nome Stringa not null,
        abitanti PosInteger,
        nazione PosInteger,
        foreign key (nazione) references Nazione (id)
    );

create table
    Compagnia (
        id PosInteger primary key,
        nome Stringa not null,
        anno AnnoComp,
        citta PosInteger,
        foreign key (citta) references Citta (id)
    );

create table
    Aeroporto (
        id PosInteger primary key,
        codice CodeIATA,
        citta PosInteger,
        foreign key (citta) references Citta (id)
    );

create table
    Volo (
        id PosInteger primary key,
        codice CodeVolo,
        durata_min PosInteger,
        partenza PosInteger,
        arrivo PosInteger,
        compagnia PosInteger,
        foreign key (partenza) references Aeroporto (id),
        foreign key (arrivo) references Aeroporto (id),
        check (arrivo <> partenza),
        foreign key (compagnia) references Compagnia (id)
    );