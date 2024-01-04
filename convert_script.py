print("HI")

import pandas as pd
import numpy as np
from scipy.io.wavfile import write
import os
import glob

directory_path = "H:/IOT_Hearing_AID/Hearing-Aid/echo-ha/"
output_wav_directory = "H:/IOT_Hearing_AID/Hearing-Aid/echo-ha/wav/"

# Fetch all Excel files in the directory
excel_files = glob.glob(os.path.join(directory_path, "*.xlsx"))

for excel_file in excel_files:
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(excel_file)

    # Convert DataFrame to numpy array, flatten it, and transpose if needed
    df = df.values.flatten().T.astype(np.int16)

    # Extract file name without extension
    file_name = os.path.splitext(os.path.basename(excel_file))[0]

    # Create the WAV file path using the original file name
    output_wav_path = os.path.join(output_wav_directory, f"{file_name}.wav")

    # Write the numpy array data to a WAV file
    write(output_wav_path, 11025, df)
