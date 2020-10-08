# Scrape in the WW2 Locations, Conver to lat lon, 
# create HTML file with folium
# https://en.wikipedia.org/wiki/List_of_World_War_II_battles_involving_the_United_States

import pandas as pd 
import numpy as np 

# Geo Libraries
from geopy.geocoders import ArcGIS
nom = ArcGIS()

# Making the geo object
from geopy.geocoders import ArcGIS
nom = ArcGIS()

#ww2_df =  pd.read_html('https://en.wikipedia.org/wiki/List_of_World_War_II_battles_involving_the_United_States')

df = pd.read_excel('ww2_battles.xlsx')

# Geocoding that column
df['Location'] = df['Location'].apply(nom.geocode)

df['latitude'] = df['Location'].apply(lambda x: x.latitude if x != None else None)
df['longitude'] = df['Location'].apply(lambda x: x.longitude if x != None else None)

df.to_excel('ww2_lat_long_added.xlsx')