import csv
import pandas as pd

DataUrl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/lol.csv'
df = pd.read_csv(DataUrl,sep='\t')
print(df.head())