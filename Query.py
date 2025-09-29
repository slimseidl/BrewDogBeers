from Storage import Session, AllBrews, Hops

session = Session()

sours = session.query("SELECT * FROM BrewDogBeers WHERE tagline like '%Sour%'")

print(f'Name: {sours.name}, Description: {sours.tagline}, ABV: {sours.content}')

