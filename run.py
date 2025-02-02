import unittest
from dotenv import load_dotenv
from flask import Flask, jsonify
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from config import Config  # Adjust this to your actual config module

# Load environment variables from the .env file
load_dotenv()

def create_app():
    """Create and configure the Flask app."""
    app = Flask(__name__)
    app.config.from_object(Config)
    return app

# Create the Flask app at module level for Gunicorn
app = create_app()

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the M16_Mini API!"})

def check_database_connection():
    """Check database connection and print results."""
    try:
        # Create an engine to connect to the PostgreSQL database
        engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
        # Attempt to connect to the database
        connection = engine.connect()
        print("Database connection successful!")
        connection.close()
    except OperationalError as e:
        print(f"Error: {e}")
        print("Database connection failed.")

def run_tests():
    """Run unit tests."""
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir='tests', pattern='test_*.py')
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    if result.wasSuccessful():
        print("All tests passed.")
    else:
        print(f"Some tests failed. {len(result.failures)} failures.")

if __name__ == "__main__":
    # When running locally for development
    print("Checking database connection...")
    check_database_connection()

    print("Running tests...")
    run_tests()

    # Run the development server
    app.run(debug=True)
