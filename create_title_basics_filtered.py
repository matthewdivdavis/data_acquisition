import pandas as pd

title_df = pd.read_csv("title.basics.tsv", sep = "\t")

mask = title_df['endYear'].str.contains('\\N', na = False)

title_filter_df = title_df.loc[mask,:]

print("title_df.shape:",title_df.shape)
print("title_filter_df.shape:",title_filter_df.shape)

title_filter_df.to_csv("title_basics_filtered.tsv", sep = "\t")