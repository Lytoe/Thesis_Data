
import pandas as pd
import os 
os.chdir(r"C:\Users\egzin\Desktop\UniPdfImp\thesis\DATA\RAW\notCategorized")
print(os.getcwd())


df = pd.read_csv('right_NC_Raw_V01.csv')
df.columns = ['A', 'B', 'C', 'D']
#print(df.columns)
ColB = df["B"]
valuesB = ColB.tolist()
#print(ColB.str.endswith(("</u><u>")))

# we need to handle NaN
mask = ColB.str.endswith("</u><u>").fillna(False)
print(ColB[mask].head(10))
df[mask].to_csv('right_NC_Raw_V02.csv', index=False)
