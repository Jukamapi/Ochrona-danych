Zadanie 1:
klucz = 233 | wynik: 100.00% | tekst: b'The Night Ferry\n\nThe night ferry left the harbour '

Entropia histogramu 0-255 nie rozstrzygnie które przesunięcie jest poprawnym. Entropia Shannona zależy tylko od częstotliwości występowania wartości. Przez to że szyfr Cezara jest tylko przesunięciem, odszyfrowanie każdego z kluczy da dokładnie taki sam zbiór częstości i entropia będzie identyczna.

Zadanie 2:
Kryptogramy tekstu 'BRAMABRAMABRAMA':
klucz SZYFR: 95ac9a9393 95ac9a9393 95ac9a9393
klucz KOD: 8da1859890 869d90918c 91968c9c85

Ponieważ długość klucza SZYFR wynosi 5, czyli tyle samo co długość okresowo powtarzającego się słowa BRAMA w tekście, każde wystąpienie jest sumowane dokładnie tymi samymi bajtami, co sprawia że utworzą się te same bajty. Klucz KOD natomiast ma inną długość i szyfrowanie będzie robione przesuniętymi fazami jak np KODKO, DKODK, ODKOD.

Zadanie 3:
1. klucz: tat | entropia: 4.3910 | początek: b"The Clockmaker's Apprentice\n\nOn his firs"
2. klucz: neg | entropia: 7.4304 | początek: b"\xe0m\x94\x94\xc5\xeb\xf6\x0b\xc8'\x91\x92\x08\xdd7\xd7\xabj \xc6\xad\xadn\xb8*\x91\xab5Hu\xcc<\xa4\x04\xba\xf9\x8aTn%"
3. klucz: mcn | entropia: 7.4512 | początek: b'V\xafMy\x04\xbb\x03_\xd8\xf1\xffq\x17\\\x01\xe4\x96h\xe7\x0e\xffH\xbb\xbbP\x90E\xf3\x07KF|@\x05\x80z`\x95\xfa5'
4. klucz: oxo | entropia: 7.4536 | początek: b'\xf4%Q\xa6\xb4\xbe\xec\x83\x7f\x0ecT\xda\x08\xa4?\xbc\xad\xbc\xa51\xb5\xaa\xd1\x02\x84\xaa\xa1\xa8\x98\xa6>e\x93\xd9MI\x08\xe6\xe9'
5. klucz: tnx | entropia: 7.4592 | początek: b'\xb3\x00f\xaen\xf3\xae\x98\xbb\xc0\x86\xa0p\xe8\xbbGHW\x0eA\xb6j(Bjp\x9b\xecP\xa21\xa0+u\xebxc\xd9/\x0c

N przetestowanych kluczy: 17576 w czasie: 8.13 s
Najlepszy klucz: tat
Entropia kryptogramu: 7.9271
Entropia odszyfrowania: 4.3259

Ponieważ szyfrowanie wykorzystuje operację XOR, która po zaaplikowaniu ponownie przywróci oryginalną wartość, ale sprawdzi to tylko czy kod został poprawnie zaimplementowany a nie pozwoli odszyfrować wiadomość używając błędnego klucza.

Ranking entropii zawiódłby, gdyby tekst sam w sobie miał wysoką entropię zbliżoną do losowej lub tekst byłby za krótki