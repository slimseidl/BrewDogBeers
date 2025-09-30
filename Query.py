from Storage import AllBrews, base
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///brews.db')
Session = sessionmaker(bind=engine)
session = Session()


# Querying all sours
# sours = session.query(AllBrews).filter(or_(AllBrews.tagline.like("%Sour%"),AllBrews.name.like("%Sour%"))).all()

# for beer in sours:
    #print(f'Name: {beer.name}, Tagline: {beer.tagline}, ABV: {beer.abv}')

# Querying High ABV Brews

high_abv = session.query(AllBrews).filter(AllBrews.abv >= 13)


# Querying Stouts
stout = session.query(AllBrews).filter(AllBrews.tagline.like('%Stout%'))

for row in stout: # for row in (xxxx) change xxxx to query name
    print(f'Name: {row.name}\n'
          f'\tTag: {row.tagline}\n'
          f'\tABV: {row.abv}')



