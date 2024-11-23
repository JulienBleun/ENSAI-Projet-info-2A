from hashlib import sha512
import os

# Fonction pour générer un sel aléatoire
def generer_sel():
    return os.urandom(16)  # Sel de 16 octets

# Fonction pour hasher un mot de passe avec un sel
def hasher_mot_de_passe(mot_de_passe):
    mot_de_passe_bytes = mot_de_passe.encode()
    hash_obj = sha512(mot_de_passe_bytes)  # Combine sel avec mot de passe
    mot_de_passe_hashe = hash_obj.hexdigest()
    return mot_de_passe_hashe  # Renvoie haché et sel

# Fonction pour vérifier un mot de passe en comparant avec mot de passe haché et sel
def verifier_mot_de_passe(mot_de_passe, mot_de_passe_hashe, sel):
    mot_de_passe_bytes = mot_de_passe.encode('utf-8')
    hash_obj = hashlib.sha256(sel + mot_de_passe_bytes)  # Assurez-vous que l'ordre est le même
    return hash_obj.hexdigest() == mot_de_passe_hashe
