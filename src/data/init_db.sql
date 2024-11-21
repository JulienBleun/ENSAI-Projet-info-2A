DROP SCHEMA IF EXISTS tp CASCADE;
CREATE SCHEMA tp;
--------------------------------------------------------------
-- Utilisateur
--------------------------------------------------------------

DROP TABLE IF EXISTS tp.utilisateur CASCADE;

CREATE TABLE tp.utilisateur (
    id_utilisateur SERIAL PRIMARY KEY,
    nom VARCHAR(100),
    prenom VARCHAR(100),
    pseudo VARCHAR(1000) UNIQUE,
    email VARCHAR(400),
    mdp VARCHAR(100), -- Mot de passe haché
    sel VARCHAR(64)   -- Sel en format hexadécimal
);


--------------------------------------------------------------
-- Collection
--------------------------------------------------------------

DROP TABLE IF EXISTS tp.collection CASCADE;

CREATE TABLE tp.collection (
    id_collection SERIAL PRIMARY KEY,
    id_utilisateur INT REFERENCES tp.utilisateur(id_utilisateur)
);

--------------------------------------------------------------
-- Manga
--------------------------------------------------------------

DROP TABLE IF EXISTS tp.manga CASCADE;
CREATE TABLE tp.manga (
    id_manga INTEGER PRIMARY KEY,
    titre VARCHAR(400) UNIQUE,
    descript TEXT,
    auteur VARCHAR(400)
);

--------------------------------------------------------------
-- Manga Physique
--------------------------------------------------------------

DROP TABLE IF EXISTS tp.manga_physique CASCADE;
CREATE TABLE tp.manga_physique (
    id_manga_physique SERIAL PRIMARY KEY,
    id_utilisateur INT REFERENCES tp.utilisateur(id_utilisateur),
    titre_manga VARCHAR(400),
    FOREIGN KEY (titre_manga) REFERENCES tp.manga(titre),
    tomes_acquis TEXT,
    statut VARCHAR(100)
);

--------------------------------------------------------------
-- Avis Collection
--------------------------------------------------------------

DROP TABLE IF EXISTS tp.avis_collection CASCADE;
CREATE TABLE tp.avis_collection (
    id_avis SERIAL PRIMARY KEY,
    id_collection INT REFERENCES tp.collection(id_collection),
    id_utilisateur INT REFERENCES tp.utilisateur(id_utilisateur),
    commentaire TEXT,
    note NUMERIC CHECK (note >= 0 AND note <= 10)
);

--------------------------------------------------------------
-- Collection Cohérente
--------------------------------------------------------------

DROP TABLE IF EXISTS tp.collection_coherente CASCADE;

CREATE TABLE tp.collection_coherente (
    id_collection INT PRIMARY KEY REFERENCES tp.collection(id_collection),
    titre VARCHAR(400),
    description TEXT
);

--------------------------------------------------------------
-- Association Manga Collection Cohérente
--------------------------------------------------------------

DROP TABLE IF EXISTS tp.association_manga_collection_coherente CASCADE;
CREATE TABLE tp.association_manga_collection_coherente (
    id_manga INT REFERENCES tp.manga(id_manga),
    id_collection INT REFERENCES tp.collection_coherente(id_collection),
    PRIMARY KEY (id_manga, id_collection)
);

--------------------------------------------------------------
-- Avis_manga
--------------------------------------------------------------

DROP TABLE IF EXISTS tp.avis_manga CASCADE;
CREATE TABLE tp.avis_manga (
    id_avis SERIAL PRIMARY KEY,
    id_manga INT REFERENCES tp.manga(id_manga),
    id_utilisateur INT REFERENCES tp.utilisateur(id_utilisateur),
    commentaire TEXT,
    note NUMERIC CHECK (note >= 0 AND note <= 10)
);

--------------------------------------------------------------
-- Collection physique
--------------------------------------------------------------

DROP TABLE IF EXISTS tp.collection_physique CASCADE;

CREATE TABLE tp.collection_physique(
    id_collection_physique SERIAL PRIMARY KEY,
    id_utilisateur INT REFERENCES tp.utilisateur(id_utilisateur)
);
