class MangaPhysique():

    def __init__(
                self,
                id_manga_physique : int,
                id_manga : int,
                id_collection_physique : int,
                dernier_tome_acquis : int,
                tomes_manquant : list[int],
                statut : str
                ) :

        self.id_manga_physique = id_manga_physique
        self.id_manga = id_manga
        self.id_collection_physique = id_collection_physique
        self.dernier_tome_acquis = dernier_tome_acquis
        self.tomes_manquant = tomes_manquant
        self.statut = statut
