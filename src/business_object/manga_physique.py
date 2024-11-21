class MangaPhysique():
    """
    Classe pour modéliser un manga physique.

    Parameters :
    ------------

    id_manga_physique : int
        Identifiant unique associé au manga physique.

    id_collection_physique : int
        Identifiant de la classe manga physique à laquelle le manga physique
        appartient.

    dernier_tome_acquis  : int
        Numéro du dernier tome acquis.

    tomes_manquant : list[int]
        Liste des numéros des tomes manquants par rapport au dernier tome
        acquis de la série.

    statut : str
        Indique le status de la série, c'est-à-dire si je continue d'acheter
        les tomes ou non.
    """
    def __init__(
        self,
        id_manga_physique,
        titre_manga: int,
        tomes_acquis: list[int],
        statut: str,
        id_utilisateur: int
                ):

        self.id_manga_physique = id_manga_physique
        self.titre_manga = titre_manga
        self.tomes_acquis = tomes_acquis
        self.statut = statut
        self.id_utilisateur = id_utilisateur
