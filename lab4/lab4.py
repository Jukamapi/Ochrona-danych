import hashlib
import hmac
from pathlib import Path
import secrets

#zad1
def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def zad1(base_dir: Path):
    sums_path = base_dir / "SHA256SUMS.txt"

    if sums_path.exists():
        with open(sums_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue

                #64 hex + ścieżka
                parts = line.split("  ", 1)
                if len(parts) != 2:
                    continue

                expected_hash, rel_path = parts[0].strip(), parts[1].strip()
                target_file = base_dir / rel_path

                if not target_file.is_file():
                    status = "BRAK"
                else:
                    calculated_hash = sha256_file(target_file)
                    status = (
                        "OK"
                        if hmac.compare_digest(
                            calculated_hash.lower(), expected_hash.lower()
                        )
                        else "BŁĄD"
                    )

                print(f"{rel_path}: {status}")
    else:
        print(f"plik {sums_path} nie istnieje.")

    t1 = b"Ala ma kota."
    t2 = b"Ola ma kota."
    h1 = hashlib.sha256(t1).digest()
    h2 = hashlib.sha256(t2).digest()

    diff_bits = sum(bin(b1 ^ b2).count("1") for b1, b2 in zip(h1, h2))
    print(f"\nSHA256('Ala ma kota.'): {h1.hex()}")
    print(f"SHA256('Ola ma kota.'): {h2.hex()}")
    print(f"N różniących się bitów: {diff_bits}\n\n\n")

#zad2
class PasswordManager:
    #login:iteracje:sól_hex:skrót_hex
    def __init__(self):
        self.db = {}

    def load_db(self, path: Path):
        if not path.exists():
            return

        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                login, iterations, salt_hex, hash_hex = line.split(":")
                self.db[login] = (
                    int(iterations),
                    bytes.fromhex(salt_hex),
                    bytes.fromhex(hash_hex),
                )

    def weryfikuj(self, login: str, haslo: str) -> bool:
        if login not in self.db:
            return False

        iterations, salt, expected_hash = self.db[login]

        calc_hash = hashlib.pbkdf2_hmac(
            hash_name="sha256",
            password=haslo.encode("utf-8"),
            salt=salt,
            iterations=iterations,
            dklen=32,
        )
        return hmac.compare_digest(calc_hash, expected_hash)

    def dodaj(self, login: str, haslo: str, iterations: int = 600000) -> str:
        salt = secrets.token_bytes(16)
        calc_hash = hashlib.pbkdf2_hmac(
            hash_name="sha256",
            password=haslo.encode("utf-8"),
            salt=salt,
            iterations=iterations,
            dklen=32,
        )
        self.db[login] = (iterations, salt, calc_hash)
        record = f"{login}:{iterations}:{salt.hex()}:{calc_hash.hex()}"
        return record


def zad2(base_dir: Path):
    pm = PasswordManager()
    hasla_path = base_dir / "hasla.txt"
    pm.load_db(hasla_path)

    test_cases = [
        ("anna", "Kasztan-2026"),
        ("anna", "kasztan-2026"),
        ("piotr", "Żółw na łące"),
        ("kasia", "Kasztan-2026"),
    ]
    for login, pswd in test_cases:
        res = pm.weryfikuj(login, pswd)
        print(f"weryfikacja: {login}, '{pswd}' -> {res}")

    haslo_wspolne = "WspolneHaslo123!"
    rec1 = pm.dodaj("test1", haslo_wspolne)
    rec2 = pm.dodaj("test2", haslo_wspolne)

    _, salt1, hash1 = pm.db["test1"]
    _, salt2, hash2 = pm.db["test2"]

    print(f"\nsól test1 == sól test2: {salt1 == salt2}")
    print(f"skrót test1 == skrót test2: {hash1 == hash2}")
    print(f"weryfikacja test1: {pm.weryfikuj('test1', haslo_wspolne)}")
    print(f"weryfikacja test2: {pm.weryfikuj('test2', haslo_wspolne)}")

#zad3
def h24(data: bytes) -> str:
    return hashlib.sha256(data).digest()[:3].hex()


def generate_variant(lines: list[bytes], v: int) -> bytes:
    out = []
    for i, line in enumerate(lines):
        content = line[:-1] if line.endswith(b"\n") else line
        if (v >> i) & 1:
            out.append(content + b" \n")
        else:
            out.append(content + b"\n")
    return b"".join(out)


def zad3(base_dir: Path):
    print("\n\n\n")
    orig_path = base_dir / "oryginal.txt"
    mod_path = base_dir / "zmieniony.txt"

    if not orig_path.exists() or not mod_path.exists():
        print("brak pliku oryginal.txt lub zmieniony.txt!")
        return

    with open(orig_path, "rb") as f:
        orig_lines = f.readlines()
    with open(mod_path, "rb") as f:
        mod_lines = f.readlines()

    #punkt1
    orig_hashes = {}
    for v in range(8192):
        data = generate_variant(orig_lines, v)
        h = h24(data)
        if h not in orig_hashes:
            orig_hashes[h] = v

    #punkt2 i punkkt3
    h24_orig_0 = h24(generate_variant(orig_lines, 0))

    found_pair = None
    count_equal_to_orig_0 = 0

    for v_mod in range(8192):
        mod_data = generate_variant(mod_lines, v_mod)
        h_mod = h24(mod_data)

        #punkt2
        if found_pair is None and h_mod in orig_hashes:
            found_pair = (orig_hashes[h_mod], v_mod, h_mod)

        #punkt3
        if h_mod == h24_orig_0:
            count_equal_to_orig_0 += 1

    if found_pair:
        v_orig, v_mod, hash_val = found_pair
        print(
            f"para kolizyjna: v_oryginał = {v_orig}, v_zmieniony = {v_mod}, h24 = {hash_val}"
        )
    else:
        print("brak pary kolizyjnej.")

    print(
        f"liczba wariantów zmienionego o h24 równym h24(oryginał_wariant_0): {count_equal_to_orig_0}"
    )



if __name__ == "__main__":
    base_dir = Path(__file__).parent
    zad1(base_dir)
    zad2(base_dir)
    zad3(base_dir)