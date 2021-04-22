# How To

1. Activate the Python virtual environment or create one then activate.
2. Install Python packages required `pip install -r requirements.txt`.
3. Create a MySQL database and name it `movie_web_service`.
4. Initialize the database with `flask db init`.
5. Generate migration files with `flask db migrate`.
6. Apply the migrations with `flask db upgrade`.
7. Run the app with `flask run`.

## NOTES

- All credetials or passwords stored in this repository are just for examples.
- CSV file can only be downloaded through browsers.

## API Endpoints

- GET `/api/v1/movies` - Retrieve all movies.
- POST `/api/v1/movies`- Add a new movie.
- GET `/api/v1/movies/<id>` - Get a movie detail by ID.
- PUT `/api/v1/movies/<id>` - Edit a movie detail by ID.
- DELETE `/api/v1/movies/<id>` - Delete a movie by ID.
- GET `/api/v1/movies/export/csv` - Download csv file that contains all movies.
- `/api/v1/movies?search=Terminator%202` - Filter movies by query string.
