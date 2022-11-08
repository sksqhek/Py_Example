import pandas as pd

exam_data = {'이름':['서준','우현','인아'],
            '수학':[90,80,70],
            '영어':[98,89,95],
            '음악':[85,95,100],
            '체육':[100,90,90]}
df = pd.DataFrame(exam_data)
df.set_index('이름', inplace=True)
print(df)
print('\n')

rlen, clen = df.shape
print(rlen, clen)
print('\n')

df['총점'] = df.sum(axis=1)#df['수학'] + df['영어'] + df['음악'] + df['체육']
df['평균'] = df['총점'] / clen
print(df)
print('\n')

print(df)
print('\n')

df.loc['평균'] = df.sum(axis=0)/rlen
print(df)
print('\n')

print(df)
print('\n')

df.to_csv('data.csv')


print("read test")
read_test = pd.read_csv('data.csv')
print(read_test)