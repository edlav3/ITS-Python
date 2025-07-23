create domain CodiceFiscale as char check (value ~ '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}$');

create domain PartitaIva as char check (value ~ '^[0-9]{11}$');

create domain IntGEZ as integer check (value >= 0);

create domain RealGEZ as numeric check (value >= 0);

create domain RealBzo as numeric check (
    value > 0
    and value < 1
);

create type Indirizzo (
    via as varchar(50),
    civico as IntGEZ,
    cap as char(5) check (value ~ '^[0-9]{5}(-[0-9]{4})?$')
);


create type statoOrdine as enum(
    'Da saldare',
    'Saldato',
    'In preparazione',
    'Inviato'
);

create domain Telefono as varchar (10);

create domain Email as varchar check (value ~ '%^[A-Za-z0-9._%\-+!#$&/=?^|~]+@[A-Za-z0-9.-]+[.][A-Za-z]+$%');


create domain stringa as varchar;


create table nazione (
	nome stringa primary key
);

create table regione (
	nome stringa not null,
	nazione stringa not null,
	primary key (nome, nazione),
	foreign key (nazione) references nazione(nome)
);

create table citta (
	id IntGEZ primary key,
	nome stringa not null,
	regione stringa not null,
	nazione stringa not null,
	unique (nome, regione, nazione),
	foreign key (regione, nazione)
		references regione(nome, nazione)
);

create table direttore (
    nome stringa not null,
    congome stringa not null, 
    cf CodiceFiscale not null,
    servizio IntGEZ not null, 
    nascita date not null,
    citta IntGEZ not null,
    foreign key (citta) references citta(id)
    primary key (cf)
);

create table dipartimento (
	nome stringa primary key,
	indirizzo indirizzo not null
	citta IntGEZ not null,
	foreign key (citta) references citta(id)
    direttore stringa not null,
    foreign key (direttore) references direttore(cf)
);

create table fornitore (
    nome stringa not null,
    iva PartitaIva primary key,
    indirizzo Indirizzo not null,
    telefono Telefono not null,
    email Email not null,
    citta IntGEZ not null,
    foreign key(citta) references citta(id)
);

create table ordine (
	codice IntGEZ primary key,
	data_stipula date not null,
	imponibile RealGEZ not null,
	aliquota RealBzo not null,
	descrizione stringa not null,
	dipartimento stringa not null,
	foreign key (dipartimento)
		references dipartimento(nome)
    stato statoOrdine not null,
    fornitore PartitaIva not null,
    foreign key (fornitore) references fornitore(iva)
);