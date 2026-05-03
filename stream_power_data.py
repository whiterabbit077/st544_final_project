import pandas as pd

# read the streaming data file
stream_pd = pd.read_csv("power_streaming_data.csv")

# check that it loaded correctly
print("streaming data shape:")
print(stream_pd.shape)

print("\nfirst few rows:")
print(stream_pd.head())