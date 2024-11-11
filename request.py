import requests
id_manga = input('valeur de id')
URL= f"https://api.jikan.moe/v4/manga/{id_manga}/full"

r = requests.get(URL)
donnees = r.json()
print(donnees ["data"]["authors"])

for i in range(len(donnees ["data"]["authors"])):
    print(donnees ["data"]["authors"][i]["name"])



def rechercher_manga_par_titre(titre):
        url = f"https://api.jikan.moe/v4/manga?q={titre}"
        response = requests.get(url)

        if response.status_code == 200:
            resultats = response.json()['data']
            print(resultats)
            if not resultats:
                print("Aucun manga trouvé.")
                return None  # Pas de mangas trouvés

     # Affichage des mangas trouvés
            for index, manga in enumerate(resultats):
                print(f"{index + 1}. Titre: {manga['title']}, ID: {manga['mal_id']}")

            return resultats  # Retourner les résultats pour un usage ultérieur
        else:
            print("Erreur lors de la recherche.")
            return None

a = rechercher_manga_par_titre("naruto")
print(a)
