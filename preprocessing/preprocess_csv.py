# -*- coding: utf-8 -*-
"""
Created on Mon May 25 11:36:17 2020

@author: Himansh
"""
import csv

csvfile = open('converted_retinanet.csv')
csvReader = csv.reader(csvfile)


class_dict = {
0: "speed limit 20", 
1: "speed limit 30", 
2: "speed limit 50", 
3: "speed limit 60", 
4 : "speed limit 70", 
5 : "speed limit 80", 
6 : "restriction ends 80", 
7 : "speed limit 100", 
8 : "speed limit 120", 
9 : "no overtaking", 
10 : "no overtaking (trucks)", 
11 : "priority at next intersection", 
12 : "priority road",
13 : "give way", 
14 : "stop", 
15 : "no traffic both ways", 
16 : "no trucks", 
17 : "no entry", 
18 : "danger", 
19 : "bend left", 
20 : "bend right", 
21 : "bend",
22 : "uneven road", 
23 : "slippery road", 
24 : "road narrows", 
25 : "construction", 
26 : "traffic signal", 
27 : "pedestrian crossing", 
28 : "school crossing", 
29 : "cycles crossing", 
30 : "snow", 
31 : "animals", 
32 : "restriction ends", 
33 : "go right", 
34 : "go left", 
35 : "go straight", 
36 : "go right or straight", 
37 : "go left or straight", 
38 : "keep right", 
39 : "keep left", 
40 : "roundabout", 
41 : "restriction ends (overtaking)", 
42 : "restriction ends (overtaking (trucks))",
}

rowList = [row for row in csvReader]
updatedList = []
for row in range(1,len(rowList)):
    rowList[row][-1] = class_dict[int(rowList[row][-1])]
    updatedList.append(rowList[row])

outputFile = open('annotations1.csv', 'w', newline = '')
outputWriter = csv.writer(outputFile)
for row in updatedList:
    outputWriter.writerow(row)
outputFile.close()
