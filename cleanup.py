import pandas as pd

dframe = pd.read_csv("rental1.csv", encoding='utf-8-sig', low_memory = False)
#columns = list(dframe)
#for i in columns:
#    print (dframe[i][2])

#dictionary = {'®':''}
#dframe.replace(dictionary, regex=True, inplace=True)


dframe.to_csv("first.csv", encoding='utf-8-sig', index=False)
df = pd.read_csv("first.csv" )

df2 = pd.read_csv("RentalQueryLast3MonthsRmDate.csv")

#print(df.isnull().sum())               
#print(df2.isnull().sum())

df3 = df.drop_duplicates(subset = ['Full URL' , 'Internal Inlinks - Anchor Text'])
#print(df3)

#df3.drop(['metadata-h2-contents','metadata-h3-contents','page'], axis=1)


df3 = df3[ (df3['Internal Inlinks - Anchor Text'] != '1') & (df3['Internal Inlinks - Anchor Text'] != '2') & (df3['Internal Inlinks - Anchor Text'] != '3') & (df3['Internal Inlinks - Anchor Text'] != '5') & (df3['Internal Inlinks - Anchor Text'].str.lower() != 'previous') & (df3['Internal Inlinks - Anchor Text'].str.lower() != 'back')]

df3["Trimmed_URL"] = df3['Full URL'].str[24:]   

df3["Full URL"].astype(str)
df2["page"].astype(str)

df4 = pd.merge(df3, df2, how='inner', left_on='Full URL', right_on='page')
#print(df4)

top_searches = df4.sort_values(["impressions"],ascending=[False])
#print(top_searches)

top_searches.to_csv("data.csv", encoding = 'utf-8-sig', index = False)
