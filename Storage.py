from Beer import Beer
from sqlalchemy import String, Float, Integer, ForeignKey, create_engine, Column, UniqueConstraint, Date
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
import sqlite3
from sqlalchemy.exc import IntegrityError
from datetime import datetime

base = declarative_base() # table inherits from base class, registers with SQLAlchemy


class AllBrews(base): # Class to define a table / fields
    __tablename__ = "BrewDogBeers"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    tagline = Column(String)
    content = Column(Float)
    ibus = Column(Float)
    first_brewed = Column(Date)

    hops = relationship("Hops", back_populates="beer")

    __table_args__ = (
        UniqueConstraint('name', name="unique_beer"),
    )

class Hops(base):
    __tablename__ = "Hops"
    id = Column(Integer, primary_key=True, autoincrement=True)
    hop_type = Column(String, nullable=False)
    beer_id = Column(Integer, ForeignKey("BrewDogBeers.id"))

    beer = relationship("AllBrews",back_populates="hops")



# Setup
engine = create_engine('sqlite:///brews.db') # actual connection to database (new db brews.db)
base.metadata.create_all(engine) # Creates a table if it doesnt already exist
base.metadata.drop_all

new_session = sessionmaker(bind=engine) # builds a session to talk to database
session = new_session() # opens a session instance 

# API Calls
all_beers = Beer()
all_brews = all_beers.get_all_beers()
hops_records = all_beers.get_all_hops()


for beer in all_brews:
    fb = beer["first_brewed"]
    try:
        if "/" in fb:             # for actual date
            first_brewed = datetime.strptime(fb, "%m/%Y").date()
        else:
            first_brewed = datetime.strptime(fb, "%Y").date()
    except Exception:
        first_brewed = None


    record = AllBrews(
        id = beer["id"],
        name = beer["name"],
        tagline = beer.get("tagline"),
        content = beer.get("abv"),
        ibus = beer.get("ibu"),
        first_brewed = first_brewed
    )

    try:
        session.add(record)
        session.commit() # commit after every record to handle duplicates, initial add will take longer
    except IntegrityError:
        session.rollback()
        print(f"Duplicate skipped: {beer['name']}")

# Adding hops to hop table
for beer_name, hops in hops_records.items(): 
    beer_obj = session.query(AllBrews).filter_by(name=beer_name).first()

    if beer_obj:
        for hop in hops:
            record = Hops(
                hop_type = hop["Hop Type"],
                beer_id = beer_obj.id
            )
            session.add(record)

session.commit()
session.close()


    








