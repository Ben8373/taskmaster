# Taskmaster

A Django-based task management application that allows users to organize tasks into categories and track their completion status.

## Features

- **Category Management**: Create and organize tasks by categories
- **Task Management**: Create tasks with titles, due dates, and completion tracking
- **Database Support**: PostgreSQL or SQLite
- **Secure Configuration**: Environment variables for sensitive settings
- **Admin Interface**: Built-in Django admin panel for managing tasks and categories

## Project Structure

```
taskmaster/
├── taskmaster/          # Project configuration
│   ├── settings.py      # Django settings (uses environment variables)
│   ├── urls.py          # URL routing
│   ├── asgi.py          # ASGI configuration
│   └── wsgi.py          # WSGI configuration
├── tasks/               # Task management app
│   ├── models.py        # Category and Task models
│   ├── views.py         # Views
│   ├── admin.py         # Admin configuration
│   └── migrations/      # Database migrations
├── manage.py            # Django management script
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variables template
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Prerequisites

- Python 3.8+
- PostgreSQL (optional, SQLite is default)
- pip

## Installation

### 1. Clone the Repository

```powershell
git clone https://github.com/YOUR_USERNAME/taskmaster.git
cd taskmaster
```

### 2. Create Virtual Environment

```powershell
python -m venv .venv
```

### 3. Activate Virtual Environment

**Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
.venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 5. Set Up Environment Variables

Create a `.env` file in the project root by copying from `.env.example`:

```powershell
Copy-Item .env.example .env
```

Edit `.env` with your actual values:

```
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

**For PostgreSQL:**
```
DATABASE_URL=postgresql://username:password@localhost:5432/taskmaster_db
```

### 6. Apply Migrations

```powershell
python manage.py migrate
```

### 7. Create Superuser

```powershell
python manage.py createsuperuser
```

You'll be prompted for:
- Username
- Email
- Password

### 8. Run Development Server

```powershell
python manage.py runserver
```

Visit `http://localhost:8000/admin` to access the Django admin panel.

## Database Configuration

### Using SQLite (Default)

Set in `.env`:
```
DATABASE_URL=sqlite:///db.sqlite3
```

### Using PostgreSQL (Recommended for Production)

**Install PostgreSQL**

**Create database and user:**
```sql
CREATE DATABASE taskmaster_db;
CREATE USER taskmaster_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE taskmaster_db TO taskmaster_user;
```

**Set in `.env`:**
```
DATABASE_URL=postgresql://taskmaster_user:your_password@localhost:5432/taskmaster_db
```

## Models

### Category

| Field | Type | Description |
|-------|------|-------------|
| id | Integer | Primary Key (Auto-increment) |
| name | String | Category name (unique) |
| created_at | DateTime | Auto-created timestamp |

### Task

| Field | Type | Description |
|-------|------|-------------|
| id | Integer | Primary Key (Auto-increment) |
| title | String | Task title |
| due_date | Date | Task deadline |
| completed | Boolean | Completion status (default: False) |
| category | ForeignKey | Link to Category (one-to-many) |
| created_at | DateTime | Auto-created timestamp |
| updated_at | DateTime | Auto-updated timestamp |

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| SECRET_KEY | Yes | Django secret key for security |
| DEBUG | No | Debug mode (True/False, default: False) |
| DATABASE_URL | No | Database connection string |

**Never commit your `.env` file to GitHub!** Use `.env.example` as a template.

## Making Migrations

After modifying models:

```powershell
python manage.py makemigrations
python manage.py migrate
```

## Useful Commands

```powershell
# Run tests
python manage.py test

# Create new app
python manage.py startapp app_name

# Shell access
python manage.py shell

# Collect static files (production)
python manage.py collectstatic

# Check for issues
python manage.py check
```

## Security Notes

⚠️ **For Production:**

1. Set `DEBUG = False` in `.env`
2. Generate a strong `SECRET_KEY` (don't use the default)
3. Set `ALLOWED_HOSTS` in `settings.py`
4. Use `SECURE_SSL_REDIRECT = True`
5. Use PostgreSQL instead of SQLite
6. Keep `.env` file secure and never commit it

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License

MIT License

## Support

For issues or questions, please open an issue on GitHub.
