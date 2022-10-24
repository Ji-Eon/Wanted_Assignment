from flask.cli import FlaskGroup
import csv

from project import app


cli = FlaskGroup(app)



if __name__ == "__main__":
    cli()
