# Importing Libraries
import numpy as np
import pandas as pd
from geopy.geocoders import ArcGIS
nom = ArcGIS()

def address_conversion(df):
    # Converting the Headers to list
    l=list(df)

    # Input Validation (Checks for Address and Address)
    if 'Address' in l:
        # Geoencoding
        df['Address'] = df['Address'].apply(nom.geocode)
        df['latitude'] = df['Address'].apply(lambda x: x.latitude if x != None else None)
        df['longitude'] = df['Address'].apply(lambda x: x.longitude if x != None else None)

        return df

    elif 'address' in l:
        # Geoencoding
        df['address'] = df['address'].apply(nom.geocode)
        df['latitude'] = df['address'].apply(lambda x: x.latitude if x != None else None)
        df['longitude'] = df['address'].apply(lambda x: x.longitude if x != None else None)

        return df

    else:
        print("No Address Column Found")
        return df