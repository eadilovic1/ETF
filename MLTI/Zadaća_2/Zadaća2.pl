zubar(z1).
zubar(z2).

radno_vrijeme(z1, 8, 16).
radno_vrijeme(z2, 16, 24).

:- dynamic termin/5.

termin(z1, [1, 1, 2025], 8, popunjeno, mujo).
termin(z1, [1, 1, 2025], 9, popunjeno, fata).
termin(z1, [1, 1, 2025], 10, slobodno, _).
termin(z1, [1, 1, 2025], 11, slobodno, _).
termin(z1, [1, 1, 2025], 12, popunjeno, suljo).
termin(z1, [1, 1, 2025], 13, slobodno, _).
termin(z1, [1, 1, 2025], 14, slobodno, _).
termin(z1, [1, 1, 2025], 15, slobodno, _).

termin(z2, [1, 1, 2025], 16, slobodno, _).
termin(z2, [1, 1, 2025], 17, slobodno, _).
termin(z2, [1, 1, 2025], 18, popunjeno, haso).
termin(z2, [1, 1, 2025], 19, slobodno, _).
termin(z2, [1, 1, 2025], 20, slobodno, _).
termin(z2, [1, 1, 2025], 21, slobodno, _).
termin(z2, [1, 1, 2025], 22, popunjeno, huso).
termin(z2, [1, 1, 2025], 23, slobodno, _).

% Definicija pravila za provjeru prestupne godine
prestupna_godina(Godina) :-
    (Godina mod 4 =:= 0, Godina mod 100 =\= 0) ;
    (Godina mod 400 =:= 0).

% Pravilo za provjeru broja dana u mjesecu
broj_dana(1, _, 31).  % Januar
broj_dana(2, Godina, D) :- prestupna_godina(Godina) -> D = 29 ; D = 28. % Februar
broj_dana(3, _, 31).  % Mart
broj_dana(4, _, 30).  % April
broj_dana(5, _, 31).  % Maj
broj_dana(6, _, 30).  % Juni
broj_dana(7, _, 31).  % Juli
broj_dana(8, _, 31).  % August
broj_dana(9, _, 30).  % Septembar
broj_dana(10, _, 31). % Oktobar
broj_dana(11, _, 30). % Novembar
broj_dana(12, _, 31). % Decembar

% Pravilo za provjeru ispravnosti datuma
ispravan_datum([Dan, Mjesec, Godina]) :-
    Mjesec >= 1, Mjesec =< 12,
    Godina > 0,
    broj_dana(Mjesec, Godina, MaxDan),
    Dan >= 1, Dan =< MaxDan.

% Pravilo za provjeru ispravnosti vremena
ispravno_vrijeme(Zubar, Sat) :-
    radno_vrijeme(Zubar, Pocetak, Kraj),
    Pocetak >= 0, Pocetak =< 23,
    Kraj >= 0, Kraj =< 24,
    Sat >= Pocetak, Sat < Kraj.

% Provjera dostupnosti
dostupan(Zubar, [Dan, Mjesec, Godina], Sat) :-
    ispravan_datum([Dan, Mjesec, Godina]),
    ispravno_vrijeme(Zubar, Sat),
    termin(Zubar, [Dan, Mjesec, Godina], Sat, slobodno, _).

% Predikat za rezervaciju termina
rezervisi_termin(Zubar, [D, M, G], Sat, Pacijent) :-
    dostupan(Zubar, [D, M, G], Sat),
    termin(Zubar, [D, M, G], Sat, slobodno, _),
    retract(termin(Zubar, [D, M, G], Sat, slobodno, _)),
    assert(termin(Zubar, [D, M, G], Sat, popunjeno, Pacijent)).

% Predikat za otkazivanje termina
otkazi_termin(Zubar, [Dan, Mjesec, Godina], Sat) :-
    ispravan_datum([Dan, Mjesec, Godina]),
    ispravno_vrijeme(Zubar, Sat),
    termin(Zubar, [Dan, Mjesec, Godina], Sat, popunjeno, _),
    retract(termin(Zubar, [Dan, Mjesec, Godina], Sat, popunjeno, _)),
    assert(termin(Zubar, [Dan, Mjesec, Godina], Sat, slobodno, _)).

% Pretraga svih zubara
svi_zubari(Zubari) :-
    findall(Zubar, zubar(Zubar), Zubari).

% Pretraga svih slobodnih termina
svi_slobodni_termini(Slobodni) :-
    findall(
        [Zubar, D, M, G, H],
        (zubar(Zubar), termin(Zubar, [D, M, G], H, slobodno, _)),
        Slobodni
    ).

% Ispis svih slobodnih termina kod svih zubara
ispisi_slobodne_termine :-
    svi_slobodni_termini(Slobodni),
    forall(
        member([Zubar, D, M, G, H], Slobodni),
        (format('Zubar: ~w Datum: ~d.~d.~d. Vrijeme: ~d~n', [Zubar, D, M, G, H]))
    ).

% Pretraga svih zauzetih termina
svi_zauzeti_termini(Zauzeti) :-
    findall(
        [Zubar, D, M, G, H, Pacijent],
        (zubar(Zubar), termin(Zubar, [D, M, G], H, popunjeno, Pacijent)),
        Zauzeti
    ).

% Ispis svih zauzetih termina kod svih zubara
ispisi_zauzete_termine :-
    svi_zauzeti_termini(Zauzeti),
    forall(
        member([Zubar, D, M, G, H, Pacijent], Zauzeti),
        (format('Zubar: ~w Datum: ~d.~d.~d. Vrijeme: ~d Pacijent: ~w~n',
                [Zubar, D, M, G, H, Pacijent]))
    ).
