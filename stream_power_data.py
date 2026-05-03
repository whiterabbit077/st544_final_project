import os
import time
import pandas as pd

# read the streaming data file
stream_pd = pd.read_csv("power_streaming_data.csv")

# folder that Spark is watching
output_folder = "stream_data"
os.makedirs(output_folder, exist_ok=True)

print("starting streaming file writer...")

for i in range(20):
    # randomly choose 5 rows
    sample_df = stream_pd.sample(n=5, replace=False)
    # create a new csv file name each time
    file_name = f"{output_folder}/batch_{i+1}.csv"
    # write the sample
    sample_df.to_csv(file_name, index=False)
    print("wrote", file_name)
    # wait 10 seconds before the next file
    time.sleep(10)
        
print("done writing all files")