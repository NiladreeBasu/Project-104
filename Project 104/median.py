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
newData.sort()

if n%2 == 0:
    median1 = float(newData[n//2])
    median2 = float(newData[n//2-1])
    median = (median1 + median2)/2
else:
    median = newData[n//2]

print(median)