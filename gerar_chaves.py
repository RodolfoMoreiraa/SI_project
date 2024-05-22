from Crypto.PublicKey import RSA

# Gerar o par de chaves
key = RSA.generate(2048)

# Exportar a chave privada em formato PEM
private_key = key.export_key()
with open("private-key-file.pem", "wb") as f:
    f.write(private_key)

# Exportar a chave pública em formato PEM
public_key = key.publickey().export_key()
with open("public-key-file.pem", "wb") as f:
    f.write(public_key)

print("Chaves geradas e guardadas como 'private-key-file.pem' e 'public-key-file.pem'")
