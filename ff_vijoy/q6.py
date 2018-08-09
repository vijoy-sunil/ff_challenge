#  Create a simple GUI of city information of California
#  See attached JSON file (ca.json), which contains information of all cities in California.
#  Use the data abstract from the JSON file to create a simple GUI for it
#  The GUI should have a filter function based on the selection of city name (selectable)
#  Display information of county full name, latitude, longitude
#  Use any python library as needed

import json
from Tkinter import *
import ttk

filename = 'ca.json'
flag_path = 'flag.gif'

with open(filename, 'r') as f:
    data = json.load(f)
    
tag = ['name', 'county_name', 'primary_latitude', 'primary_longitude', 'state_abbreviation'] 

#extract feilds from json
cities = []
counties = {}
lats = {}
longs = {}
state = {}

for index,item in enumerate(data):
    cities.append(data[index][tag[0]])
    counties[cities[index]] = data[index][tag[1]]
    lats[cities[index]] = data[index][tag[2]]
    longs[cities[index]] = data[index][tag[3]]
    state[cities[index]] = data[index][tag[4]]
    
font_size = 16
font_style = "Helvetica"

class CityInfo:
    def __init__(self, master):
        self.master = master
        master.title("City Information")
        master.geometry('620x195')
        # disbale resizing of window
        master.resizable(False, False)

        # field values on start
        self.county = counties[cities[0]]
        self.latitude = lats[cities[0]]
        self.longitude = longs[cities[0]]
        self.state = state[cities[0]]
    
        # flag 
        self.img = PhotoImage(file=flag_path)
        self.flag = Label(image = self.img)
        self.flag.image = self.img
        
        # Create a main menu and add a command to it
        main_menu = Menu(master, tearoff=0)
        main_menu.add_command(label="Quit", command=root.destroy)
        root.config(menu=main_menu)
        
        self.city_label = Label(master, text="City", font=(font_style, font_size))
        
        # combobox
        self.citybox = ttk.Combobox(master, font=(font_style, font_size))
        # apply font to combobox list
        root.option_add('*TCombobox*Listbox.font',(font_style, font_size))  
        self.citybox.bind("<<ComboboxSelected>>", self.cityselect)       
        self.citybox['values']= cities
        self.citybox.current(0)

        #county
        self.countylabel = Label(master, text="County", font=(font_style, font_size))
       
        self.county_label_text = StringVar()
        self.county_label_text.set(self.county)
        self.county_label = Label(master, textvariable=self.county_label_text, background='white',
                                  font=(font_style, font_size))
        
        
        #latitude
        self.latlabel = Label(master, text="Latitude", font=(font_style, font_size))
        
        self.lat_label_text = StringVar()
        self.lat_label_text.set(self.latitude)        
        self.lat_label = Label(master, textvariable=self.lat_label_text, background='white', 
                               font=(font_style, font_size))
              
        
        #longitude
        self.lonlabel = Label(master, text="Longitude", font=(font_style, font_size))

        self.lon_label_text = StringVar()
        self.lon_label_text.set(self.longitude)        
        self.lon_label = Label(master, textvariable=self.lon_label_text, background='white', 
                               font=(font_style, font_size))
        
                           
        # Layout
        self.city_label.grid(column=0, row=0, sticky=W, pady=5)
        self.citybox.grid(column=25, row=0, pady=5)
        
        self.countylabel.grid(column=0, row=1, sticky=W, pady=5)
        self.county_label.grid(column=25, row=1, sticky=W+E, pady=5)
        
        self.latlabel.grid(column=0, row=2, sticky=W, pady=5)
        self.lat_label.grid(column=25, row=2, sticky=W+E, pady=5)
        
        self.lonlabel.grid(column=0, row=3, sticky=W, pady=5)
        self.lon_label.grid(column=25, row=3, sticky=W+E, pady=5)
        
        self.flag.grid(row = 0, column = 100, rowspan = 5, padx = 5, pady = 5, sticky=E)
                           
    
        
    # Methods    
    # event from combobox    
    def cityselect (self, event):
        self.city_selected = self.citybox.get()
        self.updatefields(self.city_selected)
        
    # update all fields    
    def updatefields (self, event):
        self.county_label_text.set(counties[event])
        self.lat_label_text.set(lats[event])
        self.lon_label_text.set(longs[event])   
        
        #self.state_label_text.set(state[event])
      
        
        
if __name__== "__main__":
    root = Tk()
    my_gui = CityInfo(root)
    root.mainloop()
