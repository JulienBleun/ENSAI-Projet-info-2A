import os

import dotenv
import psycopg2
from psycopg2.extras import RealDictCursor
from src.utils.singleton import Singleton


class DBConnection(metaclass=Singleton):
    """
    Classe technique pour ouvrir une seule connexion à la BDD.
    """

    def __init__(self):
        dotenv.load_dotenv(override=True)
        # Open the connection.
        self.__connection = psycopg2.connect(
            host=os.environ["HOST"],
            port=os.environ["PORT"],
            database=os.environ["DATABASE"],
            user=os.environ["USER"],
            password=os.environ["PASSWORD"],
            cursor_factory=RealDictCursor,
        )

    @property
    def connection(self):
        """
        return the opened connection.

        :return: the opened connection.
        """
        return self.__connection
