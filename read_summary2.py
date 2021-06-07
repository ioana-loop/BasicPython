#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 12:03:37 2021

@author: robotduck
"""
#this imports the first CSV file and creates a list of the contents
#then, it extracts the pieces we need from a list
#finally, it writes the extracted rows to a csv file

#import csv
#reader = csv.reader(open('GMDA_004F6M_Layout1_map_Layout1Advanced_2021-04-07_12-09-56-PM_Summary.csv'))

#with open("GMDA_004F6M_Layout1_map_Layout1Advanced_2021-04-07_12-09-56-PM_Summary.csv", 'r') as f:
#    csv_reader = csv.reader(f)
#    
#    lis = [line.split(',') for line in f]        # create a list of lists
#    #for i, x in enumerate(lis):              #print the list items 
#         #print("line{0} = {1}".format(i, x))
#         
#sqrt = lis[11]
#can_acc = lis[12]
#angl_acc = lis[17]
#r = lis[22]
#
#data = [sqrt, can_acc, angl_acc, r]
#
#v = open('summary_output_small.csv', 'w')
#writer = csv.writer(v)
#writer.writerows(data)
#v.close()


### this works! it generates a CSV, but the numerical entry has an "enter" 
### KEEP.
    
import glob
import csv

c = open('summary_output_all.csv', 'w')
writer = csv.writer(c)

for file in glob.glob("*_Summary.csv"):
    with open(file, 'r') as ff:
        csv_reader2 = csv.reader(ff)            
        lis = [line.split(',') for line in ff] 
        lis[11][3] = lis[11][3].strip('\n')
        lis[12][3] = lis[12][3].strip('\n')
        lis[17][3] = lis[17][3].strip('\n')
        lis[22][3] = lis[22][3].strip('\n')
        sqrt = lis[11]
        can_acc = lis[12]
        angl_acc = lis[17]
        r = lis[22]
        data = [sqrt, can_acc, angl_acc, r]     
    writer.writerows(data)
    
c.close()
#    print(files)

