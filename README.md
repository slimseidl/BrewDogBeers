Usage / Querying:

Example:

Querying all sours:

sours = session.query(AllBrews).filter(or_(AllBrews.tagline.like("%Sour%"),AllBrews.name.like("%Sour%"))).all()
for beer in sours:
    print(f'Name: {beer.name}, Tagline: {beer.tagline}, ABV: {beer.abv}')

    Returns something like: 

    Name: Whisky Sour - B-Sides, Tagline: Pilot Brew - Deconstructed Whisky Sour., ABV: 7.0
    Name: Spiced Cherry Sour - B-Sides, Tagline: Alternative Festive., ABV: 6.5
    Name: Lizard Bride - Prototype Challenge, Tagline: Fruit Infused Sour IPA., ABV: 5.7

Querying High ABV Brews:

high_abv = session.query(AllBrews).filter(AllBrews.abv >= 13)

for row in high_abv:
    print(f'Name: {row.name}\n'
          f'\tTag: {row.tagline}\n'
          f'\tABV: {row.abv}')


    Returns something like:

    Name: Tokyo*
        Tag: Intergalactic Stout. Rich. Smoky. Fruity.
        ABV: 16.2
    Name: Sink The Bismarck!
        Tag: IPA For The Dedicated.
        ABV: 41.0
    Name: The End Of History
        Tag: The World's Strongest Beer.
        ABV: 55.0

