import folium
"""
foliumMap is a script that will draw out a map of the City of Calgary where the user can pass a latitude and longitude to pinpoint the area that has the highest traffic volume or incidents.

Resources used: https://python-visualization.github.io/folium/quickstart.html
"""

#
m = folium.Map(
    location=[51.0447, -114.0719], #Coordinates of Calgary
    zoom_start=12   
)

def createMarker(latitude, longitude, name):
    """createMarker will create and pin a marker on the map when given a latitude and longitiude, name arg creates a different version of the pin when the user mouse overs it
    """
    if(name == "Traffic"):
        tooltip = 'Click me!'
        folium.Marker([latitude, longitude], popup='<i>Highest Volume Traffic</i>', tooltip=tooltip).add_to(m)
    elif(name == "Incident"):
        tooltip = 'Click me!'
        folium.Marker([latitude, longitude], popup='<i>Highest Number of Incidents</i>', tooltip=tooltip).add_to(m)

createMarker(51.048149, -114.037943, "Incident") #Coordinates of the highest Traffic flow from one CSV file

m.save('map.html') #Creates a html file in my User Directory