import pandas as pd

data = pd.read_csv("techtehvaarfinal.csv")

print(data.head(5))
data.drop_duplicates(keep='last', inplace=True)
print(data.duplicated().sum())
data.to_csv("techtehvaarfinal.csv", index=False)
