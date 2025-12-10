
import pandas as pd
import os 
print(os.getcwd())
from pathlib import Path
file_path = Path(r"C:\Users\egzin\Desktop\uni pdfs offline on pc\thesis\DATA\final\cleaning2")

print(os.getcwd())



df = pd.read_csv('filtered_output.csv')
df.columns = ['A', 'B', 'C', 'D']
print(df.columns)
ColB = df["B"]
valuesB = ColB.tolist()

patterns = (
    "<u>",       # likely meta markup
    "the", 
    "just",      # e.g. "the right"
    "top",       # e.g. "top right"
    "guessed",   # e.g. "guessed right"
    "own",       # "own right"
    "all",       # "all right"
    "alright",   # spelling variant
    "not",       # "not right"
    "sit",       # "sit right"
    "works",     # "works right"
    "spelled",   # "spelled right"
    "got",       # "got right"
    "in",        # "in its own right"
    "Pulciano",  # "Pulciano right"
    "type",      # "type right"
    "cupboard",  # "cupboard right"
    "cup",       # "cup right"
    "side",      # "side right"
    "corner"     # "corner right"
)

mask = df['B'].str.endswith(patterns).fillna(False)

df[~mask].to_csv('filtered_OhAndURemoved.csv', index=False)