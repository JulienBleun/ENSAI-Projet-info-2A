from src.utils.reset_database import ResetDatabase

if __name__ == "__main__":
    ResetDatabase().lancer()
    ResetDatabase().pop_manga_from_api()
