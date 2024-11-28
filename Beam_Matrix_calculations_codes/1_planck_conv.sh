#!/bin/sh
#PBS -l walltime=48:00:00
#PBS -l mem=30gb,ncpus=24

cd /mnt/home/project/cakashdeep/Akash/Planck_convolution

#mpiexec -n 16 python3 Planck_elliptical_mpi1.py 1
python3 multiprocessor_plank_1.py
#python3   multiprocessor_plank_0extra.py
