import numpy as np
import pandas as pd
from tqdm import tqdm

Chunk_cuts=np.loadtxt("Chunks_500.txt",delimiter=',')
data_files=[]
for i in range(len(Chunk_cuts)):
    chunk_id=i#int(sys.argv[1])#0+mpi_id*16+rank
    if chunk_id==0:
        chunk_ranges = [0,int(Chunk_cuts[0])]
        data_files.append(f"1new_1024_{chunk_ranges[0]}_{chunk_ranges[1]}.dat")
    else:
        chunk_ranges = [int(Chunk_cuts[chunk_id-1]),int(Chunk_cuts[chunk_id])]
        data_files.append(f"1new_1024_{chunk_ranges[0]}_{chunk_ranges[1]}.dat")
print(data_files[387],data_files[388],data_files[389])
file_max=[]
for f in tqdm(data_files):
    df=pd.read_csv(f,sep=' ',header=None)
    flen=0
    for i in range(len(df)):
        row=df.iloc[i]
        row_len=len(np.trim_zeros(row))
        if row_len>flen:
            flen=row_len
    file_max.append(flen)
print(max(file_max))
print(file_max)
df=[]
