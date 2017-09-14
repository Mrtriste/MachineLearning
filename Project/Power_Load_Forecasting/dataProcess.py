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

###########
# filename = "data/processed/hourWeather.csv"
# dailyname = "data/Daily_Weather.csv"
# tgt = "data/processed/hourWeather1.csv"

# file = open(dailyname,'r')
# reader = csv.reader(file)
# daily_list = []
# for row in reader:
# 	daily_list.append(row)

# file = open(filename,'r')	
# reader = csv.reader(file)
# lst = []
# for row in reader:
# 	lst.append(row)

# night = [0,1,2,3,4,5,6,19,20,21,22,23]
# for i in range(0,len(daily_list)):
# 	hour = float(daily_list[i][7])
# 	for j in night:
# 		index = i*24+j
# 		lst[index].append(0)
# 	cnt = 0
# 	for j in range(7,19):
# 		index = i*24+j
# 		#print(float(lst[index][5]))
# 		if float(lst[index][5]) == 0:
# 			cnt = cnt+1
# 	if cnt == 0: avg = 0
# 	else: avg = hour/cnt
# 	for j in range(7,19):
# 		index = i*24+j
# 		if float(lst[index][5]) == 0:
# 			lst[index].append(avg)
# 		else: lst[index].append(0)

# csvFile = open(tgt, "wb")
# writer = csv.writer(csvFile)
# writer.writerows(lst)
# csvFile.close()

#########
# filename = "data/processed/hourWeather1.csv"
# file = open(filename,'r')
# reader = csv.reader(file)
# lst = []
# for row in reader:
# 	row.append(float(row[2])*float(row[2]))
# 	lst.append(row)
# csvFile = open(filename, "wb")
# writer = csv.writer(csvFile)
# writer.writerows(lst)
# csvFile.close()


