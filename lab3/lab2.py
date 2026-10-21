import collections
import itertools
import math
import os
import string
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def zad1():
    print("\n" + "=" * 15 + "zad 1" + "=" * 15)

    key_hex = "000102030405060708090a0b0c0d0e0f"
    key = bytes.fromhex(key_hex)
    data = b'0123456789ABCDEF' * 4
    iv = get_random_bytes(16)

    ecb = AES.new(key, AES.MODE_ECB)
    cbc = AES.new(key, AES.MODE_CBC, iv=iv)

    ct_ecb = ecb.encrypt(data)
    ct_cbc = cbc.encrypt(data)

    blocks_ecb = [ct_ecb[i : i + 16] for i in range(0, 64, 16)]
    blocks_cbc = [ct_cbc[i : i + 16] for i in range(0, 64, 16)]

    print("\nECB:")
    for idx, b in enumerate(blocks_ecb, 1):
        print(f"  Blok {idx}: {b.hex()}")

    print("\nCBC:")
    for idx, b in enumerate(blocks_cbc, 1):
        print(f"  Blok {idx}: {b.hex()}")

    dec_cipher_ecb = AES.new(key, AES.MODE_ECB)
    pt_ecb = dec_cipher_ecb.decrypt(ct_ecb)

    dec_cipher_cbc = AES.new(key, AES.MODE_CBC, iv=iv)
    pt_cbc = dec_cipher_cbc.decrypt(ct_cbc)


def derive_key(password: str, salt: bytes) -> bytes:
    return PBKDF2(password, salt, dkLen=32, count=200_000, hmac_hash_module=SHA256)

def encrypt_password_cbc(data: bytes, password: str):

    salt = get_random_bytes(16)
    iv = get_random_bytes(16)
    key = derive_key(password, salt)

    padded_data = pad(data, 16, style="pkcs7")
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    ciphertext = cipher.encrypt(padded_data)

    return ciphertext, salt, iv

def decrypt_password_cbc(ciphertext: bytes, password: str, salt: bytes, iv: bytes) -> bytes:

    key = derive_key(password, salt)
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    padded_data = cipher.decrypt(ciphertext)

    return unpad(padded_data, 16, style="pkcs7")

def zad2():
    print("\n" + "=" * 15 + "zad 2" + "=" * 15)
    password = "test123"

    with open("wiadomosc.txt", "rb") as f:
        file_bytes = f.read()

    test_cases = [
        ("Puste dane", b""),
        ("16 bajtów ASCII", b"0123456789ABCDEF"),
        ("Plik wiadomosc.txt", file_bytes),
    ]

    for name, original in test_cases:
        ct, salt, iv = encrypt_password_cbc(original, password)
        recovered = decrypt_password_cbc(ct, password, salt, iv)

        print(f"Test {name}:")
        print(f"    Długość wejścia: {len(original)} B | Długość kryptogramu: {len(ct)} B")
        print(f"    Równość bajtów: {recovered == original}")

    ct1, _, _ = encrypt_password_cbc(file_bytes, password)
    ct2, _, _ = encrypt_password_cbc(file_bytes, password)
    print(f"\nPorównanie szyfrowań tej samej wiadomości z nową solą i IV:")
    print(f"    Identyczne? {ct1 == ct2}")


def calculate_entropy(data: bytes) -> float:
    if not data:
        return 0.0

    length = len(data)
    counts = collections.Counter(data)
    entropy = 0.0
    for count in counts.values():
        p_b = count / length
        entropy -= p_b * math.log2(p_b)
    return entropy


def zad3(file_path="slaby_ecb.bin"):
    print("\n" + "=" * 15 + "zad 3" + "=" * 15)

    with open(file_path, "rb") as f:
        ciphertext = f.read()

    sample = ciphertext[:4096]
    charset = string.ascii_lowercase + string.digits
    candidates = []

    for ch in charset:
        key = ch.encode("ascii") * 16
        cipher = AES.new(key, AES.MODE_ECB)
        decrypted_sample = cipher.decrypt(sample)
        h = calculate_entropy(decrypted_sample)
        candidates.append((ch, h, key))

    candidates.sort(key=lambda item: item[1])

    print("5 najlepszych kandydatów:")
    for ch, h, _ in candidates[:5]:
        print(f"  Znak: '{ch}' | Entropia H: {h:.4f}")

    best_char, best_h, best_key = candidates[0]
    cipher_full = AES.new(best_key, AES.MODE_ECB)
    decrypted_full = cipher_full.decrypt(ciphertext)
    plaintext = unpad(decrypted_full, 16, style="pkcs7")

    first_line = plaintext.decode("utf-8", errors="replace").splitlines()[0]
    print(f"\nOdzyskany znak: '{best_char}'")
    print(f"\n1 wiersz tekstu:\n   \"{first_line}\"")


if __name__ == "__main__":
    zad1()
    zad2()
    zad3()