from pymongo import MongoClient
class Grid:
    def __init__(self, minx, maxx, miny, maxy, identifier, name):
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
def map_data(type, year):
    cluster = MongoClient(
        "mongodb+srv://andrew:1234@cluster0.pgi1d.mongodb.net/CalgaryTraffic?ssl=true&ssl_cert_reqs=CERT_NONE")
    db = cluster["Test"]

    # TRAFFIC MAX
    if type == "Traffic Volume":
        if year == 2016:
            collection = db.get_collection("TrafficVolume2016")
            max = list(collection.find({}, {'_id': 0, 'the_geom': 1}).sort("volume", -1).limit(1))
            res = []
            tmp = []

            s = max[0]['the_geom']
            s = s.replace("MULTILINESTRING ((", '')
            tmp = s.split(",")
            s = tmp[0]
            res = s.split()
            res[0], res[1] = float(res[0]), float(res[1])

        elif year == 2017:
            collection = db.get_collection("TrafficVolume2017")
            max = list(collection.find({}, {'_id': 0, 'the_geom': 1}).sort("volume", -1).limit(1))
            res = []
            tmp = []

            s = max[0]['the_geom']
            s = s.replace("MULTILINESTRING ((", '')
            tmp = s.split(",")
            s = tmp[0]
            res = s.split()
            res[0], res[1] = float(res[0]), float(res[1])

        elif year == 2018:
            collection = db.get_collection("TrafficVolume2018")
            max = list(collection.find({}, {'_id': 0}).sort("VOLUME", -1).limit(1))
            res = []
            tmp = []

            s = max[0]['multilinestring']
            s = s.replace("MULTILINESTRING ((", '')
            tmp = s.split(",")
            s = tmp[0]
            res = s.split()
            res[0], res[1] = float(res[0]), float(res[1])
    #ACCIDENT MAX
    if type == "Accident":
        if year == 2016:
            collection = db.get_collection("Accident2016")
            max = list(collection.find({}, {'_id': 0, 'Longitude' : 1, 'Latitude' : 1}).sort('Latitude', 1))
            res = []
            for i in range(len(max)):
                res.append(tuple([max[i]['Latitude'],max[i]['Longitude']]))

        elif year == 2017:
            collection = db.get_collection("Accident2017")
            max = list(collection.find({}, {'_id': 0, 'Longitude' : 1, 'Latitude' : 1}).sort('Latitude', 1))
            res = []
            for i in range(len(max)):
                res.append(tuple([max[i]['Latitude'],max[i]['Longitude']]))

        elif year == 2018:
            collection = db.get_collection("Accident2018")
            max = list(collection.find({}, {'_id': 0, 'Longitude' : 1, 'Latitude' : 1}).sort('Latitude', 1))
            res = []
            for i in range(len(max)):
                res.append(tuple([max[i]['Latitude'],max[i]['Longitude']]))

    return res
def getGridCount(grid):
    return grid.count 
def createGridDict():
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

    grids = [grid1, grid2, grid3, grid4, grid5, grid6, grid7, grid8, grid9, grid10, grid11, grid12, grid13, grid14, grid15, grid16, grid17, grid18, grid19, grid20, grid21, grid22, grid23, grid24]

    #Here I am calling Andrew's map_data function to return a list of tuple x-y coordinates
    dataList = map_data("Accident",2017)
    for grid in grids: 
        grid.checkPoint(dataList) #Passing the list of coordinates for each grid section

    sortedGrids = sorted(grids, key = getGridCount, reverse= True)
    gridDict = {grid.name:grid.count for grid in sortedGrids}
    #return gridDict
    #OR FOR TESTING
    for grid in sortedGrids:
        print(grid.count)
    print(gridDict)

#Calling the function to test the code
createGridDict()
