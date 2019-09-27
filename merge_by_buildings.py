#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 17:31:39 2018

@author: dylan
"""

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile


# Read in files, change linking index
building = pd.read_excel('building_march.xlsx')
spatial = pd.read_excel('spatial_grafton.xlsx')
spatial.columns.values[0] = 'Building Number'
#print(len(building.columns))


# Merge and place in new dataframe
merged = pd.merge(building, spatial, on='Building Number')

#for debugging
#print(len(building.columns)) 


# Write to xlsx 
writer = ExcelWriter('buildings_merged.xlsx')
merged.to_excel(writer, sheet_name='Sheet1')
writer.save()
    
