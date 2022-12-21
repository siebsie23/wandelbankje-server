import requests
import json
import os
from osm_requests import parse_to_database


def fetch_osm_benches():
    print('Fetching benches from OSM...')
    url = "https://overpass-api.de/api/interpreter"
    query = """
    [out:json];
    area(id:3600047796)->.searchArea;
    (
      node["amenity"="bench"](area.searchArea);
      way["amenity"="bench"](area.searchArea);
    );
    out body;
    >;
    out skel qt;
    """
    response = requests.post(url, data=query, headers={
        'User-Agent': 'Wandelbankje (Linux; x86_64) Python/3.8.5',
    })
    print('Done fetching benches from OSM.')
    return response.json()

def store_osm_benches():
    # Delete old benches.json file
    os.remove('data/benches.json')

    with open('data/benches.json', 'w') as outfile:
        json.dump(fetch_osm_benches(), outfile)
    parse_to_database.parse_to_database()