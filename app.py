import folium
import pandas
data = pandas.read_csv("Volcanoes_USA.txt")
#from dataFrameSeries to List (working on lists is faster)

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1500:
        return 'green'
    elif 1500 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[48.7767982,-121.8109970])

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, lv in zip(lat, lon, elev):
    fgv.add_child(folium.Marker(location=[lt,ln],popup=str(round(lv))+"m",
     icon=folium.Icon(color=color_producer(lv))))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005']  < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("map1.html")
