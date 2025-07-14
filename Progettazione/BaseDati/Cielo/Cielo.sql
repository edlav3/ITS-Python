create domain PosInteger as integer check (value >= 0);
create domain StringaM as varchar(100);
create domain CodIATA as char(3);

create table Compagnia (
    nome StringaM,
    annoFondaz PosInteger not null,
    primary key(nome)
);
create table LuogoAeroporto (
    aeroporto CodIATA,
    citta StringaM,
    nazione StringaM,
    primary key(aeroporto)
);
create table Aeroporto (
    codice CodIATA,
    nome StringaM,
    primary key(codice),
    foreign key(codice) references LuogoAeroporto(aeroporto)
);
create table ArrPart (
    codice PosInteger,
    comp StringaM not null,
    arrivo CodIATA,
    partenza CodIATA,
    primary key(codice, comp),
    foreign key(arrivo) references Aeroporto(codice),
    foreign key(partenza) references Aeroporto(codice),
    check(arrivo <> partenza)
);
create table Volo (
    codice PosInteger,
    comp StringaM not null,
    durataminuti PosInteger,
    primary key(codice, comp),
    foreign key(comp) references Compagnia(nome),
    foreign key(codice, comp) references ArrPart(codice, comp)
);

begin transaction; -- questa parte di codice serve per eseguire in blocco tutto quello che scrivo prima del commit finale

insert into Compagnia (nome, annoFondaz)
values ('alitalia', 1234),
    ('rayanair', 2026),
    ('itscyber', 12);
insert into LuogoAeroporto (aeroporto, citta, nazione)
values ('FCO', 'roma', 'italia'),
    ('KRK', 'cracovia', 'polonia'),
    ('BOH', 'dubai', 'emirati arabi');
insert into Aeroporto (codice, nome)
values ('FCO', 'aeroporto de roma'),
    ('KRK', 'aeroporto cracovia'),
    ('BOH', 'aeroporto dubai');
insert into ArrPart (codice, comp, arrivo, partenza)
values (1001, 'alitalia', 'FCO', 'KRK'),
    (1002, 'rayanair', 'KRK', 'FCO'),
    (1003, 'itscyber', 'BOH', 'FCO');
insert into Volo (codice, comp, durataminuti)
values (1001, 'alitalia', 12),
    (1002, 'rayanair', 90),
    (1003, 'itscyber', 4000);

commit; -- solo a questo punto, i dati vengono controllati

select * from Volo;
select * from ArrPart;
select * from Aeroporto;
select * from LuogoAeroporto;