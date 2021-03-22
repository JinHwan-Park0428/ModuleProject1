###미완성

import csv
import re

total_num_list = []
line_list = []
i = 0 
file = open('covid19.csv', 'r', encoding='cp949')

data = csv.reader(file)
header = next(data)

print("시도" + "%10s" % "계" + "%10s" % "12월" + "%10s" % "11월" + "%10s" % "10월")

for line in data :
    total_num = 0
    for l in line[2 : ] :
        if ',' in l :
            l = re.sub(',', '', l)
        try:
            total_num += int(l)
        except Exception :
            pass

    total_num_list.append(total_num)
    line_list.append([line[1], total_num_list[i], line[2].strip(), line[3].strip(), line[4].strip()])

    i+=1

for j in line_list :
    print(j[0] + "%10s" % j[1] + "%10s" % j[2] + "%10s" % j[3] + "%10s" % j[4])

file.close()