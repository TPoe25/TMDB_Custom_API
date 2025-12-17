# Custom TMBD API

## Movies

## TV

## Ratings

## Authentication

### User Authentication

### Guest Authentication




#### Testing on Postman
```
GET /health
GET /auth/guest-session
GET /trending/all
GET /trending/movies
GET /trending/tv
GET /movies/550
GET /movies/550/recommendations
GET /tv/1399

```
### Python Version
```
This project is developed and tested with **Python 3.11**.
```

```
Python 3.13+ is not supported by psycopg2 at this time.
```

# How to run
activate venv
```
source /Users/taylorpoe/Projects/TMDB_Custom_API/TaylorMDB/bin/activate
```
activate postgres
```
/opt/homebrew/opt/postgresql@15/bin/psql postgres
```
merge api and sql table
```
psql tmdb_api < sql/create_tables.sql
```
merge api and sql indexes
```
psql tmdb_api < sql/indexes.sql
```
script to start and test if user exists
```
source TaylorMDB/bin/activate                         
python scripts/seed_test_user.py
python api/app.py
```