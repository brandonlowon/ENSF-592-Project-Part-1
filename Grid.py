import folium

class Grid:
    def __init__(self, minx, maxx, miny, maxy):
        """
        """
        self.minx = minx
        self.maxx = maxx
        self.miny = miny
        self.maxy = maxy
        self.count = 0
        self.midX = (minx + maxx) / 2
        self.midY = (miny + maxy) / 2

    def checkPoint(self, points : tuple):
        """
        """
        for x, y in points:
                if (x >= self.minx and x < self.maxx):
                    if(y >= self.miny and y < self.maxy):
                            self.count += 1 

def getGridCount(grid):
    return grid.count             

def createMarker(grid : Grid, m :map):
    """Creates a pin on the map with the coordinates cooresponding to the midpoint of the grid with the highest traffic/accident count.
    """
    tooltip = 'Click me!'
    folium.Marker([grid.midX, grid.midY], popup='<i>Highest Volume Traffic</i>', tooltip=tooltip).add_to(m)

def createMap(dataList):
    #Creates map of Calgary
    m = folium.Map(
        location=[51.0447, -114.0719], #Coordinates of Calgary
        zoom_start=12   
    )

    startlong = -114.25
    long1 = startlong + 0.12
    long2 = long1 + 0.12
    endlong = -113.89

    starlat = 50.85
    lat1 = starlat + 0.0875
    lat2 = lat1 + 0.0875
    lat3 = lat2 + 0.0875
    endlat = 51.20

    #Seperating the city into 12 grid sections to determine the section with the most traffic/accidents
    grid1 = Grid(starlat, lat1, startlong, long1)
    grid2 = Grid(starlat, lat1, long1, long2)
    grid3 = Grid(starlat, lat1, long2, endlong)
    grid4 = Grid(lat1, lat2, startlong, long1)
    grid5 = Grid(lat1, lat2, long1, long2)
    grid6 = Grid(lat1, lat2, long2, endlong)
    grid7 = Grid(lat2, lat3, startlong, long1)
    grid8 = Grid(lat2, lat3, long1, long2)
    grid9 = Grid(lat2, lat3, long2, endlong)
    grid10 = Grid(lat3, endlat, startlong, long1)
    grid11 = Grid(lat3, endlat, long1, long2)
    grid12 = Grid(lat3, endlat, long2, endlong)

    #dataList = [(50.86, -114.24),(50.87, -114.23),(50.87, -114.23),(50.87, -114.23),(50.87,-114.0)] 
    #Test for showcasing how it works

    grids = [grid1, grid2, grid3, grid4, grid5, grid6, grid7, grid8, grid9, grid10, grid11, grid12]
    for grid in grids: 
        grid.checkPoint(dataList) #Passing the list of coordinates for each grid section

    sortedGrids = sorted(grids, key = getGridCount, reverse= True)
    createMarker(sortedGrids[0],m)
    
    m.save('map.html') #Creates a html file in my User Directory

