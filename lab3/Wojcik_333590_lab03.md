Kajetan Wójcik 333590
Python
https://github.com/Jukamapi/Ochrona-danych

Zad1:

ECB:
  Blok 1: a5ba2b6280d433bccfe6a0461cb88c4e
  Blok 2: a5ba2b6280d433bccfe6a0461cb88c4e
  Blok 3: a5ba2b6280d433bccfe6a0461cb88c4e
  Blok 4: a5ba2b6280d433bccfe6a0461cb88c4e

CBC:
  Blok 1: baeac0843b9c5891b238668e1f53970d
  Blok 2: eb090e72a1266472f3f44e5f35502c53
  Blok 3: ec8be3f3a87de42f096524ba59bd99ca
  Blok 4: f3d9ba4975e15415e8b070a7c57cbc09

Każdy blok w ECB był zaszyfrowany tak samo ponieważ algorytm szyfruje każdy blok osobno wykorzystując klucz którego długość była równa długości bloków.

CBC natomiast wykorzystuje początkowy IV i szyfruje każdy blok wykorzystując dane z poprzedniego bloku co sprawia że w zaszyfrowanych danych powtarzalność danych jest znikoma.

Zad2:

Test Puste dane:
    Długość wejścia: 0 B | Długość kryptogramu: 16 B
    Równość bajtów: True
Test 16 bajtów ASCII:
    Długość wejścia: 16 B | Długość kryptogramu: 32 B
    Równość bajtów: True
Test Plik wiadomosc.txt:
    Długość wejścia: 247 B | Długość kryptogramu: 256 B
    Równość bajtów: True

Porównanie szyfrowań tej samej wiadomości z nową solą i IV:
    Identyczne? False

Długości kryptogramu != długości danych wejściowych ponieważ w algorytmie dodawany jest padding. Wykorzystany jest styl "pkcs7", który dodaje bajty podając w nich ile paddingu dodał, np. jeżeli dodał trzy bajty to będą one wyglądać tak: 0x03 0x03 0x03. Dla zerowej długości danych dodaje on aż 16 bajtów aby algorytm wiedział podczas odszyfrowywania ile B musi usunąć.

Sól zabezpiecza przed atakami, które polegają na uzyskaniu tego samego klucza dla identycznego hasła. IV zapewnia losowość podczas procesu szyfrowania CBC.

Zad3:

5 najlepszych kandydatów:
  Znak: 'm' | Entropia H: 4.4536
  Znak: 'b' | Entropia H: 7.9472
  Znak: 'x' | Entropia H: 7.9490
  Znak: 'o' | Entropia H: 7.9493
  Znak: '2' | Entropia H: 7.9502

Odzyskany znak: 'm'

1 wiersz tekstu:
   "Record 000. The archive contains laboratory notes about symmetric encryption and careful handling of binary files."

Jest tylko 36 kluczy, ponieważ tylko tyle jest możliwych znaków a klucz tutaj jest 16-krotnością wybranego jednego zanku.

Ranking na podstawie entropi Shannona może zawieść dla danych skompresowanych, ponieważ po kompresji rozkład bajtów przemienia się w rozkład zbliżony do jednostajnego, czyli do maksymalnej entropii, przez to nie da się odróżnić poprawnej odpowiedzi od błędnej.