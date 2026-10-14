import sys

def score_candidate(data: bytes) -> float:
    valid = 0
    for b in data:
        if 32 <= b <= 126 or b in (9, 10, 13):
            valid += 1
    return valid / len(data) if data else 0.0

def decrypt_caesar(data: bytes, k: int) -> bytes:
    return bytes((b - k) % 256 for b in data)

def main():
    if len(sys.argv) < 2:
        sys.exit(1)

    with open(sys.argv[1], "rb") as f:
        ciphertext = f.read()

    candidates = []
    for k in range(256):
        dec = decrypt_caesar(ciphertext, k)
        sc = score_candidate(dec)
        candidates.append((sc, k, dec))

    candidates.sort(key=lambda item: (-item[0], item[1]))

    for rank, (sc, k, dec) in enumerate(candidates[:5], 1):
        preview = repr(dec[:50])
        print(f"{rank}. klucz = {k:3d} | wynik: {sc * 100:6.2f}% | tekst: {preview}")

    choice = input("\nWybierz wartość k do zapisu: ")
    if choice.isdigit() and 0 <= int(choice) <= 5:
        chosen_k = int(choice)
    else:
        chosen_k = candidates[0][1]

    decrypted = decrypt_caesar(ciphertext, chosen_k)
    with open("cezar.txt", "wb") as f:
        f.write(decrypted)

    print(f"\nZapisano odszyfrowany plik 'cezar.txt' dla k = {chosen_k}.")

if __name__ == "__main__":
    main()