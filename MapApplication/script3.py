

import folium
import pandas

#open the file with pandas.
df = pandas.read_csv("Volcanoes-USA.txt")
map=folium.Map(location=[df['LAT'].mean(),df['LON'].mean()],zoom_start=12,tiles='Stamen Terrain')


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



#adding markers based on the list 
for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
    map.simple_marker(location=[lat,lon],popup=name, marker_color=color(elev))
   
#create the html file with the parameters
map.create_map(path='test3.html')
