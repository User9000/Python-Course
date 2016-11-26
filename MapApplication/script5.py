 

import folium
import pandas

#open the file with pandas.
df = pandas.read_csv("Volcanoes-USA.txt")
map=folium.Map(location=[df['LAT'].mean(),df['LON'].mean()],zoom_start=12,tiles='Mapbox bright')

#function to select the best color for the marker.
def color(elev):
    minimum = int(df['ELEV'].min())
    step=int((df['ELEV'].max()-df['ELEV'].min())/3)

    if elev in range(minimum,minimum+step):
        col='green'
    elif elev in range(minimum+step, minimum+step*2):
        col='orange'
    else:
        col = 'red'
    return col

fg=folium.FeatureGroup(name='Volcano Locations')

#adding markers based on the list 
for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
    map.add_child(folium.Marker(location=[lat,lon],popup=name, icon=folium.Icon(color(elev))))

#add to the map the location options checkbox.
map.add_child(fg)

#populating points from the json file
map.add_child(folium.GeoJson(data=open('world_population.json'),
name='world population',
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<=10000000 else 'orange' if 10000000<x['properties']['POP2005']<20000000 else 'red'}))

#controll for selection
map.add_child(folium.LayerControl())

#create the html file with the parameters
map.save(outfile='test3.html')