import pymongo
import csv
from pymongo import MongoClient
import pandas as pd
import pprint
import dns
import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from foliumMap import createMarker
from matplotlib.ticker import MaxNLocator
from gridDictCreate import createGridDict

def get_year_and_type():
    '''gets the year and type selection from the combo boxes
    '''
    year = com_box_year.get()
    type = com_box_type.get()
    print(type, year)
    return type, year

def read_database(type, year):
    '''reads data from database depending on the type and year selected by the user. Returns two versions of a table, an unsorted version and a sorted version. 

    returns: a tuple of two lists containing table rows.
            table_rows - unsorted table rows
            table_rows_sorted - sorted table rows
    '''
   
    cluster = MongoClient(
            "mongodb+srv://andrew:1234@cluster0.pgi1d.mongodb.net/CalgaryTraffic?ssl=true&ssl_cert_reqs=CERT_NONE")
    db = cluster["Test"]

    # Determine correct database-->collection

    column_filter = {'_id': 0}
    column_sort = {'secname': 1, 'volume': 1, '_id': 0}

    table_read = 0
    table_sort = 0
    limit_count = 20


    if type == "Traffic Volume":
        if year == 2016:
            collection = db.get_collection("TrafficVolume2016")

            # Read Button Table - Alphabetical
            table_read = collection.find({}, column_filter).sort("segment_name", 1).limit(limit_count)
            table_rows = [row for row in table_read]


            # Sort Button Table - Volume Descending
            table_sort = collection.find({}, column_filter).sort("volume", -1).limit(limit_count)
            table_rows_sorted = [row for row in table_sort]


        elif year == 2017:
                collection = db.get_collection("TrafficVolume2017")
                # Read Button Table - Alphabetical
                table_read = collection.find({}, column_filter).sort("segment_name", 1).limit(limit_count)
                table_rows = [row for row in table_read]


                # Sort Button Table - Volume Descending
                table_sort = collection.find({}, column_filter).sort("volume", -1).limit(limit_count)
                table_rows_sorted = [row for row in table_sort]


        elif year == 2018:
                collection = db.get_collection("TrafficVolume2018")
                # Read Button Table - Alphabetical
                table_read = collection.find({}, column_filter).sort("SECNAME", 1).limit(limit_count)
                table_rows = [row for row in table_read]


                # Sort Button Table - Volume Descending
                table_sort = collection.find({}, column_filter).sort("VOLUME", -1).limit(limit_count)
                table_rows_sorted = [row for row in table_sort]


    if type == "Accident":
        if year == 2016:
            collection = db.get_collection("Accident2016")
            table_read = collection.find({}, {'_id': 0, 'index': 0}).sort("INCIDENT INFO", 1).limit(limit_count)
            table_rows = [row for row in table_read]

            table_sort = collection.find({}, {'_id': 0, 'index': 0}).sort("Count", -1).limit(limit_count)
            table_rows_sorted = [row for row in table_sort]


        elif year == 2017:
            collection = db.get_collection("Accident2017")
            table_read = collection.find({}, {'_id': 0, 'index': 0}).sort("INCIDENT INFO", 1).limit(limit_count)
            table_rows = [row for row in table_read]

            table_sort = collection.find({}, {'_id': 0, 'index': 0}).sort("Count", -1).limit(limit_count)
            table_rows_sorted = [row for row in table_sort]


        elif year == 2018:
            collection = db.get_collection("Accident2018")
            table_read = collection.find({}, {'_id': 0, 'index': 0}).sort("INCIDENT INFO", 1).limit(limit_count)
            table_rows = [row for row in table_read]

            table_sort = collection.find({}, {'_id': 0, 'index': 0}).sort("Count", -1).limit(limit_count)
            table_rows_sorted = [row for row in table_sort]


    return table_rows, table_rows_sorted

def display_table():
    '''reads combo box selection and displays table on the GUI
    '''
    try:
        type = get_year_and_type()[0]
        year = int(get_year_and_type()[1])

        data = read_database(type, year)[0]
        print(data)

        create_table(data)
        display_status_message(year, type, button= "Read", is_success = True)

    except :
        display_status_message(year, type, button= "Read", is_success = False)




def display_sorted_table():
    '''Dispalys a sorted version of a specified table on the GUI
    '''
    try:
        type = get_year_and_type()[0]
        year = int(get_year_and_type()[1])

        if type == "Traffic Volume":
            data = read_database(type, year)[1]
            print(data)

        if type == "Accident":
            data = createGridDict(year, type)


        create_table(data)
        display_status_message(year, type, button= "Sort", is_success = True)

    except:
        display_status_message(year, type, button= "Sort", is_success = False)



def create_table(data):
    '''Creates a table 
    '''
    headings = [column_name for column_name, value in data[0].items()]

    # create and add tree (table) to frame
    tree = ttk.Treeview(frm_display, columns = headings, height = 20, show = "headings")
    tree.grid(row = 0, column = 0, sticky = "nsew")

    # configure tree (table) heading and column display
    for i in range(len(headings)):
        tree.heading(i, text = headings[i])
        tree.column(i, anchor = "center", width = 200)

    # add data rows to table  
    for row in data:
        tree.insert('', 'end', values = [value for column_name, value in row.items()])

    # scroll bars
    scroll_y = ttk.Scrollbar(frm_display, orient="vertical", command=tree.yview)
    scroll_y.grid(row =0, column =1, sticky = "ns")

    scroll_x = ttk.Scrollbar(frm_display, orient="horizontal", command= tree.xview)
    scroll_x.grid(row = 1, column = 0, sticky = "ew")

    tree.configure(yscroll = scroll_y.set, xscroll = scroll_x.set)

def display_chart():
    '''reads combo box selection and displays chart
    '''
    try:
        # get type and year from combo box 
        type = get_year_and_type()[0]
        year = get_year_and_type()[1]

        # create figure
        figure1 = plt.Figure(figsize=(5,5), dpi=70)
        ax = figure1.add_subplot(111)

        # add figure to frame
        canvas = FigureCanvasTkAgg(figure1, frm_display)
        canvas.get_tk_widget().grid(row =0, column = 0, sticky = "nsew")

        
        x = [2016, 2017, 2018]
        y = [chart_data(type, year)[0] for year in x] #get the maximum traffic volume for each year in x
        # print(y)

        if type == "Traffic Volume":
            label = "Maximum Traffic Volume"
            title = "Maximum Traffic Volume vs Year"
            y_label = "Traffic Volume"

        if type == "Accident":
            label = "Maximum Number of Accidents"
            title = "Maximum Accidents vs Year"
            y_label = "Incidents"

        

        ax.plot(x, y, marker ='*', label = label)
        ax.legend()
        ax.set_title(title)
        ax.set_xlabel('Year')
        ax.set_ylabel(y_label)
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))

        display_status_message(year, type, "Analysis", True)

    except :
        display_status_message(year, type, "Analysis", False)



def chart_data(type, year):
    cluster = MongoClient(
        "mongodb+srv://andrew:1234@cluster0.pgi1d.mongodb.net/CalgaryTraffic?ssl=true&ssl_cert_reqs=CERT_NONE")
    db = cluster["Test"]

# TRAFFIC MAX
    if type == "Traffic Volume":
        # table_name = f"TrafficVolume{year}"

        if year == 2016:
            collection = db.get_collection("TrafficVolume2016")
            max = collection.find({}, {'_id': 0, 'volume': 1}).sort("volume", -1).limit(1)
            res = []
            res.append(max[0]['volume'])

        elif year == 2017:
            collection = db.get_collection("TrafficVolume2017")
            max = collection.find({}, {'_id': 0, 'volume': 1}).sort("volume", -1).limit(1)
            res = []
            res.append(max[0]['volume'])

        elif year == 2018:
            collection = db.get_collection("TrafficVolume2018")
            max = collection.find({}, {'_id': 0, 'volume': 1}).sort('volume', -1).limit(1)
            res = []
            res.append(max[0]['volume'])

# ACCIDENT MAX
    if type == "Accident":
        res = createGridDict(year, type)[0]["Number of Accidents"]

    return [res]


def display_status_message(year, type, button, is_success):
    '''Displays status message for each button clicked in the GUI

        year: user selection from year combo-box
        type: user selection from type combo-box
        button: button text which identifies button e.g "Read", "Sort". string
        is_success: boolean 
    '''

    if button == "Read":
        if is_success:
            message = f"Successfully displayed {type} table for year {year}"
        else:
            message = f"Failed to display {type} table for year {year}"
    elif button == "Sort":
        if is_success:
            message = f"Successfully sorted {type} table for year {year}"          
        else:
            message = f"Failed to sort {type} table for year {year}"
    elif button == "Analysis":
        if is_success:
            message = f"Successfully displayed {type} analysis plot for year {year}"          
        else:
            message = f"Failed to display {type} analysis plot for year {year}"
    elif button == "Map":
         if is_success:
            message = f"Sucessfully displayed map of maximum {type} for year {year}"
         else:
            message = f"Failed to display map of maximum {type} for year {year}"

    lbl_status_display["text"] = message

    # if is_success == False:
    #     lbl_status_display["bg"] = "red"



window = tk.Tk()
window.title("Calgary Traffic Analysis")
# window.geometry('350x250')

window.rowconfigure(0, minsize = 50, weight = 1)
window.columnconfigure(1, minsize = 50, weight =1)

frm_buttons = tk.Frame(window)
frm_display = tk.Frame(window)
frm_display.rowconfigure(0, minsize = 100, weight =1)
frm_display.columnconfigure(0, minsize = 100, weight = 1)


# left frame
#combo box for type
com_box_type = ttk.Combobox(frm_buttons, values = ["Accident", "Traffic Volume"] )
com_box_type.current(0)
com_box_type.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "ew")

#combo box for year
com_box_year = ttk.Combobox(frm_buttons, values = ["2016", "2017", "2018"] )
com_box_year.current(0)
com_box_year.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "ew")

# button for Read
btn_read = tk.Button(frm_buttons, text = "Read", command = display_table)
btn_read.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "ew")

# button for Sort
btn_sort = tk.Button(frm_buttons, text = "Sort", command = display_sorted_table)
btn_sort.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = "ew")

# button for Analysis
btn_analysis = tk.Button(frm_buttons, text = "Analysis", command = display_chart)
btn_analysis.grid(row = 4, column = 0, padx = 5, pady = 5, sticky = "ew")

# button for Map
btn_map = tk.Button(frm_buttons, text = "Map", command = createMarker)
btn_map.grid(row = 5, column = 0, padx = 5, pady = 5, sticky = "ew")

# label for Status
lbl_status = tk.Label(frm_buttons, text = "Status:")
lbl_status.grid(row = 6, column = 0, padx = 5, pady = 5, sticky = "ew")

# label for Status display
lbl_status_display = tk.Label(frm_buttons, text = "---", bg = "green",  wraplength = 150)
lbl_status_display.grid(row = 7, column = 0, padx = 5, pady = 5, sticky = "ew")

#right frame
txt_display = tk.Text(frm_display)
txt_display.grid(sticky = "nsew")

# position left and right frame 
frm_buttons.grid(row =0, column = 0, sticky = "ns")
frm_display.grid(row =0, column = 1, sticky = "nsew" )


window.mainloop()