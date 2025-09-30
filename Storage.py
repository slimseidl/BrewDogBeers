from Beer import Beer
from sqlalchemy import String, Float, Integer, create_engine, Column, UniqueConstraint, Date
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

base = declarative_base() # table inherits from base class, registers with SQLAlchemy


class AllBrews(base): # Class to define a table / fields
    __tablename__ = "BrewDogBeers"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    tagline = Column(String, nullable=False)
    abv = Column(Float)
    ibu = Column(Float)
    first_brewed = Column(Date)




# Setup
engine = create_engine('sqlite:///brews.db') # actual connection to database (new db brews.db)
# base.metadata.drop_all(engine)
base.metadata.create_all(engine) # Creates a table if it doesnt already exist

new_session = sessionmaker(bind=engine) # builds a session to talk to database
session = new_session() # opens a session instance 

# API Calls
all_brews = Beer().get_all_beers()


def parse_first_brewed(fb):
    try:
        if "/" in fb:             # for actual date
            return datetime.strptime(fb, "%m/%Y").date()
        else:
            return datetime.strptime(fb, "%Y").date()
    except Exception:
        return None

for beer in all_brews:
    record = AllBrews(
        id = beer["id"],
        name = beer["name"],
        tagline = beer.get("tagline"),
        abv = beer.get("abv"),
        ibu = beer.get("ibu"),
        first_brewed = parse_first_brewed(beer["first_brewed"])
    )

    session.merge(record)

session.commit()
session.close()


    








