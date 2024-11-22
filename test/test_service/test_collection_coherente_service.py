from unittest.mock import MagicMock
from src.service.collection_coherente_service import CollectionCoherenteService
from src.dao.collection_coherente_dao import CollectionCoherenteDAO
from src.business_object.collection_coherente import CollectionCoherente
from src.business_object.manga import Manga

# Création d'un exemple de contenu pour les collections cohérentes
manga1 = Manga(id_manga=1, titre="Manga A", auteur="Auteur A", descript="Description A")
manga2 = Manga(id_manga=2, titre="Manga B", auteur="Auteur B", descript="Description B")
contenu_exemple = [manga1, manga2]

# Création d'une instance de collection cohérente pour les tests
collection_exemple = CollectionCoherente(
    id_collection=100,
    id_utilisateur=1,
    titre="Collection Exemple",
    description="Description de la collection exemple",
    contenu=contenu_exemple
)

def test_creer_coherent_succes():
    """Test de la création réussie d'une collection cohérente."""

    # GIVEN
    CollectionCoherenteDAO().CreateCoherente = MagicMock(return_value=True)

    # WHEN
    nouvelle_collection = CollectionCoherenteService().creer_coherent(
        id_collection=100,
        id_utilisateur=1,
        titre="Collection Exemple",
        description="Description de la collection exemple",
        contenu=[Manga(id_manga=1, titre="Manga A", auteur="Auteur A", descript="Description A"),
        Manga(id_manga=2, titre="Manga B", auteur="Auteur B", descript="Description B")]
    )

    # THEN
    assert nouvelle_collection is not None
    assert nouvelle_collection.titre == "Collection Exemple"
    assert len(nouvelle_collection.contenu) == 2

def test_creer_coherent_echec():
    """Test de l'échec de la création d'une collection cohérente."""

    # GIVEN
    CollectionCoherenteDAO().CreateCoherente = MagicMock(return_value=False)

    # WHEN
    nouvelle_collection = CollectionCoherenteService().creer_coherent(
        id_collection=100,
        id_utilisateur=1,
        titre="Collection Exemple",
        description="Description de la collection exemple",
        contenu=contenu_exemple
    )

    # THEN
    assert nouvelle_collection is None

def test_mettre_a_jour_coherent_succes():
    """Test de la mise à jour réussie d'une collection cohérente."""

    # GIVEN
    CollectionCoherenteDAO().UpdateCoherent = MagicMock(return_value=True)

    # WHEN
    collection_modifiee = CollectionCoherenteService().mettre_a_jour_coherent(collection_exemple)

    # THEN
    assert collection_modifiee is not None
    assert collection_modifiee.titre == "Collection Exemple"

def test_mettre_a_jour_coherent_echec():
    """Test de l'échec de la mise à jour d'une collection cohérente."""

    # GIVEN
    CollectionCoherenteDAO().UpdateCoherent = MagicMock(return_value=False)

    # WHEN
    collection_modifiee = CollectionCoherenteService().mettre_a_jour_coherent(collection_exemple)

    # THEN
    assert collection_modifiee is None

def test_supprimer_coherent_succes():
    """Test de la suppression réussie d'une collection cohérente."""

    # GIVEN
    CollectionCoherenteDAO().DeleteCoherent = MagicMock(return_value=True)

    # WHEN
    resultat = CollectionCoherenteService().supprimer_coherent(100)

    # THEN
    assert resultat

def test_supprimer_coherent_echec():
    """Test de l'échec de la suppression d'une collection cohérente."""

    # GIVEN
    CollectionCoherenteDAO().DeleteCoherent = MagicMock(return_value=False)

    # WHEN
    resultat = CollectionCoherenteService().supprimer_coherent(100)

    # THEN
    assert not resultat

def test_consulter_coherent_existant():
    """Test de la consultation d'une collection cohérente existante."""

    # GIVEN
    CollectionCoherenteDAO().ReadCoherent = MagicMock(return_value=collection_exemple)

    # WHEN
    collection = CollectionCoherenteService().consulter_coherent(100)

    # THEN
    assert collection is not None
    assert collection.id_collection == 100
    assert collection.titre == "Collection Exemple"

def test_consulter_coherent_inexistant():
    """Test de la consultation d'une collection cohérente inexistante."""

    # GIVEN
    CollectionCoherenteDAO().ReadCoherent = MagicMock(return_value=None)

    # WHEN
    collection = CollectionCoherenteService().consulter_coherent(999)

    # THEN
    assert collection is None

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
