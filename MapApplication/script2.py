import folium
import pandas

#open the file with pandas.
df = pandas.read_csv("Volcanoes-USA.txt")
map=folium.Map(location=[45.372,-121.697],zoom_start=12,tiles='Stamen Terrain')
#adding markers based on the list 
for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
    map.simple_marker(location=[lat,lon],popup=name, marker_color='green' if elev in range(0,1000)\
     else 'orange' if elev in range(1000,3000) else 'red')
   
#create the html file with the parameters
map.create_map(path='test3.html')
