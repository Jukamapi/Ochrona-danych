import sys

def vigenere_encrypt(data: bytes, key: bytes) -> bytes:
    m = len(key)
    return bytes((data[i] + key[i % m]) % 256 for i in range(len(data)))

def vigenere_decrypt(data: bytes, key: bytes) -> bytes:
    m = len(key)
    return bytes((data[i] - key[i % m]) % 256 for i in range(len(data)))

def format_chunks(hex_str: str) -> str:
    chunk_len = 5 * 2
    return " ".join(hex_str[i : i + chunk_len] for i in range(0, len(hex_str), chunk_len))

def main():
    if len(sys.argv) < 2:
        sys.exit(1)

    with open(sys.argv[1], "rb") as f:
        plaintext = f.read()

    key_zamek = b"ZAMEK"
    ciphertext = vigenere_encrypt(plaintext, key_zamek)
    with open("vigenere.bin", "wb") as f:
        f.write(ciphertext)

    decrypted = vigenere_decrypt(ciphertext, key_zamek)
    assert decrypted == plaintext

    brama_text = b"BRAMABRAMABRAMA"
    c_szyfr = vigenere_encrypt(brama_text, b"SZYFR")
    c_kod = vigenere_encrypt(brama_text, b"KOD")

    print("\nKryptogramy tekstu 'BRAMABRAMABRAMA':")
    print(f"klucz SZYFR: {format_chunks(c_szyfr.hex())}")
    print(f"klucz KOD: {format_chunks(c_kod.hex())}")

if __name__ == "__main__":
    main()