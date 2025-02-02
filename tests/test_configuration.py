import unittest
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from config import Config


class TestDatabaseConnection(unittest.TestCase):

    def test_database_connection(self):
        # Get the database URI from the config
        database_uri = Config.SQLALCHEMY_DATABASE_URI

        try:
            # Create an engine to connect to the PostgreSQL database
            engine = create_engine(database_uri)
            # Attempt to connect to the database
            connection = engine.connect()
            connection.close()
            print("Database connection successful!")
            self.assertTrue(True)  # Connection successful, test passes
        except OperationalError as e:
            print(f"Error: {e}")
            print("Database connection failed.")
            self.assertTrue(False)  # Connection failed, test fails


if __name__ == "__main__":
    unittest.main()
