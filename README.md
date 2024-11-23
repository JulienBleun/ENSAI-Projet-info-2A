# ENSAI-Projet-info-2A-Application de gestion de mangas

This manga management application allows users to create, manage and share their collections of consistent, physical manga. It offers functions for searching for manga, creating and consulting reviews and creating manga collections.

Example of use :

1 Creating a coherent collection : Users can create a collection by giving it a title and a personalised description and grouping together all the manga titles they want.

2 Create a physical collection: Users can create a collection of manga that they physically own, by adding the manga that they physically own, specifying their current status (in particular whether they are still reading the series) and the volumes that they own.

3 Manga search: You can search for detailed information about a manga, such as the author, a description or reviews given by users of the application.

4 Reviews management: The application allows users to publish, update, delete and view reviews of manga or collections, including those shared by other users.

This application allows you to organise the manga you own, whether you're a collector or an occasional reader. Exchanging opinions on manga or collections makes it easier to make recommendations and discover new reading material.

▶️ Software required

- Visual Studio Code
- Python 3.10
- Git
- PostgreSQL database

---

▶️ Clone the repository
- Open Git Bash
- Create a folder P:/Cours2A/UE3-Projet-info and position yourself in it
- ```mkdir -p /p/Cours2A/UE3-Projet-info && cd $_ ```
- Clone this repository
git clone https://github.com/JulienBleun/ENSAI-Projet-info-2A.git

---

▶️ Open the repository with VSCode
- Open Visual Studio Code
- File > Ope Folder
- Click once on Cours2A-UE3-Projet-info and click on Select a folder
⚠️ If the parent folder in the VSCode explorer (on the left) is not Cours2A-UE3-Projet-info, the application will not work.

Ce dépôt contient de nombreux fichiers de configuration pour paramétrer les différents outils utilisés.

| File                  | Description                                         |
|--------------------------|-----------------------------------------------------|
| `.env`                   | Defining environment variables              |
| `.gitignore`             | List of files and directories to ignore during Git operations |
| `requirements.txt`       | List of Python dependencies required for the project |


---


▶️ Install the necessary packages
In VSCode :

 - Open a Git Bash terminal
 - Run the following commands

```
pip install -r requirements.txt
pip list
```

---

▶️ Environment variables

To connect the Python application to the required database and webservice, you need to define environment variables.
Instructions:
  1. At the root of the project, create a file named .env.
  2. Add and complete the following elements in this file :

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
▶️ Run unit tests

Classes tested

The tests are mainly carried out on services and business objects.
To run the unit tests, use the following command in Git Bash: pytest -v
- or python -m pytest -v if pytest has not been added to the PATH

---

▶️ Launch the program

This application provides a basic interface, using the terminal to navigate between different menus.
Steps to launch the program :

   1. In Git Bash, run the file `run_api.py` to update the database :
   In git Bash : ``` python src/run_api.py ```

   2. Then, still in Git Bash, launch the main application with the command : ```python src/__main__.py```
    
