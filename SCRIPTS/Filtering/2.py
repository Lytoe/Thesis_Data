import pandas as pd
import os 

os.chdir(r"C:\Users\egzin\Desktop\UniPdfImp\thesis\DATA\SCRIPTS\Filtering")
print(os.getcwd())

df = pd.read_csv('right_NC_Raw_V02.csv')
df.columns = ['A', 'B', 'C', 'D']

ColD = df["D"]

mask = ColD.str.startswith(("</u><u>", "</unc","now","away","there","after","onto","into")).fillna(False)

print(ColD[mask].head(10).tolist())

df[~mask].to_csv('right_Initial_Filtered_V09.csv', index=False)
