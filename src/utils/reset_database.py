from src.utils.singleton import Singleton
from src.dao.db_connection import DBConnection


class ResetDatabase(metaclass=Singleton):
    """
    Reinitialisation de la base de données
    """

    def lancer(self):
        print("Ré-initialisation de la base de données")

        try:
            with open("data/init_db.sql", encoding="utf-8") as init_db:
                init_db_as_string = init_db.read()
            with open("data/pop_db.sql", encoding="utf-8") as pop_db:
                pop_db_as_string = pop_db.read()

            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(init_db_as_string)
                    cursor.execute(pop_db_as_string)

        except Exception as e:
            print(f"Erreur lors de la réinitialisation de la base de données : {e}")
            raise


if __name__ == "__main__":
    ResetDatabase().lancer()
