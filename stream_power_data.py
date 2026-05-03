import os
import pandas as pd

# read the streaming data file
stream_pd = pd.read_csv("power_streaming_data.csv")

# check that it loaded correctly
print("streaming data shape:")
print(stream_pd.shape)

print("\nfirst few rows:")
print(stream_pd.head())

output_folder = "stream_data"
os.makedirs(output_folder, exist_ok=True)

sample_df = stream_pd.sample(n=5, replace=False)
sample_df.to_csv(f"{output_folder}/test_batch.csv", index=False)

print("wrote one test csv file")