#######
num = 2
filename = ['data/August_Load.csv','data/July_Load.csv']
tgtfile = ['data/processed/mid/augustLoad.csv','data/processed/mid/julyLoad.csv']
for i in range(0,2):
	lst = []
	file = open(filename[i])
	reader = csv.reader(file)
	for row in reader:
		lst.append(row)
	length = len(lst)
	tgt_lst = []
	cnt = 0
	for j in range(0,length/12/24):
		for k in range(0,24):
			index = j*24*12+12*k
			if index==0: tgt_lst.append([k,lst[index][1]])
			else:
				s = 0
				for l in range(index-num,index+num+1):
					s += float(lst[l][1])
				tgt_lst.append([k,s/(2*num+1)])
	csvFile = open(tgtfile[i],"wb")
	writer = csv.writer(csvFile)
	writer.writerows(tgt_lst)
	csvFile.close()

# #######
# filename = 'data/processed/hourWeather1.csv'
# refer = 'data/Daily_Weather.csv'
# tgt = 'data/processed/hourWeather2.csv'

# import math
# file = open(refer,'r')
# reader = csv.reader(file)
# relst = []
# for row in reader:
# 	relst.append(row)
# file = open(filename,'r')
# reader = csv.reader(file)
# lst = []
# for row in reader:
# 	lst.append(row)
# length = len(relst)
# night = [0,1,2,3,4,5,6,19,20,21,22,23]
# for i in range(0,length):
# 	rain = math.floor(float(relst[i][1])/5)
# 	sun = float(relst[i][7])
# 	for j in range(0,24):
# 		index = i*24+j
# 		lst[index].append(rain)
# 	for j in range(0,24):
# 		index = i*24+j
# 		if j in night:
# 			lst[index].append(-1)
# 		else:
# 			lst[index].append(math.floor(sun/4))

# file = open(tgt,'wb')
# writer = csv.writer(file)
# writer.writerows(lst)
# file.close()
