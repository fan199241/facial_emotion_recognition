import pandas as pd


df = pd.read_csv('fer2013.csv')

print(df.shape, df.head())
print(df['Usage'].value_counts())