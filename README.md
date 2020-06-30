Treeline
========

## Opis
**Turowa gra stategiczna 2D peer to peer.**

Gra opiera się na planszy złożonej z sześciokątnych płytek.
Na początku każdy z dwojga graczy ma przypisaną 1 płytkę terytorium z postawionym na niej ratuszem. Celem gry jest przejęcie płytki z ratuszem przeciwnika.
Gra polega na zdobywaniu zasobów (żywność, drewno i żelazo), stawianiu budynków i przejmowaniu terytorium.

Zasoby gracza zwiększają się co turę wg posiadanych płytek - mamy 3 rodzaje powierzni (las, trawę i góry), każdy generuje inną ilość innego surowca.
Dodatkowo zdobywanie zasobów można przyspieszyć stawiając na odpowiednich płytkach budynki: młyna, tartaku albo kopalni oraz przypisując robotników do tych budynków.
Na początku gracz otrzymuje 5 robotników. Kolejnych może "wyprodukować" budując dom, umieszczając w nim 2 robotników i co turę, z określonym prawdopodobieństwem (50%) otrzymuje nowego robotnika. 
Zasoby są wykorzystywane do stawiania budynków oraz przejmowania nowych płytek. Przejęcie następuje poprzez "zakup" płytki - każda płytka ma swoją cenę.
Cena płytki jest różna - płytki "niczyje: są tańsze niż płytki przeciwnika. Cenę płytek możemy zwiększyć stawiając budynek wieży obronnej - wtedy ceny płytek dookoła wieży rosną.

Komunilacja między graczami odbywa się przez peer to peer za pomocą socketów i własnego protokołu komunikacji.
Gra ma własny silnik (użyty PyGame) obsługujący rysowanie planszy, ruchomą kamerę, bieżace aktualizowanie grafiki (np. zmieniających się granic terytoriów, dostosowany interface).

Assets
------
Assets from https://opengameart.org/
