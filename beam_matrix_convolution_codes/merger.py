import numpy as np
import sys
import healpy as hp

file_num=int(sys.argv[1])

conv=np.array([])
for i in range(0,20):
    fname='conv_group'+str(i)+'.txt'
    pixels=np.loadtxt(fname,delimiter=',')
    conv=np.concatenate((conv,pixels))

filename='galactic_convoluted_map_'+str(file_num)+'_1.fits'
hp.fitsfunc.write_map(filename, conv,  dtype=None, fits_IDL=True, coord='G', column_names=None,column_units='K', extra_header=(), overwrite=True)
print(len(conv))