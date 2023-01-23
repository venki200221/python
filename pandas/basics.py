import pandas as pd 
df=pd.read_csv("D:\python\pandas\gapminder.csv")
# print(df.head())
# print(df.shape)
# print(df.columns)
# print(df.dtypes)
# print(df.info())
# country_df=df['country']
# print(country_df.tail(-1))

subset=df[['country','continent','year']]
print(subset)
subset_loc=df.loc[0]
subset_head=df.head(n=1)
print(subset_loc)

# country_df=df.loc[0]
# print(country_df)

print(df.iloc[:,range(2)])




