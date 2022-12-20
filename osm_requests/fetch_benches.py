import requests
import json


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
    response = requests.post(url, data=query)
    print('Done fetching benches from OSM.')
    return response.json()

def store_osm_benches():
    with open('data/benches.json', 'w') as outfile:
        json.dump(fetch_osm_benches(), outfile)