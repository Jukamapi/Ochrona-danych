"""Sejf sekretow i kalkulator - celowo podatna aplikacja do laboratorium 7.

Uruchamiaj wylacznie lokalnie, w kontenerze z pakietu. Dane sa fikcyjne.
"""
import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)
BAZA = "file:/dane/sekrety.db?mode=ro"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/sekret")
def sekret():
    klucz = request.args.get("klucz", "")
    zapytanie = "SELECT wlasciciel, sekret FROM sekrety WHERE klucz = ?"
    wiersze, blad = [], None
    try:
        with sqlite3.connect(BAZA, uri=True) as db:
            wiersze = db.execute(zapytanie, (klucz,)).fetchall()
    except sqlite3.Error:
        app.logger.exception("Błąd zapytania do sekretów (klucz=%r)", klucz)
        blad = "Wystąpił błąd podczas wykonywania zapytania."
    return render_template("sekret.html", klucz=klucz, zapytanie=zapytanie, wiersze=wiersze, blad=blad)


import re

WZORZEC = re.compile(
    r'^\s*(-?\d+(?:\.\d+)?)\s*([+\-*/])\s*(-?\d+(?:\.\d+)?)\s*$'
)

def oblicz(wyrazenie: str) -> float:
    if len(wyrazenie) > 100:
        raise ValueError("wyrażenie zbyt długie")

    dopasowanie = WZORZEC.match(wyrazenie)
    if not dopasowanie:
        raise ValueError("niepoprawny format wyrażenia")

    a_str, operator, b_str = dopasowanie.groups()
    a = float(a_str)
    b = float(b_str)

    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            raise ZeroDivisionError("dzielenie przez zero")
        return a / b


@app.route("/kalkulator")
def kalkulator():
    wyrazenie = request.args.get("wyrazenie")

    if wyrazenie is None:
        return render_template("kalkulator.html", wyrazenie=None, wynik=None)

    if wyrazenie == "":
        app.logger.warning("Puste wyrażenie")
        return render_template(
            "kalkulator.html", wyrazenie=wyrazenie, wynik="Błąd: puste wyrażenie"
        ), 400

    try:
        wynik = oblicz(wyrazenie)
        return render_template("kalkulator.html", wyrazenie=wyrazenie, wynik=wynik)
    except (ValueError, ZeroDivisionError) as exc:
        app.logger.warning("Błędne wyrażenie %r: %s", wyrazenie, exc)
        return render_template(
            "kalkulator.html", wyrazenie=wyrazenie, wynik=f"Błąd: {exc}"
        ), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
