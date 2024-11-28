#!/bin/sh
#PBS -l walltime=48:00:00
#PBS -l mem=20gb,ncpus=24

cd /mnt/home/project/cakashdeep/Akash/Planck_convolution
#mpiexec -n 24 python3 Planck_elliptical_mpi1.py 5
python3 multiprocessor_plank_5.py
