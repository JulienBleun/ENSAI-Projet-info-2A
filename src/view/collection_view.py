from src.dao.collection_coherente_dao import Collection_coherenteDAO
from src.dao.collection_physique_dao import CollectionPhysiqueDAO

def creer_collection_coherente_view(utilisateur_id):
    titre = input("Titre de la collection cohérente : ")
    description = input("Description : ")
    if Collection_coherenteDAO().CreateCoherente(titre, description, utilisateur_id):
        print("Collection cohérente créée avec succès.")
    else:
        print("Erreur lors de la création de la collection.")

def creer_collection_physique_view(utilisateur_id):
    titre = input("Titre de la collection physique : ")
    dernier_tome_acquis = int(input("Dernier tome acquis : "))
    status = input("Statut de la série ('reading' ou 'dropped') : ")
    
    if CollectionPhysiqueDAO().CreatePhysique(titre, dernier_tome_acquis, status, utilisateur_id):
        print("Collection physique créée avec succès.")
    else:
        print("Erreur lors de la création de la collection.")
