import unittest
from src.business_object.utilisateur import utilisateur

class TestUtilisateur(unittest.TestCase):

    def test_creation_utilisateur(self):
        # GIVEN
        expected_id = 1
        expected_prenom = "John"
        expected_nom_utilisateur = "john_doe"
        expected_email = "john.doe@example.com"
        expected_mot_de_passe = "password123"

        # WHEN
        user = utilisateur(
            id=expected_id,
            prenom=expected_prenom,
            nom_utilisateur=expected_nom_utilisateur,
            email=expected_email,
            mot_de_passe=expected_mot_de_passe
        )

        # THEN
        self.assertEqual(user.id, expected_id)
        self.assertEqual(user.nom_utisateur, expected_nom_utilisateur)
        self.assertEqual(user.email, expected_email)
        self.assertEqual(user.mot_de_passe, expected_mot_de_passe)
