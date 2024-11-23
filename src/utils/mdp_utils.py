from hashlib import sha512


def hasher_mot_de_passe(mot_de_passe):
    mot_de_passe_bytes = mot_de_passe.encode()
    hash_obj = sha512(mot_de_passe_bytes)
    mot_de_passe_hashe = hash_obj.hexdigest()
    return mot_de_passe_hashe
