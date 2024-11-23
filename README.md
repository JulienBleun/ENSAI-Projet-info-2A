# ENSAI-Projet-info-2A-Application de gestion de mangas

Cette application de gestion de mangas permet aux utilisateurs de créer, gérer et partager leurs collections de mangas cohérentes et physiques. Elle offre des fonctionnalités de recherche de mangas, de création et consultation d'avis et de créations de collections de mangas.

Exemple d'utilsation :

1 Créer une collection cohérente : L'utilisateur peut créer une collection en lui donnant un titre et une description personnalisée et regroupant tous les titres de mangas souhaités.

2 Créer une collection physique : L'utilisateur peut créer une collection de mangas qu'il possède physiquement, en ajoutant les mangas quu'il détient physiquement, il peut préciserson statut actuel (notamment s'il lit toujours la série), ainsi que les tomes qu'il possède.

3 Recherche de mangas : Il est possible d'obtenir des informations détaillées sur un manga comme par exemple l'auteur, sa description ou ses avis donnés par les utilisateurs de l'application.

4 Gestion des avis : L'application permet aux utilisateurs de publier, mettre à jour, supprimer et consulter les avis sur des mangas ou des collections, y compris ceux partagés par d'autres utilisateurs.

Cette application permet donc d'avoir une organisation des mangas que l'on possède, que l'on soit collectionneur ou lecteur occasionnel. L'échange d'avis sur les mangas ou collections facilite les recommendations et la découverte de nouvelles lectures.

▶️ Logiciels requis

- Visual Studio Code
- Python 3.10
- Git
- Une base de données PostgreSQL

---

▶️ Clonez le dépôt
- Ouvrir Git Bash
- Créez un dossier P:/Cours2A/UE3-Projet-info et positionnez-vous dedans
mkdir -p /p/Cours2A/UE3-Projet-info && cd $_
- Clonez ce dépôt
git clone https://github.com/JulienBleun/ENSAI-Projet-info-2A.git

---

▶️ Ouvrez le dépôt avec VSCode
- Ouvrir Visual Studio Code
- File > Ope Folder
- Cliquer une seule fois sur Cours2A-UE3-Projet-info et cliquez sur Sélectionner un dossier
⚠️ Si le dossier parent dans l'explorer VSCode (à gauche) n'est pas Cours2A-UE3-Projet-info, l'application ne fonctionnera pas

Fichiers de configuration

Ce dépôt contient de nombreux fichiers de configuration pour paramétrer les différents outils utilisés.

| Fichier                  | Description                                         |
|--------------------------|-----------------------------------------------------|
| `.env`                   | Définir les variables d'environnement               |
| `.gitignore`             | Liste des fichiers et répertoires à ignorer lors des opérations Git |
| `requirements.txt`       | Liste des dépendances Python requises pour le projet |


---


▶️ Installez les packages nécessaires
Dans VSCode :

 - Ouvrir un terminal Git Bash
 - Exécutez les commandes suivantes

```
pip install -r requirements.txt
pip list
```

---

▶️ Variables d'environnement

Pour connecter l'application Python à la base de données et au webservice requis, vous devez définir des variables d'environnement.
Instructions :
  1. À la racine du projet, créez un fichier nommé .env.
  2. Ajoutez et complétez les éléments suivants dans ce fichier :

  ```
  WEBSERVICE_HOST=

  POSTGRES_HOST=sgbd-eleves.domensai.ecole
  POSTGRES_PORT=5432
  POSTGRES_DATABASE=idxxxx
  POSTGRES_USER=idxxxx
  POSTGRES_PASSWORD=idxxxx
  POSTGRES_SCHEMA=tp

  ```

---
▶️ Lancer les tests unitaires

Classes testées

Les tests sont principalement effectués sur les services et les objets métiers
Pour exécuter les tests unitaires, utilisez la commande suivante dans Git Bash : pytest -v
- ou python -m pytest -v si pytest n'a pas été ajouté au PATH

---

▶️ Lancer le programme

Cette application propose une interface basique à l'aide du terminal pour naviguer entre différents menus.
Étapes pour lancer le programme :

1. **Initialisation de la base de données** :  
   Dans Git Bash, exécutez le fichier `run_api.py` pour mettre à jour la base de données :
   Dans git Bash : ``` python src/run_api.py ```

   Puis toujours dans Git Bash, lancez l'application principale avec la commande : ```python src/__main__.py```
    
