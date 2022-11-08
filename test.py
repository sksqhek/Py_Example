import matplotlib.pyplot as plt
import csv
f = open('파일.csv')
data = csv.reader(f)

ratio = []
labels = []
for row in data:
    if len(labels) == 0:
        labels = row[1:]
    elif len(ratio) == 0:
        ratio = list(map(int, row[1:]))

plt.rcParams['font.family'] = 'Malgun Gothic'

plt.pie(ratio, labels=labels, autopct='%.1f%%')
plt.show()
