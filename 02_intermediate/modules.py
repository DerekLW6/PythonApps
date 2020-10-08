import time 
import os
import pandas as pd

while True:
    if os.path.exists('Swing/original.csv'):
        data = pd.read_csv('Swing/original.csv')
        print(data.mean())
    else:
        pass
    time.sleep(5)