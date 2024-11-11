import requests
import time
from src.dao.db_connection import DBConnection
from src.utils.singleton import Singleton


class ResetDatabase(metaclass=Singleton):
    """
    Reinitialisation de la base de données
    """

    def lancer(self):
        print("Ré-initialisation de la base de données")

        try:
            with open("src/data/init_db.sql", encoding="utf-8") as init_db:
                init_db_as_string = init_db.read()
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(init_db_as_string)

        except Exception as e:
            print(f"Erreur lors de la réinitialisation de la base de données : {e}")
            raise

    def populer(self):
        print("Population de la base de données")

        try:
            with open("src/data/pop_db.sql", encoding="utf-8") as pop_db:
                pop_db_as_string = pop_db.read()

            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(pop_db_as_string)

        except Exception as e:
            print(f"Erreur lors de la population de la base de données : {e}")
            raise

    def pop_manga_from_api(self):

        BASE_URL = "https://api.jikan.moe/v4"
        SEARCH_ENDPOINT = "/manga"
        print("Récupération et insertion des données de mangas")

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    i = 1
                    can_continue = True
                    while (can_continue):
                        response = requests.get(BASE_URL + SEARCH_ENDPOINT, params={"page": i})
                        if response.status_code == 200:
                            mangas = response.json()["data"]
                            for manga in mangas:
                                cursor.execute("SELECT * from tp.manga wHERE id_manga = %s", (manga['mal_id'],))
                                if cursor.fetchone() is None:
                                    auteur = manga['authors'][0]['name'] if manga['authors'] else None
                                    cursor.execute(
                                        "INSERT INTO tp.manga (id_manga, titre, descript, auteur) VALUES (%s, %s, %s, %s);",
                                        (manga['mal_id'], manga['title'], manga['synopsis'], auteur)
                                    )
                            print(f'La page {i} a correctement été chargée')
                            i += 1
                            can_continue = response.json()["pagination"]["has_next_page"]
                            time.sleep(0.5)
                        else:
                            print(f"Erreur de requête pour la page {i}: {response.status_code}")
                            time.sleep(2)
                        connection.commit()

        except Exception as e:
            print(f"Erreur lors de la récupération des données de mangas : {e}")
            raise


if __name__ == "__main__":
    ResetDatabase().lancer()
