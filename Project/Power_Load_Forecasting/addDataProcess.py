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
# 
filename = "data/processed/hourWeather1.csv"
file = open(filename,'r')
reader = csv.reader(file)
lst = []
for row in reader:
	row.append(float(row[2])*float(row[2]))
	lst.append(row)
csvFile = open(filename, "wb")
writer = csv.writer(csvFile)
writer.writerows(lst)
csvFile.close()
