import pandas

df = pandas.read_csv('app_data.csv')

print(df)


df.to_csv('file.csv')
df.to_json('test.json', orient='records')
