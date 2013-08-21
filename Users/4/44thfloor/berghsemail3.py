# Zarino will put code in here.

# Follow along by creating your own scraper
# -> https://scraperwiki.com/scrapers/new/python
# and typing / copying / pasting into that

import scraperwiki
import requests
import lxml.html

def scrape_people():
        fred = ['http://www.last.fm/charts/artists/hyped/place',
                'http://www.last.fm/charts/tracks/hyped/place']
        cntry = ['United+States',
                 'United+Kingdom',
                 'Sweden',
                 'Norway',
                 'Belgium',
                 'Canada',
                 'Denmark',
                 'France',
                 'Germany',
                 'Italy']
        ctyUS = ['Atlanta',
                 'Austin',
                 'Baltimore',
                 'Boston',
                 'Buffalo',
                 'Chicago',
                 'Cincinnati',
                 'Cleveland',
                 'Columbus',
                 'Dallas',
                 'Denver',
                 'Detroit',
                 'El Paso',
                 'Houston',
                 'Indianapolis',
                 'Jacksonville',
                 'Las Vegas',
                 'Little Rock',
                 'Los Angeles',
                 'Louisville',
                 'Memphis',
                 'Miami',
                 'Milwaukee',
                 'Minneapolis',
                 'Nashville',
                 'New Orleans',
                 'New York',
                 'Orlando',
                 'Pensacola',
                 'Philadelphia',
                 'Phoenix',
                 'Pittsburgh',
                 'Portland',
                 'Richmond',
                 'Rochester',
                 'Sacramento',
                 'San Diego',
                 'San Francisco',
                 'San Jose',
                 'Seattle',
                 'St Louis',
                 'Syracuse',
                 'Tampa',
                 'Virginia Beach',
                 'Washington DC',
                 'West Palm Beach']
        ctyUK = ['Aberdeen',
                 'Birmingham',
                 'Brighton',
                 'Bristol',
                 'Cardiff',
                 'Edinburgh',
                 'Exeter',
                 'Glasgow',
                 'Leeds',
                 'Liverpool',
                 'London',
                 'Manchester',
                 'Newcastle',
                 'Newport',
                 'Nottingham',
                 'Plymouth',
                 'Southampton']
        ctyUK = ['Gothenburg',
                 'Linköping',
                 'Malmö',
                 'Stockholm',
                 'Umeå',
                 'Uppsala',
                 'Västerås']
        ctySP = ['A Coruña',
                 'Alicante',
                 'Barcelona',
                 'Bilbao',
                 'Burgos',
                 'Gijón',
                 'Granada',
                 'Madrid',
                 'Murcia',
                 'Oviedo',
                 'Salamanca',
                 'Seville',
                 'Valencia',
                 'Zaragoza']
        ctyNW = ['Bergen',
                 'Oslo']
        ctyBl = ['Antwerp',
                 'Brussels',
                 'Charleroi',
                 'Brussels',
                 'Ghent',
                 'Liège']
        ctyCA = ['Calgary',
                 'Edmonton',
                 'Halifax',
                 'Montreal',
                 'Ottawa',
                 'Quebec',
                 'Saskatoon',
                 'Toronto',
                 'Vancouver',
                 'Winnipeg']
        ctyDM = ['Copenhagen']
        ctyFR = ['Bordeaux',
                 'Clermont-Ferrand',
                 'Grenoble',
                 'Lille',
                 'Lyon',
                 'Marseille',
                 'Metz',
                 'Montpellier',
                 'Nancy',
                 'Nantes',
                 'Nice',
                 'Paris',
                 'Rennes',
                 'Strasbourg',
                 'Toulouse']
        ctyGR = ['Berlin',
                 'Bremen',
                 'Cologne',
                 'Dresden',
                 'Frankfurt',
                 'Hamburg',
                 'Magdeburg',
                 'Munich',
                 'Rostock',
                 'Stuttgart']
        ctyIT = ['Bari',
                 'Bologna',
                 'Florence',
                 'Genoa',
                 'Milan',
                 'Naples',
                 'Palermo',
                 'Rome',
                 'Turin']
        endSt = ['?limit=50']
        for ix in fred:
            r = requests.get(ix).text
            dom = lxml.html.fromstring(r)
            for profile in dom.cssselect('p.email'):
                d = {
                'email': profile.cssselect('a')[0].get('href'),
                }
                scraperwiki.sqlite.save(['email'], d)

scrape_people()