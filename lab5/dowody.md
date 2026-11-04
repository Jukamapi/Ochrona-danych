====================ZAD1================

```bash
PS C:\Users\kajet\Programming\lab5\pliki-dla-studentow> curl -i http://127.0.0.1:8080/materialy/
HTTP/1.1 200 OK
Date: Wed, 04 Nov 2026 11:33:46 GMT
Server: Apache
Content-Length: 305
Content-Type: text/html;charset=ISO-8859-1

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
 <head>
  <title>Index of /materialy</title>
 </head>
 <body>
<h1>Index of /materialy</h1>
<ul><li><a href="/"> Parent Directory</a></li>
<li><a href="notatka.txt"> notatka.txt</a></li>
</ul>
</body></html>
PS C:\Users\kajet\Programming\lab5\pliki-dla-studentow> curl -i http://127.0.0.1:8080/materialy/notatka.txt
HTTP/1.1 200 OK
Date: Wed, 04 Nov 2026 11:34:16 GMT
Server: Apache
Last-Modified: Wed, 04 Nov 2026 11:22:31 GMT
ETag: "45-65f7198470bc0"
Accept-Ranges: bytes
Content-Length: 69
Content-Type: text/plain; charset=UTF-8

Publiczna notatka: ten plik ma pozostac dostepny pod znanym adresem.

PS C:\Users\kajet\Programming\lab5\pliki-dla-studentow> curl -i http://127.0.0.1:8080/wewnetrzne/
HTTP/1.1 200 OK
Date: Wed, 04 Nov 2026 11:35:02 GMT
Server: Apache
Content-Length: 301
Content-Type: text/html;charset=ISO-8859-1

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
 <head>
  <title>Index of /wewnetrzne</title>
 </head>
 <body>
<h1>Index of /wewnetrzne</h1>
<ul><li><a href="/"> Parent Directory</a></li>
<li><a href="plan.txt"> plan.txt</a></li>
</ul>
</body></html>
PS C:\Users\kajet\Programming\lab5\pliki-dla-studentow> curl -i http://127.0.0.1:8080/wewnetrzne/plan.txt
HTTP/1.1 200 OK
Date: Wed, 04 Nov 2026 11:35:06 GMT
Server: Apache
Last-Modified: Wed, 04 Nov 2026 11:22:31 GMT
ETag: "3a-65f7198470bc0"
Accept-Ranges: bytes
Content-Length: 58
Content-Type: text/plain; charset=UTF-8

Fikcyjny plan: ten katalog ma byc niedostepny przez HTTP.




web-1  | 172.18.0.1 - - [04/Nov/2026:11:33:46 +0000] "GET /materialy/ HTTP/1.1" 200 305
web-1  | 172.18.0.1 - - [04/Nov/2026:11:34:16 +0000] "GET /materialy/notatka.txt HTTP/1.1" 200 69
web-1  | 172.18.0.1 - - [04/Nov/2026:11:35:02 +0000] "GET /wewnetrzne/ HTTP/1.1" 200 301
web-1  | 172.18.0.1 - - [04/Nov/2026:11:35:06 +0000] "GET /wewnetrzne/plan.txt HTTP/1.1" 200 58



PS C:\Users\kajet\Programming\lab5\pliki-dla-studentow> docker compose exec web httpd -t
>>
Syntax OK




web-1  | [Wed Nov 04 11:38:21.080537 2026] [mpm_event:notice] [pid 1:tid 1] AH00492: caught SIGWINCH, shutting down gracefully
web-1 exited with code 0 (restarting)





PS C:\Users\kajet\Programming\lab5\pliki-dla-studentow> curl -i http://127.0.0.1:8080/materialy/
>>
HTTP/1.1 403 Forbidden
Date: Wed, 04 Nov 2026 11:39:01 GMT
Server: Apache
Content-Length: 239
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html><head>
<title>403 Forbidden</title>
</head><body>
<h1>Forbidden</h1>
<p>You don't have permission to access this resource.</p>
</body></html>
PS C:\Users\kajet\Programming\lab5\pliki-dla-studentow> curl -i http://127.0.0.1:8080/materialy/notatka.txt
>>
HTTP/1.1 200 OK
Date: Wed, 04 Nov 2026 11:39:10 GMT
Server: Apache
Last-Modified: Wed, 04 Nov 2026 11:22:31 GMT
ETag: "45-65f7198470bc0"
Accept-Ranges: bytes
Content-Length: 69
Content-Type: text/plain; charset=UTF-8

Publiczna notatka: ten plik ma pozostac dostepny pod znanym adresem.
PS C:\Users\kajet\Programming\lab5\pliki-dla-studentow> curl -i http://127.0.0.1:8080/wewnetrzne/
>>
HTTP/1.1 403 Forbidden
Date: Wed, 04 Nov 2026 11:39:15 GMT
Server: Apache
Content-Length: 239
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html><head>
<title>403 Forbidden</title>
</head><body>
<h1>Forbidden</h1>
<p>You don't have permission to access this resource.</p>
</body></html>
PS C:\Users\kajet\Programming\lab5\pliki-dla-studentow> curl -i http://127.0.0.1:8080/wewnetrzne/plan.txt
>>
HTTP/1.1 403 Forbidden
Date: Wed, 04 Nov 2026 11:39:19 GMT
Server: Apache
Content-Length: 239
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html><head>
<title>403 Forbidden</title>
</head><body>
<h1>Forbidden</h1>
<p>You don't have permission to access this resource.</p>
</body></html>







web-1  | [Wed Nov 04 11:39:01.094391 2026] [autoindex:error] [pid 11:tid 17] [client 172.18.0.1:47814] AH01276: Cannot serve directory /usr/local/apache2/htdocs/materialy/: No matching DirectoryIndex (index.html) found, and server-generated directory index forbidden by Options directive
web-1  | 172.18.0.1 - - [04/Nov/2026:11:39:01 +0000] "GET /materialy/ HTTP/1.1" 403 239
web-1  | 172.18.0.1 - - [04/Nov/2026:11:39:10 +0000] "GET /materialy/notatka.txt HTTP/1.1" 200 69
web-1  | [Wed Nov 04 11:39:15.671167 2026] [authz_core:error] [pid 11:tid 34] [client 172.18.0.1:57938] AH01630: client denied by server configuration: /usr/local/apache2/htdocs/wewnetrzne/
web-1  | 172.18.0.1 - - [04/Nov/2026:11:39:15 +0000] "GET /wewnetrzne/ HTTP/1.1" 403 239
web-1  | [Wed Nov 04 11:39:19.549372 2026] [authz_core:error] [pid 10:tid 16] [client 172.18.0.1:37882] AH01630: client denied by server configuration: /usr/local/apache2/htdocs/wewnetrzne/plan.txt
web-1  | 172.18.0.1 - - [04/Nov/2026:11:39:19 +0000] "GET /wewnetrzne/plan.txt HTTP/1.1" 403 239



PS C:\Users\kajet\Programming\lab5\pliki-dla-studentow> docker compose logs --tail 30 web
>>
web-1  | [Wed Nov 04 11:33:25.025225 2026] [mpm_event:notice] [pid 1:tid 1] AH00489: Apache/2.4.69(Unix) configured -- resuming normal operations
web-1  | [Wed Nov 04 11:33:25.025415 2026] [core:notice] [pid 1:tid 1] AH00094: Command line: 'httpd -D FOREGROUND'
web-1  | 172.18.0.1 - - [04/Nov/2026:11:33:46 +0000] "GET /materialy/ HTTP/1.1" 200 305
web-1  | 172.18.0.1 - - [04/Nov/2026:11:34:16 +0000] "GET /materialy/notatka.txt HTTP/1.1" 200 69
web-1  | 172.18.0.1 - - [04/Nov/2026:11:35:02 +0000] "GET /wewnetrzne/ HTTP/1.1" 200 301
web-1  | 172.18.0.1 - - [04/Nov/2026:11:35:06 +0000] "GET /wewnetrzne/plan.txt HTTP/1.1" 200 58
web-1  | [Wed Nov 04 11:38:21.080537 2026] [mpm_event:notice] [pid 1:tid 1] AH00492: caught SIGWINCH, shutting down gracefully
web-1  | [Wed Nov 04 11:38:23.318935 2026] [mpm_event:notice] [pid 1:tid 1] AH00489: Apache/2.4.69(Unix) configured -- resuming normal operations
web-1  | [Wed Nov 04 11:38:23.319037 2026] [core:notice] [pid 1:tid 1] AH00094: Command line: 'httpd -D FOREGROUND'
web-1  | [Wed Nov 04 11:39:01.094391 2026] [autoindex:error] [pid 11:tid 17] [client 172.18.0.1:47814] AH01276: Cannot serve directory /usr/local/apache2/htdocs/materialy/: No matching DirectoryIndex (index.html) found, and server-generated directory index forbidden by Options directive
web-1  | 172.18.0.1 - - [04/Nov/2026:11:39:01 +0000] "GET /materialy/ HTTP/1.1" 403 239
web-1  | 172.18.0.1 - - [04/Nov/2026:11:39:10 +0000] "GET /materialy/notatka.txt HTTP/1.1" 200 69
web-1  | [Wed Nov 04 11:39:15.671167 2026] [authz_core:error] [pid 11:tid 34] [client 172.18.0.1:57938] AH01630: client denied by server configuration: /usr/local/apache2/htdocs/wewnetrzne/
web-1  | 172.18.0.1 - - [04/Nov/2026:11:39:15 +0000] "GET /wewnetrzne/ HTTP/1.1" 403 239
web-1  | [Wed Nov 04 11:39:19.549372 2026] [authz_core:error] [pid 10:tid 16] [client 172.18.0.1:37882] AH01630: client denied by server configuration: /usr/local/apache2/htdocs/wewnetrzne/plan.txt
web-1  | 172.18.0.1 - - [04/Nov/2026:11:39:19 +0000] "GET /wewnetrzne/plan.txt HTTP/1.1" 403 239
```

====================ZAD2==========================
```bash

PS C:\Users\kajet\Programming\lab5\pliki-dla-studentow> docker compose exec web httpd -t
Syntax OK





PS C:\Users\kajet\Programming\lab5\pliki-dla-studentow>     curl -i http://127.0.0.1:8080/panel/raport.txt
>>
HTTP/1.1 401 Unauthorized
Date: Wed, 04 Nov 2026 11:42:51 GMT
Server: Apache
WWW-Authenticate: Basic realm="Laboratorium 5"
Content-Length: 421
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html><head>
<title>401 Unauthorized</title>
</head><body>
<h1>Unauthorized</h1>
<p>This server could not verify that you
are authorized to access the document
requested.  Either you supplied the wrong
credentials (e.g., bad password), or your
browser doesn't understand how to supply
the credentials required.</p>
</body></html>





PS C:\Users\kajet\Programming\lab5\pliki-dla-studentow> curl -i -u student http://127.0.0.1:8080/panel/raport.txt
Enter host password for user 'student':
HTTP/1.1 401 Unauthorized
Date: Wed, 04 Nov 2026 11:46:11 GMT
Server: Apache
WWW-Authenticate: Basic realm="Laboratorium 5"
Content-Length: 421
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html><head>
<title>401 Unauthorized</title>
</head><body>
<h1>Unauthorized</h1>
<p>This server could not verify that you
are authorized to access the document
requested.  Either you supplied the wrong
credentials (e.g., bad password), or your
browser doesn't understand how to supply
the credentials required.</p>
</body></html>





PS C:\Users\kajet\Programming\lab5\pliki-dla-studentow> curl -i -u student http://127.0.0.1:8080/panel/raport.txt
Enter host password for user 'student':
HTTP/1.1 200 OK
Date: Wed, 04 Nov 2026 11:46:35 GMT
Server: Apache
Last-Modified: Wed, 04 Nov 2026 11:22:31 GMT
ETag: "3a-65f7198470bc0"
Accept-Ranges: bytes
Content-Length: 58
Content-Type: text/plain; charset=UTF-8

Raport cwiczeniowy: dostep po poprawnym uwierzytelnieniu




PS C:\Users\kajet\Programming\lab5\pliki-dla-studentow> curl -i http://127.0.0.1:8080/
HTTP/1.1 200 OK
Date: Wed, 04 Nov 2026 11:46:56 GMT
Server: Apache
Last-Modified: Wed, 04 Nov 2026 11:22:31 GMT
ETag: "15f-65f7198470bc0"
Accept-Ranges: bytes
Content-Length: 351
Content-Type: text/html; charset=UTF-8

<!doctype html>
<html lang="pl"><meta charset="utf-8"><title>Laboratorium 5</title>
<h1>Laboratorium 5: serwer WWW działa</h1>
<p>Materiały ćwiczeniowe do konfiguracji dostępu w Apache.</p>
<ul><li><a href="/materialy/">Materiały</a></li>
<li><a href="/wewnetrzne/">Wewnętrzne</a></li>
<li><a href="/panel/raport.txt">Panel</a></li></ul></html>
```



====================ZAD3================

```bash

PS C:\Users\kajet\Programming\lab5\pliki-dla-studentow> docker compose exec web ls -ln /lab-data/
>>
total 8
-rw-r-----    1 0        2               48 Nov  4 11:22 ogolny.txt
-rw-------    1 0        2               61 Nov  4 11:22 poufny.txt



PS C:\Users\kajet\Programming\lab5\pliki-dla-studentow> curl -i http://127.0.0.1:8080/cgi-bin/uprawnienia.cgi
>>
HTTP/1.1 200 OK
Date: Wed, 04 Nov 2026 11:57:27 GMT
Server: Apache
Transfer-Encoding: chunked
Content-Type: text/plain; charset=utf-8

UID: 2, GID: 2

Plik: /lab-data/ogolny.txt
LAB05: dokument dostepny dla grupy procesu WWW.

Plik: /lab-data/poufny.txt
Permission denied






PS C:\Users\kajet\Programming\lab5\pliki-dla-studentow> curl -i http://127.0.0.1:8080/cgi-bin/uprawnienia.cgi
>>
HTTP/1.1 401 Unauthorized
Date: Wed, 04 Nov 2026 11:59:27 GMT
Server: Apache
WWW-Authenticate: Basic realm="Laboratorium 5"
Content-Length: 421
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html><head>
<title>401 Unauthorized</title>
</head><body>
<h1>Unauthorized</h1>
<p>This server could not verify that you
are authorized to access the document
requested.  Either you supplied the wrong
credentials (e.g., bad password), or your
browser doesn't understand how to supply
the credentials required.</p>
</body></html>





PS C:\Users\kajet\Programming\lab5\pliki-dla-studentow> curl -i -u student http://127.0.0.1:8080/cgi-bin/uprawnienia.cgi
Enter host password for user 'student':
HTTP/1.1 200 OK
Date: Wed, 04 Nov 2026 11:59:53 GMT
Server: Apache
Transfer-Encoding: chunked
Content-Type: text/plain; charset=utf-8

UID: 2, GID: 2

Plik: /lab-data/ogolny.txt
LAB05: dokument dostepny dla grupy procesu WWW.

Plik: /lab-data/poufny.txt
Permission denied
```