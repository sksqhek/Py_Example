import pandas as pd
import numpy as np

df1 = pd.DataFrame(data = np.array([[1,5,10],
                    [1,10,20],
                    [1,15,30]]),columns=['ID', 'value1', 'time'])
print(df1)

df2 = pd.DataFrame(data=np.array([[1,2,20],
                    [1,7,30],
                    [1,10,40]]),columns=['ID', 'value2', 'time'])
print(df2)

df3 = pd.merge(df1, df2, how='outer', on=['ID','time'])
df3 = df3[['ID', 'value1','value2', 'time']]

print(df3.fillna(' '))
