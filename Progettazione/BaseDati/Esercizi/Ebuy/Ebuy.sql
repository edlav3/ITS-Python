create domain PosInteger as integer check (value >= 0);

create domain Stringa as varchar(300);

create domain Voto as integer check (
    value >= 1
    and value <= 5
);

create domain RealGZ as real check (value >= 0);

create table
    Utente (
        username Stringa primary key,
        registrazione timestamp not null
    );

create table
    Categoria (
        nome Stringa primary key,
        super Stringa,
        foreign key (super) references Categoria (nome),
        check (
            super is null
            or nome <> super
        )
    )
create table
    PostOggetto (
        codice PosInteger primary key,
        descrizione Stringa not null,
        pubblicazione timestamp not null,
        ha_feedback boolean not null,
        voto Voto,
        commento Stringa,
        istante_feedback timestamp,
        check (
            (
                ha_feedback = true
                and voto is not null
                and istante_feedback is not null
            )
            or (
                ha_feedback = false
                and voto is null
                and istante_feedback is null
                and commento is null
            )
        ),
        utente Stringa not null,
        foreign key (utente) references Utente (username),
        tipo char not null check (
            tipo = "Asta"
            or tipo = "CompraloSubito"
        ),
        categoria Categoria not null,
        foreign key (categoria) references Categoria (nome),
    );

create table
    MetodoPagamento (nome Stringa primary key)
create table
    met_post (
        postoggetto integer not null,
        metodo Stringa not null,
        foreign key (postoggetto) references PostOggetto (codice),
        foreign key (metodo) references MetodoPagamento (nome),
        primary key (postoggetto, metodo)
    )
create table
    PostOggettoAsta (
        codice PosInteger primary key,
        foreign key (codice) references PostOggetto (codice),
        prezzo_base RealGZ not null,
        prezzo_bid RealGZ not null,
        scadenza timestamp not null
    );

create table
    PostOggettoCompraloSubito (
        codice PosInteger primary key,
        foreign key (codice) references PostOggetto (codice),
        prezzo RealGZ not null
    );

create table
    Bid (
        istante date not null,
        id PosInteger not null,
        primary key (istante, id),
        foreign key (utente) references Utente (username),
        foreign key (codice) references PostOggettoAsta (codice)
    );

