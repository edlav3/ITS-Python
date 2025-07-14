--1: Quali sono i voli (codice e nome della compagnia) la cui durata supera le 3 ore?
select * from volo where durataminuti > 180;

--2: Quali sono le compagnie che hanno voli che superano le 3 ore?
select distinct volo.comp from volo where durataminuti > 180;

--3: Quali sono i voli (codice e nome della compagnia) che partono dall’aeroporto con codice ‘CIA’?
select codice, comp from ArrPart where partenza='CIA';

--4: Quali sono le compagnie che hanno voli che arrivano all’aeroporto con codice FCO
select distinct comp from ArrPart where arrivo='FCO';

--5: Quali sono i voli (codice e nome della compagnia)
--che partono dall’aeroporto ‘FCO’ e arrivano all’aeroporto ‘JFK’?
select codice, comp from ArrPart where partenza='FCO' and arrivo='JFK';

--6: Quali sono le compagnie che hanno voli che partono dall’aeroporto
--‘FCO’ e atterrano all’aeroporto ‘JFK’?
select comp from ArrPart where partenza='FCO' and arrivo='JFK';

--7: Quali sono i nomi delle compagnie che hanno voli diretti
---dalla città di ‘Roma’ alla città di ‘New York’?
select distinct ap.comp
from ArrPart as ap, LuogoAeroporto as l1, LuogoAeroporto as l2
where ap.partenza=l1.aeroporto
and ap.arrivo=l2.aeroporto
and l1.citta='Roma'
and l2.citta='New York';

--8: Quali sono gli aeroporti (con codice IATA, nome e luogo) nei quali partono voli
--della compagnia di nome ‘MagicFly’?
select  distinct LuogoAeroporto.aeroporto, LuogoAeroporto.citta, LuogoAeroporto.nazione from ArrPart, LuogoAeroporto
where ArrPart.comp='MagicFly';