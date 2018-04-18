import os
import pandas as pd
import numpy as np
import time

glos = pd.read_excel('CollegeScorecardDataDictionary.xlsx',sheet_name='data_dictionary',usecols='C,E', index_col = 1).to_dict()

lf = 'male.completed_by.4'
default_cols = ['INSTNM']
cols = default_cols + [k for k,v in glos['developer-friendly name'].items() if lf in str(v)]

files = [x for x in os.listdir() if x.endswith('.csv')]

##df = pd.concat((pd.read_csv(f,usecols=cols).dropna(axis=0,how='any') for f in files))

frames = []
for file in files:
    df = pd.read_csv(file,usecols=cols).dropna(axis=0,how='any')
    df['year'] = file[6:10]
    frames.append(df)
df = pd.concat(frames)

df.rename(columns=glos['developer-friendly name'],inplace=True)

df=df[(df.values != 'PrivacySuppressed').all(axis=1)]

df['delta'] = df['title_iv.female.completed_by.4yrs'].astype(float) - df['title_iv.male.completed_by.4yrs'].astype(float)

conditions = [(df['delta'] == 0),(df['delta'] > 0),(df['delta'] < 0)]

choices = ['No Difference','Female Higher','Male Higher']
df['difference'] = np.select(conditions, choices)

gb=df.groupby('difference').size()

