# -*- coding: utf-8 -*-

import csv

filename = "data/Data_Weather.csv"
tgt = "data/june_weather.csv"
file = open(filename,'r')	
reader = csv.reader(file)
cnt = 0
lst = []
for row in reader:
	if(reader.line_num<=3):
		temp = row[0:8]
		temp[0] = cnt%24
		if(temp[5]==""):temp[5] = 0
		lst.append(temp)
		cnt = cnt+1
	else:
		break

csvFile = open(tgt, "wb")
writer = csv.writer(csvFile)
writer.writerows(lst)
csvFile.close()