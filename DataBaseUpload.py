import pymongo
import csv
from pymongo import MongoClient
import pandas as pd

cluster = MongoClient("mongodb+srv://brandon:1234@cluster0.pgi1d.mongodb.net/CalgaryTraffic?retryWrites=true&w=majority")
db = cluster["CalgaryTraffic"]
collection = db["test"]

#One code block for each file, headers have to be exact same name on the volume
"""
csvfile = open('C://test//2017_Traffic_Volume_Flow.csv', 'r')
reader = csv.DictReader( csvfile )
header= [ "year", "segment_name", "the_geom", "length_m", "volume"]

for each in reader:
    row={}
    for field in header:
        row[field]=each[field]
    
    
    db.TrafficVolumeFlow2017.insert_one(row)

"""

#In the example above, TrafficVolumeFlow2017, in db.TrafficVolumeFlow2017.insert_one(row), will create a collection of that name, in the database
#Running the code again will add the same data fields and create duplicates, so you'll have to check the number of rows in the CSV and check if the database has the same number of entries.

"""
csvfile1 = open('C://test//Traffic_Incidents.csv', 'r')
reader = csv.DictReader( csvfile1 )
header= [ "INCIDENT INFO", "DESCRIPTION", "START_DT", "MODIFIED_DT", "QUADRANT", "Longitude", "Latitude", "location", "Count", "id"]

for each in reader:
    row={}
    for field in header:
        row[field]=each[field]

    db.trafficIncidents.insert_one(row)

csvfile2 = open('C://test//Traffic_Incidents_Archive_2016.csv', 'r')
reader = csv.DictReader( csvfile2 )
header= [ "INCIDENT INFO", "DESCRIPTION", "START_DT", "MODIFIED_DT", "QUADRANT", "Longitude", "Latitude", "location", "Count"]

for each in reader:
    row={}
    for field in header:
        row[field]=each[field]

    db.trafficIncidentsArchive2016.insert_one(row)

csvfile2 = open('C://test//Traffic_Incidents_Archive_2017.csv', 'r')
reader = csv.DictReader( csvfile2 )
header= [ "INCIDENT INFO", "DESCRIPTION", "START_DT", "MODIFIED_DT", "QUADRANT", "Longitude", "Latitude", "location", "Count"]

for each in reader:
    row={}
    for field in header:
        row[field]=each[field]

    db.trafficIncidentsArchive2017.insert_one(row)

csvfile3 = open('C://test//Traffic_Volumes_for_2018.csv', 'r')
reader = csv.DictReader( csvfile3 )
header= [ "YEAR", "SECNAME", "Shape_Leng", "VOLUME", "multilinestring"]

for each in reader:
    row={}
    for field in header:
        row[field]=each[field]

    db.trafficVolume2018.insert_one(row)

csvfile3 = open('C://test//TrafficFlow2016.csv', 'r')
reader = csv.DictReader( csvfile3 )
header= [ "year", "segment_name", "the_geom", "length_m", "volume"]

for each in reader:
    row={}
    for field in header:
        row[field]=each[field]

    db.TrafficVolumeFlow2016.insert_one(row)
"""