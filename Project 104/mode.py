import csv
from collections import Counter

with open("HW.csv", newline = "") as f:
    reader = csv.reader(f)
    data = list(reader)

data.pop(0)
newData = []
for i in range(len(data)):
    num = data[i][2]
    newData.append(float(num))

data = Counter(newData)
modedataforrange = {
    "110-120": 0,
    "120-130": 0,
    "130-140": 0,    
    "140-150": 0,
    "150-160": 0,
}

for height,occurance in data.items():
    if 110 < float(height) < 120:
        modedataforrange["110-120"]+=occurance
    elif 120 < float(height) < 130:
        modedataforrange["120-130"]+=occurance
    elif 130 < float(height) < 140:
        modedataforrange["130-140"]+=occurance
    elif 140 < float(height) < 150:
        modedataforrange["140-150"]+=occurance
    elif 150 < float(height) < 160:
        modedataforrange["150-160"]+=occurance

moderange,modeoccurance = 0,0

for range,occurance in modedataforrange.items():
    if occurance > modeoccurance:
        moderange,modeoccurance = [int(range.split("-")[0]), int(range.split("-")[1])],occurance
    
mode = float((moderange[0]+moderange[1])/2)

print(mode)

