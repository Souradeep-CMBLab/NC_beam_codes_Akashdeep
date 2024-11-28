import numpy as np
import pandas as pd
import sys

Chunk_cuts=np.loadtxt("Chunks_500.txt",delimiter=',')
#data_files=[]
group_boundary=[]
for i in range(0,len(Chunk_cuts),25):
    group_boundary.append(Chunk_cuts[i+24])

import time
from mpi4py import MPI

file_num=int(sys.argv[1])
filename='CMB_realization_'+str(file_num)+'.txt'

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()


start_time = time.time()

sim_map=np.loadtxt(filename,delimiter=',')

if rank==0:
    pixel_ranges = [0,int(group_boundary[0])]
else:
    pixel_ranges = [int(group_boundary[rank-1]),int(group_boundary[rank])]

beam_file='Beam_matrix_part_'+str(rank)+'.dat'
df=pd.read_csv(beam_file,sep=' ',header=None)

conv_map=np.zeros((pixel_ranges[1]-pixel_ranges[0]))
for p in range(pixel_ranges[0],pixel_ranges[1]):
    center_pixel=p
    row_id=p-pixel_ranges[0]
    row=df.iloc[row_id].values
    row=np.trim_zeros(row)
    beam_matrix=row[2:]
    nb_pixels=[int(beam_matrix[i]) for i in range(0,len(beam_matrix),2)]
    nb_beam=np.array([beam_matrix[i] for i in range(1,len(beam_matrix)+1,2)])
    nb_beam=nb_beam/np.sum(nb_beam)
    nb_simmulated=np.array([sim_map[i] for i in nb_pixels])
    conv_temp=np.sum(nb_simmulated*nb_beam)
    conv_map[row_id]=conv_temp

save_file='conv_group'+str(rank)+'.txt'
np.savetxt(save_file,conv_map,delimiter=',')
end_time = time.time()
print("Time taken:", end_time - start_time, "seconds for rank",rank)
df=[]
nb_beam=[]
nb_simmulated=[]
conv_temp=[]
nb_pixels=[]

comm.Barrier()
print('all process are in same stage')
