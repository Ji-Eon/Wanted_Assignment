from flask.cli import FlaskGroup
import csv

from project import app, db,WantedCompany


cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()





## CSV File을 읽어드린후 데이터를 자동으로 저장하게 구현되었습니다.
@cli.command("insert_wanted")
def insert_wanted_data():
   CSV_PATH = '/usr/src/app/wanted_temp_data.csv'    
   with open(CSV_PATH, newline='', encoding='utf8') as csvfile:
        data_reader = csv.DictReader(csvfile)
        for row in data_reader:
            db.session.add(WantedCompany(company_ko=row["company_ko"],company_en=row["company_en"],company_ja=row["company_ja"],tag_ko=row["tag_ko"],tag_en=row["tag_en"],tag_ja=row["tag_ja"]))
            db.session.commit()


if __name__ == "__main__":
    cli()
