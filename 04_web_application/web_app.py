import folium
import pandas as pd

# Reading in and building lists for all of the needed columns
data = pd.read_csv('.\\04_web_application\\volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

# Elevation fuction
def elevation_color(elevation):
    if elevation < 500:
        return 'gray'
    elif elevation < 1500:
        return 'blue'
    else:
        return 'red'
    
# Creating the Base Map
map = folium.Map(location= [38.58, -99.1], zoom_start = 3, tiles = "Stamen Terrain")

# Creating a feature group
fvg = folium.FeatureGroup(name="Volcanoes")

# Adding point markers
for lt, ln, el in zip(lat, lon, elev):
    # Cirles as Markers
    # fg.add_child(folium.CircleMarker(location= [lt, ln], radius = 6, popup = str(el) + "m", fill_color=elevation_color(el), color ='grey', fill_opacity=0.7))
                                     
    # Pins as Markers
    fvg.add_child(folium.Marker(location= [lt, ln], popup = str(el) + "m", icon = folium.Icon(color=elevation_color(el))))

fg = folium.FeatureGroup(name="Population Data")

# Geo JSON with Folium
fg.add_child(folium.GeoJson(data = open('.\\04_web_application\\world.json', encoding='utf-8-sig').read(), 
                                   style_function=lambda x: {'fillColor': 'blue' if x['properties']['POP2005'] > 100000000 else 'red'}))


map.add_child(fvg)
map.add_child(fg)

# Layer Control
map.add_child(folium.LayerControl())

# Saving
map.save('.\\04_web_application\\Map1.html')





