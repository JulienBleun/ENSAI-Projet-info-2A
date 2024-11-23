import unittest
from src.business_object.utilisateur import Utilisateur


class TestUtilisateur(unittest.TestCase):

    def test_creation_utilisateur(self):
        # GIVEN
        expected_id_utilisateur = 1
        expected_prenom = "John"
        expected_nom = "Doe"
        expected_pseudo = "john_doe"
        expected_email = "john.doe@example.com"
        expected_mdp = "password123"
        
        # WHEN
        user = Utilisateur(
            id_utilisateur=expected_id_utilisateur,
            prenom=expected_prenom,
            nom = expected_nom,
            pseudo=expected_pseudo,
            email=expected_email,
            mdp=expected_mdp,
            
        )

        # THEN
        self.assertEqual(user.id_utilisateur, expected_id_utilisateur)
        self.assertEqual(user.prenom, expected_prenom)  
        self.assertEqual(user.nom, expected_nom)
        self.assertEqual(user.pseudo, expected_pseudo)
        self.assertEqual(user.email, expected_email)
        self.assertEqual(user.mdp, expected_mdp)
        
if __name__ == '__main__':
    unittest.main()
