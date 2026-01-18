import pandas as pd
import glob

INPUT_FOLDER = "data/biometric_states"
OUTPUT_FILE = "data/biometric_sampled_india.csv"

files = glob.glob(f"{INPUT_FOLDER}/*.csv")

dfs = []
for file in files:
    df = pd.read_csv(file)
    dfs.append(df)

merged_df = pd.concat(dfs, ignore_index=True)
merged_df.to_csv(OUTPUT_FILE, index=False)

print("Merged biometric data rows:", len(merged_df))
print("Saved:", OUTPUT_FILE)
