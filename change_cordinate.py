import os

f = open("train.txt", 'r')
lines = f.readlines()

for line in lines:
	splited_line = line.split(" ")
	path, filename = os.path.split(splited_line[0])
	base, ext = os.path.splitext(filename)
	f2 = open('gt_' + base + '.txt', "w+")
	for i in range(1, len(splited_line)):
		splited_cordinate = splited_line[i].split(",")
		x1 = splited_cordinate[0]
		y1 = splited_cordinate[1]
		x2 = splited_cordinate[2]
		y2 = splited_cordinate[3]
		changed_cordinate = x1+','+y1+','+x2+','+y1+','+x2+','+y2+','+x1+','+y2+','+'korean'+','+'###'+'\n'
		f2.writelines(changed_cordinate)

	f2.close()

f.close()