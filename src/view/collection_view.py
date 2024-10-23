from dao.collection_physique_dao import CollectionPhysiqueDAO
from dao.collection_coherente_dao import Collection_coherenteDAO
from business_object.collection_physique import CollectionPhysique
from business_object.collection_coherente import CollectionCoherente




def creer_collection_coherente_view(utilisateur_id):
    titre = input("Titre de la collection cohérente : ")
    description = input("Description : ")
    CreateCoherente(utilisateur_id, titre, description)
    print("Collection cohérente créée avec succès.")

def creer_collection_physique_view(utilisateur_id):
    titre = input("Titre de la collection physique : ")
    dernier_tome_acquis = int(input("Dernier tome acquis : "))
    status = input("Statut de la série ('reading' ou 'dropped') : ")
    CreatePhysique(utilisateur_id, titre, dernier_tome_acquis, status)
    print("Collection physique créée avec succès.")

# Autres fonctions pour afficher, mettre à jour et supprimer des collections...

def afficher_mes_collections_view():
    print("Voici vos collections de mangas :")
    # Ajoute ici la logique pour récupérer et afficher les collections de l'utilisateur


def ajouter_a_collection_view(manga_id):
    titre = input("Entrez le titre de la collection : ")
    dernier_tome_acquis = int(input("Entrez le dernier tome acquis : "))
    status = input("Entrez le statut de la série ('reading' ou 'dropped') : ")
    
    # Appelle la fonction pour créer la collection physique
    creer_collection_physique(utilisateur_connecte['id'], titre, dernier_tome_acquis, status)
    print("Le manga a été ajouté à votre collection avec succès.")
