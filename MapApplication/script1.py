import folium
#create the map and zoom
map=folium.Map(location=[45.372,-121.697],zoom_start=12,tiles='Stamen Terrain')
#adding marker
map.simple_marker(location=[45.3288,-121.6625],popup='Mt. Hood Meadows', marker_color='red')
map.simple_marker(location=[45.3311,-121.7311],popup='Timberlake Lodge', marker_color='green')
#create the html file with the parameters
map.create_map(path='test3.html')


