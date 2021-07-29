import pandas as pd
import requests
from ast import literal_eval
import folium
import googlemaps

gmaps = googlemaps.Client(key="AIzaSyDlGa7OeK3KIXBt6oUsZVnG4Yjv1g44HJs")

#df = pd.read_excel('./sample/data3.xlsx')

m=folium.Map(location=[35.865494, 128.593419],zoom_start=12)

#for i in df.index:
folium.CircleMarker([38.0,48.0],
        tooltip = 5,
        color='PuRd',
        fill_color='PuRd'
).add_to(m)

m