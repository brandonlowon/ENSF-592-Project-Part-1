import json
import numpy as np
import folium
from folium.plugins import MarkerCluster
class Grid:
    def __init__(self, minx, maxx, miny, maxy,identifier, name):
        self.minx = minx
        self.maxx = maxx
        self.miny = miny
        self.maxy = maxy
        self.count = 0
        self.midX = (minx + maxx) / 2
        self.midY = (miny + maxy) / 2
        self.identifier = identifier
        self.name = name

    def checkPoint(self, points : tuple):
        for x, y in points:
                if (x >= self.minx and x < self.maxx):
                    if(y >= self.miny and y < self.maxy):
                            self.count += 1 
    

def getGridCount(grid):
    return grid.count             
def get_geojson_grid(upper_right, lower_left, n, m):
    """Returns a grid of geojson rectangles, and computes the exposure in each section of the grid based on the vessel data.
    Parameters
    ----------
    upper_right: array_like
        The upper right hand corner of "grid of grids" (the default is the upper right hand [lat, lon] of the USA).

    lower_left: array_like
        The lower left hand corner of "grid of grids"  (the default is the lower left hand [lat, lon] of the USA).

    n: integer
        The number of rows/columns in the (n,n) grid.

    list
        List of "geojson style" dictionary objects   
    """
    all_boxes = []

    lat_steps = np.linspace(lower_left[0], upper_right[0], n+1)
    lon_steps = np.linspace(lower_left[1], upper_right[1], m+1)

    lat_stride = lat_steps[1] - lat_steps[0]
    lon_stride = lon_steps[1] - lon_steps[0]

    for lat in lat_steps[:-1]:
        for lon in lon_steps[:-1]:
            # Define dimensions of box in grid
            upper_left = [lon, lat + lat_stride]
            upper_right = [lon + lon_stride, lat + lat_stride]
            lower_right = [lon + lon_stride, lat]
            lower_left = [lon, lat]

            # Define json coordinates for polygon
            coordinates = [
                upper_left,
                upper_right,
                lower_right,
                lower_left,
                upper_left
            ]

            geo_json = {"type": "FeatureCollection",
                        "properties":{
                            "lower_left": lower_left,
                            "upper_right": upper_right
                        },
                        "features":[]}

            grid_feature = {
                "type":"Feature",
                "geometry":{
                    "type":"Polygon",
                    "coordinates": [coordinates],
                }
            }

            geo_json["features"].append(grid_feature)

            all_boxes.append(geo_json)

    return all_boxes

def createMarker(grid : Grid, m :map):
    """Creates a pin on the map with the coordinates cooresponding to the midpoint of the grid with the highest traffic/accident count.
    """
    tooltip = 'Click me!'
    folium.Marker([grid.midX, grid.midY], popup='<i>Highest Accident Traffic</i>', tooltip=tooltip).add_to(m)

def createMap():
    #Creates map of Calgary
    m = folium.Map(
        location=[51.0447, -114.0719], #Coordinates of Calgary
        zoom_start=12   
    )

    #Generate GeoJson Grid
    lowerLeft = [50.85, -114.25]
    upperRight = []
    startlong = -114.25
    long1 = startlong + 0.09
    long2 = long1 + 0.09
    long3 = long2 + 0.09
    endlong = -113.89

    startlat = 50.85
    lat1 = startlat + 0.06
    lat2 = lat1 + 0.06
    lat3 = lat2 + 0.06
    lat4 = lat3 + 0.06
    lat5 = lat4 + 0.06
    endlat = 51.21
    lowerLeft = [startlat, startlong]
    upperRight = [endlat, endlong]

    #Seperating the city into 24 grid sections to determine the section with the most traffic/accidents
    grid1 = Grid(startlat, lat1, startlong, long1,"1", "Ann & Sandy Conservation")
    grid2 = Grid(startlat, lat1, long1, long2, "2", "Bridlewood SW Calgary")
    grid3 = Grid(startlat, lat1, long2, long3, "3", "Sundance S Calgary")
    grid4 = Grid(startlat, lat1, long3, endlong, "4", "Seton SE Calgary")

    grid5 = Grid(lat1, lat2, startlong, long1,"5", "Fish Creek River")
    grid6 = Grid(lat1, lat2, long1, long2,"6", "Fish Creek Pronvince Park")
    grid7 = Grid(lat1, lat2, long2, endlong,"7", "Lake Bonavista & Shepard Industrial")
    grid8 = Grid(lat1, lat2, long3, endlong,"8", "McKenzie Towne & New Brighton")

    grid9 = Grid(lat2, lat3, startlong, long1,"9", "Discovery Ridge")
    grid10 = Grid(lat2, lat3, long1, long2,"10", "Mount Royal Univeristy & West Glenmore Trail")
    grid11 = Grid(lat2, lat3, long2, endlong,"11", "Deerfoot & East Glenmore Trail")
    grid12 = Grid(lat2, lat3, long3, endlong,"12", "East Calgary Landfill Area")

    grid13 = Grid(lat3, lat4, startlong, long1,"13", "Sarcee Trail & Coach Hill")
    grid14 = Grid(lat3, lat4, long1, long2,"14", "West Downtown Area & Crowchild Trail")
    grid15 = Grid(lat3, lat4, long2, long3,"15", "East Downtown Area & Memorial Drive & Deerfoot Trail")
    grid16 = Grid(lat3, lat4, long3, endlong,"16", "16th Avenue East and Stoney Trail")

    grid17 = Grid(lat4, lat5, startlong, long1,"17", "Crowchild Trail & Stoney Trail NW Calgary")
    grid18 = Grid(lat4, lat5, long1, long2,"18", "Nose Hill")
    grid19 = Grid(lat4, lat5, long2, long3,"19", "Deerfoot & Airport Area")
    grid20 = Grid(lat4, lat5, long3, endlong,"20", "McKnight Boulevard & Stoney Trail NE Calgary")

    grid21 = Grid(lat5, endlat, startlong, long1,"21", "SpyHill & Stoney Trail")
    grid22 = Grid(lat5, endlat, long1, long2,"22", "Evanston & Stoney Trail")
    grid23 = Grid(lat5, endlat, long2, long3,"23", "Deerfoot Trail & Stoney Trail North Calgary")
    grid24 = Grid(lat5, endlat, long3, endlong,"24", "Skyview Area & Stoney Trail")  

    dataList = [(50.86, -114.24),(50.87, -114.23),(50.87, -114.23),(50.87, -114.23),(50.87,-114.0)] 
    #Test for showcasing how it works

    grids = [grid1, grid2, grid3, grid4, grid5, grid6, grid7, grid8, grid9, grid10, grid11, grid12, grid13, grid14, grid15, grid16, grid17, grid18, grid19, grid20, grid21, grid22, grid23, grid24]
    grids = [grid1, grid2, grid3, grid4]
    for grid in grids: 
        grid.checkPoint(dataList) #Passing the list of coordinates for each grid section

    sortedGrids = sorted(grids, key = getGridCount, reverse= True)

    gridDict = {grid.name:grid.count for grid in sortedGrids}
    return (gridDict)
    

    createMarker(sortedGrids[0],m)
    gridLines = get_geojson_grid(upperRight, lowerLeft,6,4)

    for i, geo_json in enumerate(gridLines):

        gj = folium.GeoJson(geo_json,
                            style_function=lambda feature: {
                                                                            'color':"black",
                                                                            'weight': 2,
                                                                            'dashArray': '5, 5',
                                                                            'fillOpacity': 0.01,
                                                                        })
        m.add_child(gj)

    m.save('map.html') #Creates a html file in my User Directory


createMap()

def createMarkerVolume(x,y): #
    """Creates a pin on the map with the coordinates cooresponding to the midpoint of the grid with the highest traffic/accident count.
    """
    tooltip = 'Click me!'
    folium.Marker([x, y], popup='<i>Highest Accident Traffic</i>', tooltip=tooltip).add_to(m)

