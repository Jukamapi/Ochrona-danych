#!/usr/bin/python3
import os

print("Content-Type: text/plain; charset=utf-8\n")
print(f"UID: {os.geteuid()}, GID: {os.getegid()}")

sciezki = ["/lab-data/ogolny.txt", "/lab-data/poufny.txt"]

for sciezka in sciezki:
    print(f"\nPlik: {sciezka}")
    try:
        with open(sciezka, "r", encoding="utf-8") as f:
            print(f.read().strip())
    except PermissionError:
        print("Permission denied")
    except Exception as e:
        print(f"Błąd odczytu: {e}")
