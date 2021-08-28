import csv

with open("HW.csv", newline = "") as f:
    reader = csv.reader(f)
    data = list(reader)

data.pop(0)
newData = []

for i in range(len(data)):
    num = data[i][2]
    newData.append(float(num))

n = len(newData)
total = 0
for x in newData:
    total += x

mean = total/n
print(mean)