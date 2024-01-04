import pandas as pd
import numpy as np
import random

from scipy.io.wavfile import write
import os
import glob

directory_path = "H:/IOT_Hearing_AID/Hearing-Aid/echo-ha/"
output_wav_directory = "H:/IOT_Hearing_AID/Hearing-Aid/echo-ha/wav/"



excel_file_path = "H:/IOT_Hearing_AID/Hearing-Aid/echo-ha/noise_75.xlsx"

# # Read the Excel file into a pandas DataFrame
df= pd.read_excel(excel_file_path)

df = df.values
df = df.flatten()
df = df.T

signal = (df).astype(np.int16)
from scipy.io.wavfile import write
write("H:/IOT_Hearing_AID/Hearing-Aid/echo-ha/wav/dr_try.wav", 11025, signal)