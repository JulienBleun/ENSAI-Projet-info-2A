from src.utils.reset_database import ResetDatabase

if __name__ == "__main__":
    ResetDatabase().lancer()    # Initialise la base de données
    ResetDatabase().pop_manga_from_api()    # Remplit la table manga
# Rentrer Ctrl+C dans le terminal pour stopper l'insertion de mangas
