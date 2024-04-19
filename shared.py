#Set up all the locations for each of the families
from ipyleaflet import basemaps

BASEMAPS = {
    "Mapnik": basemaps.OpenStreetMap.Mapnik,
    "NatGeoWorldMap": basemaps.Esri.NatGeoWorldMap,
    "OpenTopoMap": basemaps.OpenTopoMap,
    "NASAGIBS": basemaps.NASAGIBS.ViirsEarthAtNight2012,
}


CITIES = {
    "Nana in Minto": {"latitude": 48.2917, "longitude": -97.3715, "altitude": 824},
    "Daphne in Clovis": {"latitude": 34.4048, "longitude": -103.2052, "altitude": 4285},
    "Grayson in Alamogordo":{"latitude": 32.8995, "longitude": -105.9603, "altitude": 4163},
    "Raegan in Richmond": {"latitude": 37.5413, "longitude": -77.4348, "altitude": 167},
    "Grumpy & GiGi in Grafton": {"latitude": 48.4142, "longitude": -97.4056, "altitude": 820}
}
