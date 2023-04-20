import pandas as pd

#skiprows=7 은 원하지 않는 7행을 건너뛰기
cfr = pd.read_csv("rn_20221217145512.csv", encoding="cp949", skiprows=7)
print()
max_row = cfr[cfr["강수량(mm)"] == cfr["강수량(mm)"].max()].values[0]
print("{} {}".format(max_row[0], max_row[-1]))