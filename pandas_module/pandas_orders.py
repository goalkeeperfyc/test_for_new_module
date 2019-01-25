import pandas as pd

data = list(range(10))

df = pd.DataFrame(data, columns=["column"])

#count every unique value's frequency in column
df["column"].value_counts()