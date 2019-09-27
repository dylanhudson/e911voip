#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 12:50:42 2018

@author: dylan
"""


import pandas as pd


def get_street_number(data):
    string = str(data['Building Address'])
    split_string = string.split()

    streetNumber= split_string[0]
    return streetNumber

def get_street_name(data):
    string = str(data['Building Address'])
    split_string = string.split()

    streetName  = split_string[1] + " " + split_string[2]
    return streetName

def generate_ERL(data):
    building = str(data['Building Number'])
    floor = str(data['Flr'])
    room = str(data['Room'])

    room = room.replace(".", "_")

    ERL = building + "_FL" + floor + "_RM" + room

    return ERL

def pop_Operator(data):
    return "1"

def location(data):
    location = "Floor " + str(data['Flr']) + " Room " + str(data['Room'])
    return location

def city(data):
    city = data['City']
    return city

def add_zip(data):
    zcode = data['Zip']
    zcode = int(zcode)
    zcode = "0" + str(zcode)
    return zcode

def add_country(data):
    return "USA"

def add_state(data):
    return "MA"

def sec_desk(data):
    return "MedfordCommCenter"


def trunking(data):
    return 1

def dir_cd(data):
    return "0"

def wireless(data):
    return "0"

def custname(data):
    return "Tufts University"




# Read in source data from file
sites = pd.read_excel('buildings_merged.xlsx')

#create empty dataframe for source data
raw_data = pd.DataFrame()


#Change the building number to slice from raw source
i = 60

while True:
   
    Building_number_string = "G0" + str(i)
    raw_data = sites.loc[ sites['Building Number'] == Building_number_string ]

 
    #**for merging multiple sites
    #raw_data2 = pd.DataFrame()
    #raw_data3 = pd.DataFrame()
    #raw_data4 = pd.DataFrame()
    #raw_data2 = sites.loc[ sites['Building Number'] == "B004"]
    #raw_data3 = sites.loc[ sites['Building Number'] == "B005"]
    #raw_data4 = sites.loc[ sites['Building Number'] == "B006"]
    #raw_data = raw_data.append(raw_data2)
    #raw_data = raw_data.append(raw_data3)
    #raw_data = raw_data.append(raw_data4)
    
    #create new dataframe for provisioning worksheet
    pw = pd.DataFrame()
    
    #create columns
    pw['Operator'] = 'Operator'
    pw['ERLID'] = 'ERLID'
    pw['Building Number (HNO)'] = 'Building Number (HNO)'
    pw['Prefix Directional (PRD)'] = 'Prefix Directional (PRD)'
    pw['Street (RD)'] = 'Street (RD)'
    pw['Trailing Street Suffix (POD)'] = 'Trailing Street Suffix (POD)'
    pw['Location (LOC)'] = 'Location (LOC)'
    pw['City (A3)'] = 'City (A3)'
    pw['State (A1)'] = '(State (A1)'
    pw['Country'] = 'Country'
    pw['Zip Code (PC)'] = 'Zip Code (PC)'


    pw['Direct CD'] = 'Direct CD'
    pw['Wireless Locator'] = 'Wireless Locator'
    pw['Cust Name (NAM)'] = 'Cust Name (NAM)'
    pw['ELIN'] = 'ELIN'
    pw['SecurityDesk Group'] = 'SecurityDesk Group'
    pw['Crisis Email'] = 'Crisis Email'
    pw['URL Data'] = 'URL Data'
    pw['DO NOT EDIT'] = 'DO NOT EDIT'
    
    
    #populate new columns
    
    pw['Operator'] = raw_data.apply(pop_Operator, axis=1)
    pw['ERLID'] = raw_data.apply(generate_ERL, axis=1)
    pw['Building Number (HNO)'] = raw_data.apply(get_street_number, axis=1)
    pw['Street (RD)'] = raw_data.apply(get_street_name, axis=1)
    
    pw['Location (LOC)'] = raw_data.apply(location, axis=1)
    pw['City (A3)'] = raw_data.apply(city, axis=1)
    pw['State (A1)'] = raw_data.apply(add_state, axis=1)
    pw['Country'] = raw_data.apply(add_country, axis=1)
    pw['Zip Code (PC)'] = raw_data.apply(add_zip, axis=1)
    pw['Direct CD'] = raw_data.apply(dir_cd, axis=1)
    pw['Wireless Locator'] = raw_data.apply(wireless, axis=1)
    pw['Cust Name (NAM)'] = raw_data.apply(custname, axis=1)
    #pw['ELIN'] = 'ELIN'
    pw['SecurityDesk Group'] = raw_data.apply(sec_desk, axis=1)
    #pw['Crisis Email'] = 'Crisis Email'
    pw['DO NOT EDIT'] = raw_data.apply(generate_ERL, axis=1)
    
    
    #write to Excel
    name = Building_number_string + "raw_ERL_data.xlsx"
    writer = pd.ExcelWriter(name)
    pw.to_excel(writer, sheet_name='Grafton_Provisioning_Worksheet')
    writer.save()
    i += 1
    
    
    
    
