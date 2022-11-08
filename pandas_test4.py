import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("전국무인교통단속카메라표준데이터.csv", encoding='EUC-KR')

df2 = df.loc[df['시도명'] == '강원도']#강원도만 추출

plt.rc('font', family='gulim')
df2.plot(kind='scatter',x='제한속도',y='설치장소',c=df2.제한속도, cmap='cool')

plt.show()