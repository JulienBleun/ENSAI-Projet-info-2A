class Avis():

    def __init__(self,
                 id_avis: int,
                 id_objet_avis: int,
                 contenu: str,
                 note: int):

        self.id_avis = id_avis
        self.id_objet_avis = id_objet_avis
        self.contenu = contenu
        self.note = note
