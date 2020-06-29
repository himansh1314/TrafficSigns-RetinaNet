# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 13:17:33 2020

@author: Himansh
"""

import os
gt = open('gt.txt', 'r')
converted = open("converted.csv", 'w')
for line in gt:
    line = line.replace(";", ",")
    converted.write(line)
gt.close()
converted.close()
    
