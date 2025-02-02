# M16_Mini Flask Application

This project is a Flask-based web application designed to interact with a PostgreSQL database and run basic unit tests. It is deployed using Gunicorn on Render for production. This README will guide you through setting up and deploying the app.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Running the App Locally](#running-the-app-locally)
- [Testing](#testing)
- [Deployment](#deployment)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites
Before you begin, ensure you have the following installed:

- Python 3.11 or above
- `pip` for managing Python packages
- PostgreSQL (if running locally)
- `git` (optional, for cloning the repository)

### Step 1: Clone the Repository
Clone this repository to your local machine using the following command:

git clone https://github.com/scoobSRW/M16_Mini.git
cd M16_Mini

### Step 2: Install Dependencies
Create a virtual environment and install the required dependencies:

python3 -m venv .venv
source .venv/bin/activate  # For Linux/macOS
.venv\Scripts\activate     # For Windows
pip install -r requirements.txt

### Step 3: Setup Environment Variables
Make sure to create a `.env` file in the project root and add your environment variables, such as your database URI and any API keys:

# Example .env
SQLALCHEMY_DATABASE_URI=postgresql://user:password@localhost/dbname

## Configuration
This project uses a `Config` class in the `config.py` file to manage configurations such as the database URI and secret keys. You can modify this file to adjust settings for development, testing, or production.

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost/dbname'
    SECRET_KEY = 'your-secret-key'

## Running the App Locally
To run the application locally in development mode, use the following command:

python run.py

This will start the Flask development server. You can access the application at `http://127.0.0.1:5000`.

## Testing
This project includes unit tests that can be run using the `unittest` framework.

To run the tests, use the following command:

python run.py

This will execute the unit tests and print the results to the terminal.

## Deployment

### Step 1: Prepare the App for Deployment
Ensure that the app is configured to use Gunicorn and is ready for deployment. The app should use the `run.py` file as the entry point for Gunicorn:

gunicorn run:app

### Step 2: Deploy to Render
1. Create a new web service on Render.
2. Connect your GitHub repository containing this project.
3. Set up the environment variables in the Render dashboard (e.g., `SQLALCHEMY_DATABASE_URI`, `SECRET_KEY`).
4. Render will automatically detect the Flask app and deploy it.

The app will be available at a Render-provided URL after deployment. You can access the live app from that URL.

## Troubleshooting

- **404 Error**: Ensure that the routes in your Flask application are defined correctly. If you see a 404 error, make sure the `run.py` file is set up with the correct `Flask` application.

- **Database Connection Error**: If you're seeing database connection issues, check the `.env` file to ensure the `SQLALCHEMY_DATABASE_URI` is correct and accessible.

- **Deployment Issues**: If the app isn't deploying correctly, check the logs on Render for any errors. Common issues include missing environment variables or incorrect configurations in `config.py`.

## Contributing
If you'd like to contribute to this project, feel free to submit a pull request. Please make sure to include tests for any new features or bug fixes.

1. Fork the repository.
2. Create a new branch for your changes.
3. Implement your changes and commit them.
4. Push the branch to your fork.
5. Create a pull request with a clear explanation of your changes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
