import pymongo
import csv
from pymongo import MongoClient
import pandas as pd
import pprint
import dns


def get_year_and_type():
    '''gets the year and type selection from the combo boxes
    '''
    year = com_box_year.get()
    type = com_box_type.get()
    print(type, year)
    return type, year

# Read Steps:
# 1. Call get_year_and_type and return year & type of desired dataset
# 2. Find correct collection based off of return values
# 3. Display data (accident vs traffic volume) and (year) [top 10 entries]
# 4. Send status message

# Sort Steps:
# 1. Call get_year_and_type and return year & type of desired dataset
# 2. Find correct collection based off of return values
# 3. Display Data: Sort by traffic volume if type = traffic volume | Sort by accident if type=accident [top 10 entries]
# 4. Send status message

# Analysis Steps:
# 1. Call get_year_and_type and return year & type of desired dataset
# 2. Find correct collection based off of return values
# 3. Find maximum values (sum i think) of traffic volume/accident for 2016, 2017, 2018
# 4. Send status message

# Map Steps:
# 1. Call get_year_and_type and return year & type of desired dataset
# 2. Find correct collection based off of return values
# 3. Find section with max accidents/max traffic volume ???
# 4. Display map with highlighted section
# 5. Send status message


def display_table(type, year):
    '''reads combo box selection and displays table
    '''
    # type = get_year_and_type()[0]
    # year = int(get_year_and_type()[1])

    cluster = MongoClient(
        "mongodb+srv://andrew:1234@cluster0.pgi1d.mongodb.net/CalgaryTraffic?ssl=true&ssl_cert_reqs=CERT_NONE")
    db = cluster.get_database("CalgaryTraffic")

    # Determine correct database-->collection

    column_filter = {'_id': 0,
                     'the_geom': 0,
                     'length_m': 0}

    column_filter_2018 = {'_id': 0,
                          'Shape_Leng': 0,
                          'multilinestring': 0}

    table_read = 0
    table_sort = 0

    if type == "Traffic Volume":
        if year == 2016:
            collection = db.get_collection("TrafficVolumeFlow2016")

            # Read Button Table - Alphabetical
            table_read = collection.find({}, column_filter).sort("segment_name", 1).limit(5)

            # Sort Button Table - Volume Descending
            table_sort = collection.find({}, column_filter).sort("volume", -1).limit(10)

        elif year == 2017:
            collection = db.get_collection("TrafficVolumeFlow2017")
            # Read Button Table - Alphabetical
            table_read = collection.find({}, column_filter).sort("segment_name", 1).limit(10)

            # Sort Button Table - Volume Descending
            table_sort = collection.find({}, column_filter).sort("volume", -1).limit(10)

        elif year == 2018:
            collection = db.get_collection("trafficVolume2018")
            # Read Button Table - Alphabetical
            table_read = collection.find({}, column_filter_2018).sort("SECNAME", 1)

            # Sort Button Table - Volume Descending
            table_sort = collection.find({}, column_filter_2018).sort("VOLUME", 1)

    # if type == "Accident":
    #     collection = db.get_collection("trafficIncidents")
    #     list = db.trafficIncidents.find({$text:{$search: "2020"}}, {'_id': 0, 'INCIDENT INFO': 1, 'DESCRIPTION': 1, 'Count': 1})

    return table_read, table_sort


table_read, table_sort = display_table("Traffic Volume", 2016)

for item in table_read:
    print(item)

print("\n")

for item in table_sort:
    print(item)