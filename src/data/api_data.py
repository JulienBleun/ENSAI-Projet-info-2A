import psycopg2
import requests

from src.utils.singleton import Singleton


def pop_manga_from_api(metaclass=Singleton)

    BASE_URL = "https://api.jikan.moe/v4/"
    SEARCH_ENDPOINT = "manga"

    # BDD
    conn = psycopg2.connect(database="id2424", user="postgres", password="root")
    cur = conn.cursor()

    # Création schéma + table
    cur.execute("CREATE SCHEMA IF NOT EXISTS tp;")
    cur.execute("CREATE TABLE tp.manga (id_manga PRIMARY KEY, titre VARCHAR(400), descript TEXT);")

    # Récupération des données
    for i in range (1, 10):
        resultat_requete = requests.get(BASE_URL + SEARCH_ENDPOINT, params={"page": i})
        if resultat_requete.status_code == 200:
            # Insertion données
            for res in resultat_requete.json()["data"]:
                cur.execute(
                    "INSERT INTO tp.manga(id_manga, titre, descript) VALUES (%s, %s, %s);",
                    (res['mal_id'], res['title'], res['synopsis'])
                )
        else:
            print("Erreur")


    conn.commit()
    cur.close()
    conn.close()
