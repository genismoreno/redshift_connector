# Redshift connect

## Startup
1. Copy-paste the file `docker.env.example` as `docker.env` file and define the env vars properly.
2. Run `docker-compose build`
3. Run `docker-compose run app [table_name] [job_id]`

For more app info run `docker-compose run app -h`.

## New redshift functionalities
If new redshift functionalities are required, please add them in `app/redshift_db.py`.

## Requirements
Under `requirements.txt` file (please keep them alphabetically sorted).

## Pre-commit
Please install the pre-commit hooks: `pre-commit install`.