### Zadanie 1:
**Wejścia:**
* ' <- 0 wierszy
* ' OR '1'='1 <- 4 wiersze
* ' UNION SELECT name, sql FROM sqlite_master WHERE type='table'-- <- 2 wiersze
* SELECT wlasciciel, sekret FROM sekrety WHERE klucz = '' UNION SELECT klucz, wlasciciel FROM sekrety--' <- 4 wiersze
* ' UNION SELECT count(*), 'x' FROM sqlite_master-- <- 1 wiersz

**Zapytanie po wstawieniu danych:**
* ' OR '1'='1
* SELECT nazwa, wartosc FROM sekrety WHERE klucz = '' OR '1'='1'

**Nazwy tabel:**
* konta: CREATE TABLE konta(login TEXT, rola TEXT, email TEXT)
* sekrety: CREATE TABLE sekrety(klucz TEXT, wlasciciel TEXT, sekret TEXT)

**Odpowiedź:**
Dane wejściowe zawierające znaki specjalne SQL były zinterpretowane jako kod SQL, a nie jako dane, bo trafiły do zapytania przez sklejanie stringów


### Zadanie 2:
**Tabela:**
| Wejście:                                                                                               | przed | po  |
| ------------------------------------------------------------------------------------------------------ | ----- | --- |
| '                                                                                                      | 0     | 0   |
| ' OR '1'='1                                                                                            | 4     | 0   |
| ' UNION SELECT name, sql FROM sqlite_master WHERE type='table'--                                       | 2     | 0   |
| SELECT wlasciciel, sekret FROM sekrety WHERE klucz = '' UNION SELECT klucz, wlasciciel FROM sekrety--' | 4     | 0   |
| ' UNION SELECT count(*), 'x' FROM sqlite_master--                                                      | 1     | 0   |

**Fragment kodu z parametrem:** zapytanie = "SELECT wlasciciel, sekret FROM sekrety WHERE klucz = ?"

**Zapytanie d'Artagnan**: muszkieter: Jeden za wszystkich

**Jedno zdanie:** parametr jest przekazywany bazie danych osobno od treści zapytania , więc nie może zmienić struktury.

**Odpowiedź:** Nie, parametr nie może zastąpić nazwy tabeli ani kolumny, `?` działają tylko dla wartości literałów, nie dla identyfikatorów SQL.



### Zadadnie 3:

**Trzy wyrażenia z kroku 2:**
* `__import__('os').listdir('/etc'): Wynik: ['modules-load.d', 'mtab', 'hosts', 'crontabs', 'fstab', 'services', ...`
* `open('/etc/os-release').read(): Wynik: NAME="Alpine Linux" ID=alpine VERSION_ID=3.24.4...`
* `__import__('os').getuid(): Wynik: 1000`

**UID proesu:** 1000

**Tabela:**
| Wejście                            | Wynik                              | Kod HTTP |
| ---------------------------------- | ---------------------------------- | -------- |
| `2+3`                              | Wynik: 5.0                         | 200      |
| `7/2`                              | Wynik: 3.5                         | 200      |
| `-1.5*4`                           | Wynik: -6.0                        | 200      |
| `1/0`                              | Błąd: dzielenie przez zero         | 400      |
| `__import__('os').listdir('/etc')` | Błąd: niepoprawny format wyrażenia | 400      |
| `open('/etc/os-release').read()`   | Błąd: niepoprawny format wyrażenia | 400      |
| `__import__('os').getuid()`        | Błąd: niepoprawny format wyrażenia | 400      |
| `[puste wejście]`                  | Błąd: puste wyrażenie              | 400      |

**Jedno zdanie:** biała lista dozwolonych operacji (`+ - * /` na liczbach) jest bezpieczna, ponieważ znamy wszytkie możliwe działania i są one bezpieczne, podczas gdy blokowanie słów typu `import` nie jest całkowicie odporne, ponieważ atakujący może ominąć filtr w inny sposób, czarne listy zawsze mogą mieć lukę, a biała lista z definicji jej nie ma.

