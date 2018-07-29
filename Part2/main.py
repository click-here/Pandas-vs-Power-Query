import pandas as pd
df = pd.read_csv('API_EG.USE.ELEC.KH.PC_DS2_en_csv_v2_10034224.csv',skiprows=4)
years = [x for x in df.columns.values if len(x)==4]

df = df[['Country Name'] + years].set_index('Country Name')
df = df.unstack().reset_index()
df.columns = ['year','country','kWh']
df = df.sort_values(['year','kWh'], ascending=[False,False])
df = df.dropna().drop_duplicates('year').set_index('year')
print(df)
