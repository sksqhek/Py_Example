import pandas as pd
import matplotlib.pyplot as plt

seoul_df = pd.read_csv("OBS_ASOS_MNH_20220614192856.csv", encoding='EUC-KR')
deagu_df = pd.read_csv("OBS_ASOS_MNH_20220614192948.csv", encoding='EUC-KR')

print(seoul_df['최고기온(°C)'])
print(deagu_df['최고기온(°C)'])

plt.rc('font', family='gulim')
plt.figure()
seoul_df['최고기온(°C)'].hist()
plt.figure()
deagu_df['최고기온(°C)'].hist()

plt.figure()
boxplot =  seoul_df.boxplot(column=['최고기온(°C)'])
plt.figure()
boxplot =  deagu_df.boxplot(column=['최고기온(°C)'])

plt.show()
