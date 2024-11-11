from unittest.mock import MagicMock

from src.service.collection_physique_service import CollectionPhysiqueService
from src.dao.collection_physique_dao import CollectionPhysiqueDAO
from src.business_object.collection_physique import CollectionPhysique
from src.business_object.manga_physique import MangaPhysique


def test_creer_physique_ok():
    """Création de CollectionPhysique réussie avec MangaPhysique"""

    # GIVEN
    id_utilisateur, id_collection = 1, 101
    titre, description = "Ma collection", "Description de ma collection"
    contenu = [
        MangaPhysique(id_manga_physique=1, id_manga=100, id_collection_physique=101,
                      dernier_tome_acquis=12, tomes_manquant=[1, 3], statut="En cours"),
        MangaPhysique(id_manga_physique=2, id_manga=101, id_collection_physique=101,
                      dernier_tome_acquis=20, tomes_manquant=[], statut="Complétée")
    ]
    CollectionPhysiqueDAO().CreatePhysique = MagicMock(return_value=True)

    # WHEN
    service = CollectionPhysiqueService()
    collection = service.creer_physique(id_utilisateur, id_collection, titre, description, contenu)

    # THEN
    assert collection is not None
    assert collection.id_collection == id_collection
    assert collection.titre == titre
    assert len(collection.contenu) == 2
    assert collection.contenu[0].dernier_tome_acquis == 12


def test_creer_physique_echec():
    """Création de CollectionPhysique échouée"""

    # GIVEN
    id_utilisateur, id_collection = 1, 102
    titre, description = "Collection échouée", "Une description échouée"
    contenu = [
        MangaPhysique(id_manga_physique=3, id_manga=102, id_collection_physique=102,
                      dernier_tome_acquis=5, tomes_manquant=[2, 4], statut="En attente")
    ]
    CollectionPhysiqueDAO().CreatePhysique = MagicMock(return_value=False)

    # WHEN
    service = CollectionPhysiqueService()
    collection = service.creer_physique(id_utilisateur, id_collection, titre, description, contenu)

    # THEN
    assert collection is None


def test_mettre_a_jour_physique_ok():
    """Mise à jour d'une CollectionPhysique réussie"""

    # GIVEN
    collection_modifiée = CollectionPhysique(
        id_utilisateur=2, id_collection=103, titre="Collection mise à jour",
        description="Nouvelle description", contenu=[
            MangaPhysique(id_manga_physique=4, id_manga=103, id_collection_physique=103,
                          dernier_tome_acquis=10, tomes_manquant=[6, 7], statut="Abandonnée")
        ]
    )
    CollectionPhysiqueDAO().UpdatePhysique = MagicMock(return_value=True)

    # WHEN
    service = CollectionPhysiqueService()
    result = service.mettre_a_jour_physique(collection_modifiée)

    # THEN
    assert result is not None
    assert result.titre == "Collection mise à jour"
    assert result.contenu[0].statut == "Abandonnée"

def test_mettre_a_jour_physique_echec():
    """Test de l'échec de la mise à jour d'une CollectionPhysique."""

    # GIVEN
    collection_modifiee = CollectionPhysique(
        1, 100, "Titre mis à jour", "Description mise à jour", contenu=[
            MangaPhysique(id_manga_physique=4, id_manga=103, id_collection_physique=103,
                          dernier_tome_acquis=10, tomes_manquant=[6, 7], statut="Abandonnée")
        ]
    )
    CollectionPhysiqueDAO().UpdatePhysique = MagicMock(return_value=False)

    # WHEN
    service = CollectionPhysiqueService()
    resultat = service.mettre_a_jour_physique(collection_modifiee)

    # THEN
    assert resultat is None
    
def test_supprimer_physique_ok():
    """Suppression d'une CollectionPhysique réussie"""

    # GIVEN
    collection = CollectionPhysique(
        id_utilisateur=3, id_collection=104, titre="Collection à supprimer",
        description="Description à supprimer", contenu=[]
    )
    CollectionPhysiqueDAO().DeletePhysique = MagicMock(return_value=True)

    # WHEN
    service = CollectionPhysiqueService()
    result = service.supprimer_physique(collection)

    # THEN
    assert result is True

def test_supprimer_physique_echec():
    """Test de l'échec de la suppression d'une CollectionPhysique."""

    # GIVEN
    collection_a_supprimer = CollectionPhysique(
        1, 100, "Collection à supprimer", "Description à supprimer", contenu=[]
    )
    CollectionPhysiqueDAO().DeletePhysique = MagicMock(return_value=False)

    # WHEN
    service = CollectionPhysiqueService()
    resultat = service.supprimer_physique(collection_a_supprimer)

    # THEN
    assert resultat is False
    
def test_consulter_physique_ok():
    """Consultation d'une CollectionPhysique réussie"""

    # GIVEN
    id_collection = 105
    collection_attendue = CollectionPhysique(
        id_utilisateur=4, id_collection=id_collection, titre="Consultation réussie",
        description="Une consultation", contenu=[
            MangaPhysique(id_manga_physique=5, id_manga=104, id_collection_physique=105,
                          dernier_tome_acquis=15, tomes_manquant=[2, 8], statut="Active")
        ]
    )
    CollectionPhysiqueDAO().ReadPhysique = MagicMock(return_value=collection_attendue)

    # WHEN
    service = CollectionPhysiqueService()
    result = service.consulter_physique(id_collection)
  
    # THEN
    assert result is not None
    assert result.id_collection == id_collection
    assert result.contenu[0].dernier_tome_acquis == 15

def test_consulter_physique_echec():
    """Test de l'échec de la consultation d'une CollectionPhysique."""

    # GIVEN
    id_collection = 100
    CollectionPhysiqueDAO().ReadPhysique = MagicMock(return_value=None)

    # WHEN
    service = CollectionPhysiqueService()
    resultat = service.consulter_physique(id_collection)

    # THEN
    assert resultat is None

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])

