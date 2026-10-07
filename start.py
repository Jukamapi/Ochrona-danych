from hashlib import sha256

texts = ["Ala ma kota.", "Ala ma kota!"]

for text in texts:
    hashed = sha256(text.encode("utf-8")).hexdigest()
    print(text)
    print(hashed)