# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 16:25:31 2022

@author: sl691
"""

#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Elsie Liu (elsieliu55@gmail.com)
# Date:   Fall 2022
#--------------------------------------------------------------

# Ask the user for a date, specifying the format
user_date = input("Enter a date (M/D/YYYY)")

#Create a variable pointing to the data file
file_name = './data/raw/sara.txt'

#Create a file object from the file
file_object = open(file_name,'r')

#Read contents of file into a list
line_list = file_object.readlines()

#Close the file
file_object.close()

date_dict = {}
location_dict = {}

#Pretend we read one line of data from the file
for lineString in line_list:
    if lineString[0]  in ('#','u'):
        continue
    
    #Split the string into a list of data items
    lineData = lineString.split("\t")
    #Extract items in list into variables
    record_id = lineData[0]
    obs_date = lineData[2].split(' ')[0]
    obs_lc = lineData[3]
    obs_lat = lineData[5]
    obs_lon = lineData[6]
    if obs_lc in("1","2","3"):
        pass
    else:
        continue
    #Print the location of sara
    #print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")
    date_dict[record_id]= obs_date
    location_dict[record_id]=(obs_lat,obs_lon)
    #Create an empty key list
    matching_keys = []
    
    # Loop through all key, value pairs in the date_dictionary
    for the_key, the_value in date_dict.items():
        #See if the date (the value) matches the user date
        if the_value == user_date:
            matching_keys.append(the_key)
#Reveal locations for each key in matching_keys
for matching_key in matching_keys:
    obs_lat, obs_lon = location_dict[matching_key]
    print(f"Record {matching_key} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {user_date}")