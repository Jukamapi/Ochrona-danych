Zadanie 1:

dokumenty/budzet.csv: BŁĄD
dokumenty/dane.bin: OK
dokumenty/harmonogram.txt: BRAK
dokumenty/kontakt.txt: OK
dokumenty/regulamin.txt: OK

SHA256('Ala ma kota.'): 9b9ae722342758f4bb6a5dd94470ddfab3c95cda15186231f53bb4666e657605
SHA256('Ola ma kota.'): f7f49ccc3e7308f936f9cb71a792c3526663e9ddee89dc3e38fb83db4f308535
N różniących się bitów: 131

Suma kontrolna zapisana w nieszyfrowanym pliku obok danych nie ochroni przed podmianą, ponieważ można wyliczyć nową sumę i podmienić też plik sum, do ochrony powinno się użyć podpisu cyfrowego i kluczy.



Zadanie 2:

weryfikacja: anna, 'Kasztan-2026' -> True
weryfikacja: anna, 'kasztan-2026' -> False
weryfikacja: piotr, 'Żółw na łące' -> True
weryfikacja: kasia, 'Kasztan-2026' -> False

sól test1 == sól test2: False
skrót test1 == skrót test2: False
weryfikacja test1: True
weryfikacja test2: True

Sól uniemożliwia wykrycie jednakowych haseł u różnych użytkowników
Duża liczba iteracji celowo spowalnia obliczenia, co utrudnia ataki brute force



Zadadnie 3:

para kolizyjna: v_oryginał = 7282, v_zmieniony = 1761, h24 = aac6b9
liczba wariantów zmienionego o h24 równym h24(oryginał_wariant_0): 0

Znalezienie dowolnej pary o wspólnym skrócie wynika z paradoksu urodzinowego