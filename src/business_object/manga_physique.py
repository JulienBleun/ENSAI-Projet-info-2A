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
        id_manga_physique: int,
        titre_manga: str,
        tomes_acquis: list[int],
        statut: str,
        id_utilisateur: int):
        
        if not isinstance(id_manga_physique, int):
            raise TypeError("L'identifiant du manga physique doit être un entier.")
        if not isinstance(titre_manga, str):
            raise TypeError("Le titre du manga doit être une chaîne de caractères.")
        if not isinstance(tomes_acquis, list) or not all(isinstance(tome, int) for tome in tomes_acquis):
            raise TypeError("Les tomes acquis doivent être une liste d'entiers.")
        if not isinstance(statut, str):
            raise TypeError("Le statut doit être une chaîne de caractères.")
        if not isinstance(id_utilisateur, int):
            raise TypeError("L'identifiant de l'utilisateur doit être un entier.")

        self.id_manga_physique = id_manga_physique
        self.titre_manga = titre_manga
        self.tomes_acquis = tomes_acquis
        self.statut = statut
        self.id_utilisateur = id_utilisateur
