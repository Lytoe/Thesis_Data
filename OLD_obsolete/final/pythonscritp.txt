import pandas as pd
import os 
print(os.getcwd())

os.chdir(r'G:/Stable/py11env/samples1000/finalPos')
print(os.getcwd())

df = pd.read_csv('sample.csv')
df.columns = ['A', 'B', 'C', 'D']
print(df.columns)

ColD = df["D"]
valuesB = ColD.tolist()

print(ColD.str.startswith("</u>"))

mask = df['D'].str.startswith(('</u>', '?', '.', '!')).fillna(False)
df[mask].to_csv('filtered_output.csv', index=False)








