#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 21:36:49 2018

@author: dylan
"""

import pandas as pd
import numpy as np

def generate_ERL(data):
    building = str(data['Building Number'])
    floor = str(data['Flr'])
    room = str(data['Room'])
    
    ERL = building + "_FL" + floor + "_RM" + room 
    
    return ERL


sites = pd.read_excel('locations.xlsx')

sites['ERL'] = 'ERL'
sites['ERL'] = sites.apply(generate_ERL, axis=1)

writer = ExcelWriter('ERLtest.xlsx')
sites.to_excel(writer, sheet_name='Sheet1')
writer.save()



    
    
    
