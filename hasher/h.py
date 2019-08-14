import hashlib

hasher = hashlib.sha256()
with open('hasher/txt', 'rb') as f:
    b = f.read()
    hasher.update(b)

print(hasher.hexdigest())