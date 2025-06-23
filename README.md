# HomeCampus Python

This project contains a small Flask application used for serving math content. It now includes very basic user authentication using **Flask-Login** and **SQLAlchemy**.

## Running locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set the `DATABASE_URL` environment variable if you want to use a database other than the default SQLite database `app.db`. This is useful when deploying to Google Cloud (e.g., Cloud SQL).
3. Initialize the database and run the server:
   ```bash
   python app2.py
   ```

The app will create the database tables on first run. You can then register new users at `/Register` and sign in at `/LoginPage`.
