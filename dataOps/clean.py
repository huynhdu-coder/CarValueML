import pandas as pd

#read datasets
df = pd.read_csv('data/cars.csv')
# print(df.shape) #(762091,20)
# print(df.head())

#check for duplicates (9145 rows)
duplicatesTotal = df.duplicated().sum()
print(f"Number of duplicates: {duplicatesTotal}")

duplicates = df[df.duplicated()]
print(duplicates.head(20))
print(duplicates.shape)


# #remove duplicates
# df.drop_duplicates(inplace=True)


