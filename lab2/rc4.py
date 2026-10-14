import sys
import math
import time
import string
import itertools

def rc4_crypt(data: bytes, key: bytes) -> bytes:
    keylength = len(key)
    S = [i for i in range(256)]
    j = 0

    for i in range(256):
        j = (j + S[i] + key[i % keylength]) % 256
        S[i], S[j] = S[j], S[i]

    i = 0
    j = 0
    out = bytearray(len(data))

    for idx, byte in enumerate(data):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]

        out[idx] = byte ^ K

    return bytes(out)

def calculate_entropy(data: bytes) -> float:
    if not data:
        return 0.0
    freq = [0] * 256
    for b in data:
        freq[b] += 1
    n = len(data)
    ent = 0.0
    for c in freq:
        if c > 0:
            p = c / n
            ent -= p * math.log2(p)
    return ent

def main():
    if len(sys.argv) < 2:
        sys.exit(1)

    # 1
    test_data = b"Weryfikacja symetrii RC4: 12345"
    test_key = b"abc"
    assert rc4_crypt(rc4_crypt(test_data, test_key), test_key) == test_data

    with open(sys.argv[1], "rb") as f:
        ciphertext = f.read()

    sample = ciphertext[:512]
    alphabet = string.ascii_lowercase

    start_time = time.time()
    candidates = []

    # brute force
    for p in itertools.product(alphabet, repeat=3):
        k = "".join(p).encode("ascii")
        dec_sample = rc4_crypt(sample, k)
        ent = calculate_entropy(dec_sample)
        candidates.append((ent, k, dec_sample))

    candidates.sort(key=lambda x: (x[0], x[1]))
    elapsed = time.time() - start_time

    best_ent, best_key, _ = candidates[0]

    for rank, (ent, k, dec_s) in enumerate(candidates[:5], 1):
        print(f"{rank}. klucz: {k.decode()} | entropia: {ent:.4f} | początek: {repr(dec_s[:40])}")

    print(f"\nN przetestowanych kluczy: {len(candidates)} w czasie: {elapsed:.2f} s")
    print(f"Najlepszy klucz: {best_key.decode()}")

    full_decrypted = rc4_crypt(ciphertext, best_key)

    assert rc4_crypt(full_decrypted, best_key) == ciphertext
    with open("rc4.txt", "wb") as f:
        f.write(full_decrypted)

    ent_c = calculate_entropy(ciphertext)
    ent_d = calculate_entropy(full_decrypted)

    print(f"Entropia kryptogramu: {ent_c:.4f}")
    print(f"Entropia odszyfrowania: {ent_d:.4f}")

if __name__ == "__main__":
    main()