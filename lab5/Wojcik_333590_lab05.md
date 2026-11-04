### Zadanie 1:

**Tabela adresów i kodów HTTP:**
| Adres URL                | Kod przed zmianą | Widoczna lista plików? |  Kod po zmianie   |
| :----------------------- | :--------------: | :--------------------: | :---------------: |
| `/materialy/`            |    **200 OK**    |          Tak           | **403 Forbidden** |
| `/materialy/notatka.txt` |    **200 OK**    |   Nie (treść pliku)    |    **200 OK**     |
| `/wewnetrzne/`           |    **200 OK**    |          Tak           | **403 Forbidden** |
| `/wewnetrzne/plan.txt`   |    **200 OK**    |   Nie (treść pliku)    | **403 Forbidden** |

* **Wpis z logu serwera potwierdzający odmowę dostępu:**
  `[Wed Nov 04 11:39:19.549372 2026] [authz_core:error] [pid 10:tid 16] [client 172.18.0.1:37882] AH01630: client denied by server configuration: /usr/local/apache2/htdocs/wewnetrzne/plan.txt`
* **Wyjaśnienie:**
  `Options -Indexes` blokuje tylko generowanie automatycznego indeksu katalogu, gdy brakuje pliku indeksowego, pozwalając na pobranie znanych plików, a blokada dostępu `Require all denied` odrzuca wszystkie żądania HTTP do całej wskazanej ścieżki.

### Zadanie 2:

**Kody HTTP z prób:**
1. `/panel/raport.txt` bez danych logowania: **401 Unauthorized**
2. `/panel/raport.txt` z błędnym hasłem: **401 Unauthorized**
3. `/panel/raport.txt` z poprawnym hasłem: **200 OK**
4. Strona główna `/` bez logowania: **200 OK**

* **Wartość nagłówka WWW-Authenticate (bez logowania):**
  `Basic realm="Laboratorium 5"`
* **Wyjaśnienie:**
  Uwierzytelnianie HTTP Basic przesyła poświadczenie tylko zakodowane przez Base64 bez żadnego szyfrowania, przez co w kanale HTTP dane użyte do logowania są przesyłane tak naprawdę jawnym tekstem i sprawia to, że są bardzo podatne na przechwycenie.

### Zadanie 3:

* **UID i GID procesu CGI:**
  `UID: 2`, `GID: 2` (użytkownik/grupa `daemon`)
* **Właściciele i prawa obu plików (`ls -ln /lab-data/`):**
  * `ogolny.txt`: uprawnienia `-rw-r-----`, właściciel UID `0`, grupa GID `2`
  * `poufny.txt`: uprawnienia `-rw-------`, właściciel UID `0`, grupa GID `2`
* **Wyniki odczytu z poziomu CGI:**
  * `/lab-data/ogolny.txt`: Odczytano poprawnie (`LAB05: dokument dostepny dla grupy procesu WWW.`)
  * `/lab-data/poufny.txt`: Odmowa odczytu (`Permission denied`)
* **Kody HTTP:**
  * Przed włączeniem Basic: **200 OK**
  * Po włączeniu Basic bez logowania: **401 Unauthorized**
  * Po włączeniu Basic z poprawnym hasłem: **200 OK**
* **Wyjaśnienie:**
  Uwierzytelnienie w serwerze WWW zachodzi na poziomie Apache, natomiast CGI jest uruchamiany w systemie jako proces serwera o stałych uprawnieniach i podlega tylko ograniczeniom uprawnień POSIX Linuksa.

### dowody.md:
W tym pliku jest większość komend których używałem, oraz ich odpowiedzi.