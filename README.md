# ENSAI-Projet-info-2A-Application de gestion de mangas

Cette application de gestion de mangas permet aux utilisateurs de créer, gérer et partager leurs collections de mangas à la fois virtuelle et physiques. Elle offre des fonctionnalités de recherche de mangas, de création et consultation d'avis et de créations de collections de mangas.

Exemple d'utilsation : 

1 Créer une collection cohérente : L'utilisateur peut créer une collection en luid donnant un titre et une description personnalisée et regroupant tous les titres de mangas souhaités.

2 Créer une collection physique : L'utilisateur peut créer une collection de mangas qu'il possède physiquement, en précisant le titre de chaque série, son statut actuel (terminée ou en cours), s'il continue d'acheter des tomes, ainsi que les tomes manquants dans la série.

3 Recherche de mangas : Il est possible de rechercher des informations détaillées sur un manga comme par exemple l'auteur sa description ou ses avis.

4 Gestion des avis : L'application permet aux utilisateurs de publier, mettre à jour, supprimer et consulter les avis sur des mangas ou des collections, y compris ceux partagés par d'autres utilisateurs.

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
git clone 

---

▶️ Installez les packages nécessaires
Dans VSCode :

 - Ouvrir un terminal Git Bash
 - Exécutez les commandes suivantes
   
```
pip install -r requirements.txt ```
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
  POSTGRES_SCHEMA=projet

  ```

---

▶️ Lancer le programme

Cette application propose une interface graphique très basique pour naviguer entre différents menus.

- Dans Git Bash : ```python src/__main__.py```
