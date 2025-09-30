# 🍺 BrewDog Beer Explorer - PunkAPI

** A Python project that connects to the Punk API, fetches data about BrewDog beers, stores it in a local SQLite database using SQLAlchemy, and allows the user to query for details like ABV, type of beer, and brewing data. **


## 📌 Features
- Retrieve all beers from the Punk API (400+)
- Store beer details (id, name, description, abv, ibus, brew date)
- Search for beer by name, tagline, etc
- Get a hops list for specific beers 
- Query beers (e.g. high ABV, sours, stouts, etc)
- Print detail about beers

## ⚙️ Installation
1. Clone the repo
2. Create a virtual environment (recommended)
    - python -m venv venv
3. Install dependencies
    - pip install (requirements)


## ▶️ Usage / Querying:


1. ### Querying all sours:

    sours = session.query(AllBrews).filter(or_(AllBrews.tagline.like("%Sour%"),AllBrews.name.like("%Sour%"))).all()
    for beer in sours:
    print(f'Name: {beer.name}, Tagline: {beer.tagline}, ABV: {beer.abv}')

    First Output:

    Name: Spiced Cherry Sour - B-Sides, Tagline: Alternative Festive., ABV: 6.5

2. ### Querying High ABV Brews:

    high_abv = session.query(AllBrews).filter(AllBrews.abv >= 13)

    for row in high_abv:
        print(f'Name: {row.name}\n'
            f'\tTag: {row.tagline}\n'
            f'\tABV: {row.abv}')


    First Output:

    Name: Tokyo*
        Tag: Intergalactic Stout. Rich. Smoky. Fruity.
        ABV: 16.2

3. ### Print Info:

from Beer import Beer
beer = Beer()
beer.print_info("WhiskySour")

Output:
Whisky Sour - B-Sides is a(n) Pilot Brew - Deconstructed Whisky Sour.. It's alcohol content is 7%.
It was first brewed on 03/2015. It contains the following hops: Amarillo, Citra, Simcoe


## 📂 Project Structure

- Beer.py - Beer class for API calls and hops extraction
- BeerList.txt - Full list of beers
- ClassInstance.py - Python file placeholder to create a class instance
- Query.py - Placeholder to create queries on brews database
- Storage.py - SQLAlchemy model and database setup
- README.md - Documentation
- InitialBuild
    - BeerInfo.py - Initial Structure for Beer Class
    - Hops.py - Structure for Hops Method


## 🛠️ Tech / Packages
- Python 3.12
- Requests (API Calls)
- SQLAlchemy (ORM + SQLite)
- PunkAPI (BrewDog Beer Data)


## ✅ Future Improvements

- Add UI
- Store a hops table in DB
- Expand to complex queries
- Add unit testing
