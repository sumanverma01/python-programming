import pandas as pd 
df= pd.read_csv(r'C:/Users/suman/OneDrive/Desktop/csv/deliveries.csv')
print(df)
df.head(3)
df.tail(3)
type(df)
df.columns
