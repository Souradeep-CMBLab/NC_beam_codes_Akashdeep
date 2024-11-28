import os
import numpy as np

# Get a list of all files in the current directory
files = os.listdir()

# Filter the list to only include files with .dat extension
dat_files = [file for file in files if file.endswith('.dat')]

dat_files=np.array(dat_files)
np.save('datlist.txt',dat_files)
