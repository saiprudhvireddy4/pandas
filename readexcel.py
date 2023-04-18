import pandas as pd
df = pd.read_excel("C:\\Users\\DELLL\\Desktop\\work1.xlsx",sheet_name=0)
df2 = pd.read_excel("C:\\Users\\DELLL\\Desktop\\work1.xlsx",sheet_name=1)


df1 = pd.DataFrame(df)
df3 = pd.DataFrame(df2)

data = [
    ["jai", 46, 78, 66]
]

df3 = pd.DataFrame(data, columns=["Name", "maths", "English", "Science"])

df4 = pd.concat([df1, df3], ignore_index=True)

print(df4)
print(df4.fillna(9))

