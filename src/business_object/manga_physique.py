class MangaPhysique():
    """
    Classe pour modéliser un manga physique. Un manga physique est un manga
    possédé dans la vraie vie par un utilisateur, avec un certain nombre de
    tomes acquis par ce dernier. Pour cela chaque manga physique possède un
    attribut 'id_utilisateur'. On rajoute également l'attribut 'statut' qui
    donne plus d'informations sur le manga physique en question.

    Parameters :
    ------------

    id_manga_physique : int
        Identifiant unique associé au manga physique.

    titre_manga : str
        Titre du manga associé au manga physique.

    dernier_tome_acquis  : int
        Numéro du dernier tome acquis.

    tomes_acquis : list[int]
        Liste des numéros des tomes acquis par l'utilisateur.

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

        if not isinstance(titre_manga, str):
            raise TypeError("Le titre du manga doit être une chaîne de caractères.")
        if not isinstance(tomes_acquis, list):
            raise TypeError("Les tomes acquis doivent être une liste.")
        if not isinstance(statut, str):
            raise TypeError("Le statut doit être une chaîne de caractères.")

        self.id_manga_physique = id_manga_physique
        self.titre_manga = titre_manga
        self.tomes_acquis = tomes_acquis
        self.statut = statut
        self.id_utilisateur = id_utilisateur
