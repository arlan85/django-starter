# Django Project Details

## Project Overview

This is a Django web application project that implements a multi-department dashboard system. The project consists of a main `dashboard` project and three department-specific Django apps: `engineering_dept`, `marketing_dept`, and `sales_dept`. Each department has its own dedicated views, URL routing, and test suite.

### Project Structure

The project contains a root configuration and aplication configurations for three departments: Engineering, Markteting, and Sales.

```text
01_05_challenge_ci_workflow/
├── dashboard/             # Main Django project
│   ├── settings.py        # Project settings and configuration
│   ├── urls.py            # Root URL configuration
│   ├── tests.py           # Dashboard-level tests
│   ├── wsgi.py            # WSGI configuration
│   └── asgi.py            # ASGI configuration
├── *_dept/                # Department apps
│   ├── views.py           # Views
│   ├── urls.py            # URL routing
│   ├── tests.py           # Tests
│   └── models.py          # Models (currently empty)
├── manage.py              # Django management script
├── Makefile               # Build automation
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

### Project Purpose

The project serves as a demonstration of Django's multi-app architecture pattern.

The main `dashboard` project coordinates these apps through URL routing, with each department accessible via its own namespace. The project uses SQLite as the default database and includes Django's standard admin interface.

Each department app displays a welcome message for the corresponding department:

- **Engineering Department** (`/engineering/`)
- **Marketing Department** (`/marketing/`)
- **Sales Department** (`/sales/`)

### Dependencies

- **Django**: Version 5.0 or higher (but less than 6.0) as specified in `requirements.txt`

## Running the Project

The project includes a `Makefile` with several convenient commands for development and testing.

### Available Makefile Targets

| Command | Description |
|---------|-------------|
| `make install` | Install Python dependencies from requirements.txt |
| `make run` | Start the Django development server |
| `make test` | Run all Django tests |
| `make migrations` | Create and apply database migrations |
| `make clean` | Remove bytecode, database, and temporary files |
| `make help` | Display available commands |

### Prerequisites

- Python 3.x installed on your system
- `pip` package manager
- `make` utility (available on macOS, Linux, and Windows with appropriate tools)

### Installation

Install project dependencies:

```bash
make install
```

This command runs `pip install -r requirements.txt` to install Django and other required packages.

### Running the Development Server

Start the Django development server:

```bash
make run
```

This starts the Django development server, typically accessible at `http://127.0.0.1:8000/`. The server will automatically reload when you make code changes.

### Database Migrations

Create and apply database migrations:

```bash
make migrations
```

This command:

1. Runs `python manage.py makemigrations` to detect model changes
2. Runs `python manage.py migrate` to apply migrations to the SQLite database

> [!NOTE]
> Since the department apps don't currently define any models, migrations may not create any tables beyond the Django defaults (auth, sessions, etc.).

### Running Tests

Execute all tests in the project:

```bash
make test
```

This runs `python manage.py test`, which discovers and executes all test cases in:

- `dashboard/tests.py`
- `engineering_dept/tests.py`
- `marketing_dept/tests.py`
- `sales_dept/tests.py`

### Cleaning Up

Remove generated files and the database:

```bash
make clean
```

This command:

- Removes all `__pycache__` directories (Python bytecode)
- Removes `.DS_Store` files (macOS metadata)
- Deletes the `db.sqlite3` database file

## Tests

The project includes comprehensive test coverage across all apps. Tests are located in `tests.py` files within each app directory.

### Dashboard Tests (`dashboard/tests.py`)

The dashboard tests verify URL routing and HTTP response codes:

- **`test_root_url_404`**: Verifies that the root URL (`/`) returns a 404 status code since no view is mapped to it
- **`test_department_pages_resolve`**: Ensures that all three department endpoints (`/engineering/`, `/marketing/`, `/sales/`) return HTTP 200 OK status codes

These tests use Django's `SimpleTestCase` and `Client` to simulate HTTP requests.

### Engineering Department Tests (`engineering_dept/tests.py`)

Tests verify the app configuration:

- **`test_app_is_registered`**: Confirms that `engineering_dept` is properly installed in `INSTALLED_APPS` in `settings.py`
- **`test_app_name_is_correct`**: Validates that the app configuration has the expected name `engineering_dept`

These tests use Django's app registry to verify configuration.

### Marketing Department Tests (`marketing_dept/tests.py`)

Tests verify the marketing view functionality:

- **`test_marketing_index_content`**: Checks that the marketing page response contains the word "Marketing" in its content. Uses Django's URL reversing with the `marketing:index` namespace to test the view.

### Sales Department Tests (`sales_dept/tests.py`)

Tests verify external dependencies:

- **`test_math_library_available`**: Verifies that the `numpy` library can be imported. This test checks for a dependency that may be required for sales calculations, though `numpy` is not currently listed in `requirements.txt`.

> [!TIP]
> The sales test expects `numpy` to be available, but it's not included in `requirements.txt`. This may be intentional for the CI/CD challenge, requiring you to add it to the dependencies or handle the import appropriately.

### Running Specific Tests

You can run tests for a specific app using Django's test command:

```bash
# Run only dashboard tests
python manage.py test dashboard

# Run only engineering department tests
python manage.py test engineering_dept

# Run only marketing department tests
python manage.py test marketing_dept

# Run only sales department tests
python manage.py test sales_dept
```

### Test Coverage

The test suite covers:

- ✅ URL routing and HTTP responses
- ✅ App registration and configuration
- ✅ View content validation
- ✅ External dependency checking

All tests use Django's built-in testing framework, making them suitable for integration into CI/CD pipelines.
