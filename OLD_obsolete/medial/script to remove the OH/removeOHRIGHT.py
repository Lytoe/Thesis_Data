
import pandas as pd
import os 
print(os.getcwd())
from pathlib import Path
file_path = Path("C:/Users/egzin/Desktop/uni pdfs offline on pc/thesis/DATA/medial/script to remove the (oh right)/")

print(os.getcwd())



df = pd.read_csv('filtered_output2.csv')
df.columns = ['A', 'B', 'C', 'D']
print(df.columns)
ColB = df["B"]
valuesB = ColB.tolist()
print(ColB.str.endswith(("Oh", "oh")))

# we need to handle NaN
mask = df['B'].str.endswith(("Oh", "oh","ah","yeah","that's","that''s", "it''s")).fillna(False)

df[~mask].to_csv('filtered_OhRemoved.csv', index=False)
