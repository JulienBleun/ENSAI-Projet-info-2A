### TODO rien normalement c'est bon insh
import logging

from src.utils.singleton import Singleton
from src.utils.log_decorator import log

from src.dao.db_connection import DBConnection

from src.business_object.avis_manga import AvisManga
from src.business_object.abstract_avis import AbstractAvis




class AvisMangaDao(metaclass=Singleton):
    """Classe contenant les méthodes pour accéder aux avis des mangas de la """
    """base de données"""

    #log
    def create_avis_manga(self, avis: AvisManga) -> bool:
        """Création d'un avis sur un manga dans la base de données

        Parameters
        ----------
        avis : AvisManga

        Returns
        -------
        created : bool
            True si la création est un succès
            False sinon
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO tp.avis_manga (id_manga, id_utilisateur, commentaire, note)"
                        "VALUES (%(id_manga)s, %(id_utilisateur)s, %(commentaire)s, %(note)s)                         "
                        "  RETURNING id_avis;                          ",
                        {
                            "id_manga": avis.id_manga,
                            "id_utilisateur": avis.id_utilisateur,
                            "commentaire": avis.commentaire,
                            "note": avis.note,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise

        created = False
        if res:
            avis.id_avis = res["id_avis"]
            created = True

        return created
