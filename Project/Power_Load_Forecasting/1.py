# #####
# filename = ['data/August_Load.csv','data/July_Load.csv']
# for i in range(0,2):
# 	lst = []
# 	file = open(filename[i])
# 	reader = csv.reader(file)
# 	for row in reader:
# 		temp = row[0:2]
# 		lst.append(temp)
# 	csvFile = open(filename[i],"wb")
# 	writer = csv.writer(csvFile)
# 	writer.writerows(lst)
# 	csvFile.close()

######
# filename = ['data/August_Load.csv','data/July_Load.csv']
# tgtfile = ['data/processed/int/augustLoad.csv','data/processed/int/julyLoad.csv']
# for i in range(0,2):
# 	lst = []
# 	file = open(filename[i])
# 	reader = csv.reader(file)
# 	for row in reader:
# 		lst.append(row)
# 	length = len(lst)
# 	tgt_lst = []
# 	cnt = 0
# 	for j in range(0,length/12/24):
# 		for k in range(0,24):
# 			index = j*24*12+12*k
# 			tgt_lst.append([k,lst[index][1]])

# 	csvFile = open(tgtfile[i],"wb")
# 	writer = csv.writer(csvFile)
# 	writer.writerows(tgt_lst)
# 	csvFile.close()
