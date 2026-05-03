import os
import time
import pandas as pd

# read the streaming data file
stream_pd = pd.read_csv("power_streaming_data.csv")

output_folder = "stream_data"
os.makedirs(output_folder, exist_ok=True)

for i in range(20):
    sample_df = stream_pd.sample(n=5, replace=False)
    file_name = f"{output_folder}/batch_{i+1}.csv"
    sample_df.to_csv(file_name, index=False)
    print("wrote", file_name)
    time.sleep(10)