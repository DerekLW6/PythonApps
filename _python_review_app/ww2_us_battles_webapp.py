import folium
import pandas as pd

# Reading in and building lists for all of the needed columns
data = pd.read_csv('ww2_lat_long_added.csv')
lat = list(data['latitude'])
lon = list(data['longitude'])
name = list(data['Name'])
# elev = list(data['ELEV'])

# Creating the Base Map
map = folium.Map(location= [46.25, 4.75], zoom_start = 3, tiles = "Stamen Terrain")

# Creating a feature group
fvg = folium.FeatureGroup(name="Base Features")

# Adding point markers
for lt, ln, nm in zip(lat, lon, name):                                     
    # Pins as Markers
    fvg.add_child(folium.Marker(location= [lt, ln], popup = str(nm)))

map.add_child(fvg)

# Adding Enemy Feature Group

# Layer Control
map.add_child(folium.LayerControl())

# Saving
map.save('.\\WW2_US_Battles.html')