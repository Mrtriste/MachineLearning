# -*- coding: utf-8 -*-

import csv

# ###### hour_weather
# filename = "data/Hour_Weather.csv"
# tgt = "data/processed/hourWeather.csv"
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


# ###### june load
# filename = "data/June_Load.csv"
# tgt = "data/processed/juneLoad.csv"
# file = open(filename,'r')	
# reader = csv.reader(file)
# cnt = 0
# lst = []
# for row in reader:
# 	temp = row[0:2]
# 	temp[0] = cnt%24
# 	lst.append(temp)
# 	cnt = cnt+1

# csvFile = open(tgt, "wb")
# writer = csv.writer(csvFile)
# writer.writerows(lst)
# csvFile.close()

########
# filename = ["data/July_Load.csv","data/August_Load.csv"]
# tgt = ["data/processed/julyLoad.csv","data/processed/augustLoad.csv"]
# for i in range(0,2):
# 	file = open(filename[i],'r')	
# 	reader = csv.reader(file)
# 	hour_cnt = 0
# 	min_cnt = 0
# 	s = 0
# 	lst = []
# 	for row in reader:
# 		s = s + float(row[1])
# 		min_cnt = min_cnt+1
# 		if min_cnt==12:
# 			temp=range(0,2)
# 			temp[0]=hour_cnt
# 			temp[1]=s/12
# 			lst.append(temp)
# 			hour_cnt = (hour_cnt+1)%24
# 			min_cnt = 0
# 			s = 0
# 	csvFile = open(tgt[i], "wb")
# 	writer = csv.writer(csvFile)
# 	writer.writerows(lst)
# 	csvFile.close()


#######
# filename = ["data/processed/juneLoad.csv","data/processed/julyLoad.csv","data/processed/augustLoad.csv"]
# tgt = 'data/processed/hourLoad.csv'
# lst = []
# for i in range(0,len(filename)):
# 	file = open(filename[i],'r')	
# 	reader = csv.reader(file)
# 	for row in reader:
# 		lst.append(row)

# csvFile = open(tgt, "wb")
# writer = csv.writer(csvFile)
# writer.writerows(lst)
# csvFile.close()

