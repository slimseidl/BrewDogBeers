from Beer import Beer
from sqlalchemy import String, Float, Integer, Text, create_engine, Column, UniqueConstraint
from sqlalchemy.orm import declarative_base, sessionmaker
import sqlite3
from sqlalchemy.exc import IntegrityError
from datetime import datetime


all = Beer()
all_brews = all.get_all_beers()

base = declarative_base()

class dbRecords(base):
    __tablename__ = "BrewDog Beers"
    id_ = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    tagline = Column(String)







