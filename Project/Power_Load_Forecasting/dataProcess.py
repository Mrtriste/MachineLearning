# -*- coding: utf-8 -*-

import csv

###### hour_weather
# filename = "data/Hour_Weather.csv"
# tgt = "data/hourWeather.csv"
# file = open(filename,'r')	
# reader = csv.reader(file)
# cnt = 0
# lst = []
# for row in reader:
# 	temp = row[0:8]
# 	temp[0] = cnt%24
# 	if(temp[5]==""):temp[5] = 0
# 	lst.append(temp)
# 	cnt = cnt+1

# csvFile = open(tgt, "wb")
# writer = csv.writer(csvFile)
# writer.writerows(lst)
# csvFile.close()


###### june load
filename = "data/June_Load.csv"
tgt = "data/juneLoad.csv"
file = open(filename,'r')	
reader = csv.reader(file)
cnt = 0
lst = []
for row in reader:
	temp = row[0:2]
	temp[0] = cnt%24
	lst.append(temp)
	cnt = cnt+1

csvFile = open(tgt, "wb")
writer = csv.writer(csvFile)
writer.writerows(lst)
csvFile.close()
