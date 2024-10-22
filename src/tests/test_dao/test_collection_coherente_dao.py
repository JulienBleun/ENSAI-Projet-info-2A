import os #utilisé pour manipuler les vaiables d'environnment avec patch.dict()
import pytest

from unittest.mock import patch # patch est utilisé pour remplacer des objets ou méthodes pendant les tests

from utils.reset_database import ResetDatabase
from utils.securite import hash_password

