INSERT INTO tp.utilisateur (nom, prenom, pseudo, email, mdp) VALUES ('Robert', 'Michel', 'JeanMicheMuche', 'Michel.Robert@gmail.com', 'robertro');
INSERT INTO tp.utilisateur (nom, prenom, pseudo, email, mdp) VALUES ('Dupont', 'Michel', 'DUponManga', 'Michel.Robert@gmail.com', 'robertro');
INSERT INTO tp.utilisateur (nom, prenom, pseudo, email, mdp) VALUES ('RAIZJj', 'Michel', 'Mangareader', 'Michel.Robert@gmail.com', 'robertro');


INSERT INTO tp.collection (id_utilisateur) VALUES ('2');
INSERT INTO tp.collection (id_utilisateur) VALUES ('3');

INSERT INTO tp.manga (id_manga, titre, descript) VALUES ('123', 'Naruto', 'Un ninja qui voulait devenir Hokage à la place de Hokage');
INSERT INTO tp.manga (id_manga, titre, descript) VALUES ('1', 'One Piece', 'Un gamin sur leau avec un chapeau');


INSERT INTO tp.avis_collection (id_collection, id_utilisateur, commentaire, note) VALUES ('1', '2', 'Meilleure collection de toute ma vie !', '10');
INSERT INTO tp.avis_collection (id_collection, id_utilisateur, commentaire, note) VALUES ('2', '3', 'Shitty collection you donkey', '0');


INSERT INTO tp.avis_manga (id_manga, id_utilisateur, commentaire, note) VALUES ('123', '2', 'Un peu trop de fillers à mon goût', '0');
INSERT INTO tp.avis_manga (id_manga, id_utilisateur, commentaire, note) VALUES ('1', '3', 'SAGASHI MONO SASAGHI NI YUKU NO SAAAAA', '10');
