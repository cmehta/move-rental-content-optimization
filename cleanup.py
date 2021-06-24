import pandas as pd

dframe = pd.read_csv("BotifyData.csv", encoding='utf-8', low_memory = False)
#print(df)
#columns = list(df)
#for i in columns:
#    print (df[i][2])

dictionary = {'®':''}
dframe.replace(dictionary, regex=True, inplace=True)
#dframe.to_csv("first.csv",index=False)


df = pd.read_csv("first.csv" )

df2 = pd.read_csv("RentalQueryLast3MonthsRmDate.csv")

#df3 = df.groupby(['Full URL' , 'Title' , 'Internal Inlinks - Anchor Text'])
#df3.first()

df3 = df.drop_duplicates(subset = ['Full URL' , 'Internal Inlinks - Anchor Text'])
#print(df3)

#df3.drop(['Source Full URL','metadata-h2-contents','metadata-h3-contents'], axis=1)

#print(df)
df3["Full URL"].astype(str)
df2["page"].astype(str)


df4 = pd.merge(df3, df2, how='inner', left_on='Full URL', right_on='page')
print(df4)
df4.to_csv("trynew2.csv", index = False)

