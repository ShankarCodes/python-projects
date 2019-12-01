import hashlib
def sha256(obj):
    return hashlib.sha256(obj).hexdigest()

