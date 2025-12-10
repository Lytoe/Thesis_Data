
naming order is like this :

right_<position>_<stage>_v<version>.csv

Example

right_initial_raw_v01.csv
right_medial_filtered_v02.csv
right_final_cleaned_v03.csv

DATA DESCRIPTION – Keyword "right" Corpus Extraction

Positions:
- initial: <u></u>"Right, ..." 
- medial: "... right ..."
- final: "... right?"<u></u>

Stages:
- raw: direct corpus dump 10k
- filtered: algorithmic removal of non-occurrences, duplicates, noise   
- cleaned: manual checks + formatting

Processed using scripts in /scripts/

