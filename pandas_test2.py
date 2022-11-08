import pandas as pd

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",
                 names = ['꽃받침길이cm', '꽃받침폭cm', '꽃잎길이cm', '꽃잎폭cm', '종'])

print(df["종"].value_counts())


index_name = ['꽃받침길이cm', '꽃받침폭cm', '꽃잎길이cm', '꽃잎폭cm']
average = pd.DataFrame({
        "Iris-setosa": [df[x].loc[df['종']=="Iris-setosa"].mean() for x in index_name],
        "Iris-versicolor": [df[x].loc[df['종']=="Iris-versicolor"].mean() for x in index_name],
        "Iris-virginica": [df[x].loc[df['종']=="Iris-virginica"].mean() for x in index_name],
    }, index=index_name)

print(average)

