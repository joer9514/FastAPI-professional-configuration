# FastAPI Professional Configuration

This project is a boilerplate or template designed to kickstart your FastAPI projects with a professional configuration setup. It includes a variety of tools and configurations to ensure code quality, consistency, and performance.

## Features

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **SQLModel**: For interacting with the database using Python classes.
- **Uvicorn**: An ASGI server for running your application.
- **Jinja2**: A modern and designer-friendly templating language for Python, modelled after Django’s templates.
- **Security**: Includes configurations for CORS, Host Header Injection prevention, and more.
- **Database Support**: Configurations for both MySQL (`aiomysql`) and PostgreSQL (`asyncpg`).
- **Environment Variables**: Use of `.env` files for configuration to keep your secrets safe.
- **Code Quality**: Integration with `flake8`, `black`, `isort`, and `mypy` for linting and formatting.

## Installation

To get started with this project, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/joer9514/fastapi-professional-configuration.git
cd fastapi-professional-configuration
```
2. Install dependencies:
Using Pipenv:

`pipenv install`

Or using Poetry:

`poetry install`

Setup your .env file based on the .env.example provided in the repository.

Run the application:

Using Uvicorn:

`uvicorn main:app --reload`

## Configuration
- Database: Configure your database connection details in the .env file. Supported databases are MySQL and PostgreSQL.
- CORS: Set your whitelist of origins in the .env file to protect against Cross-Origin Resource Sharing (CORS) attacks.
- Server Mode: You can specify the server mode (dev or prod) in the .env file.

## Code Quality
This project is configured with several tools to ensure code quality:

- Flake8 for code linting.
- Black for code formatting.
- isort for import sorting.
- mypy for static type checking.
You can run these tools using the following commands:

```
flake8 .
black .
isort .
mypy .
```

## Contributing
Contributions are welcome! Please feel free to submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
