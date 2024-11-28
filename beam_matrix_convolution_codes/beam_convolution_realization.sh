#!/bin/bash
#PBS -l walltime=24:00:00
#PBS -l mem=15gb,ncpus=22

cd /mnt/home/project/cakashdeep/Akash/test_2_mod/conjugated_files/
for i in {0..1}
do
    python3 cmb_realization_generator.py $i
    mpiexec -n 20 python3 elliptical_beam_matrix_convolution.py $i
    python3 merger.py $i

    echo $i of 20 map generated
    filename="CMB_realization_${i}.txt"
#    rm filename 

done
