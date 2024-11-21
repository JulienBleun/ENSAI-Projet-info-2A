import unittest
from src.business_object.utilisateur import Utilisateur


class TestUtilisateur(unittest.TestCase):

    def test_creation_utilisateur(self):
        # GIVEN
        expected_id = 1
        expected_prenom = "John"
        expected_nom = "Doe"
        expected_pseudo = "john_doe"
        expected_email = "john.doe@example.com"
        expected_mot_de_passe = "password123"

        # WHEN
        user = utilisateur(
            id=expected_id,
            prenom=expected_prenom,
            nom = expected_nom,
            pseudo=expected_pseudo,
            email=expected_email,
            mot_de_passe=expected_mot_de_passe
        )

        # THEN
        self.assertEqual(user.id, expected_id)
        self.assertEqual(user.prenom, expected_prenom)  
        self.assertEqual(user.nom, expected_nom)
        self.assertEqual(user.pseudo, expected_pseudo)
        self.assertEqual(user.email, expected_email)
        self.assertEqual(user.mot_de_passe, expected_mot_de_passe)
