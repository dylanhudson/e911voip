#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 12:50:42 2018

@author: dylan
"""


import pandas as pd
import numpy as np


def get_street_number(data):
    string = str(data['Building Address'])
    split_string = string.split()
    
    streetNumber= split_string[0]
    return streetNumber


def get_street_name(data):
    string = str(data['Building Address'])
    split_string = string.split()
    
    streetName  = split_string[1]
    return streetName
    
#read in file
address = pd.read_excel('locations.xlsx')
#insert new columns
address['NUM'] = 'NUM'
address['ADDR'] = 'ADDR'

#populate new columns with split addresses.
address['NUM'] = address.apply(get_street_number, axis=1)
address['ADDR'] = address.apply(get_street_name, axis=1)

#write to Excel
writer = pd.ExcelWriter('ADDRtest.xlsx')
address.to_excel(writer, sheet_name='Sheet1')
writer.save()

