import pandas as pd

name_df = pd.read_csv("name.basics.tsv", sep = "\t")

mask = name_df['primaryProfession'].str.contains('actor|actress|director', na = False)

short_name_df = name_df.loc[mask,:]

print(name_df.head())
print("name_df.shape:",name_df.shape)
print("short_name_df.shape:",short_name_df.shape)

short_name_df.to_csv("name_basics_filtered.tsv", sep = "\t")