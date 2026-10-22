from utils.osm_client import fetch_osm_data
from utils.gis_client import fetch_gis_data

def fetch_data(source, query):
    if source == "Overpass":
        return fetch_osm_data(query)
    elif source == "2GIS":
        return fetch_gis_data(query)

    else:
        return None