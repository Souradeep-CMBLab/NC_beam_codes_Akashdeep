'''import numpy as np
day=1
num_cores=24
work_done=24*4*(day-1)
remain_chunks=np.loadtxt('extra_ids.txt',delimiter=',')
for j in range(0,4):
    fname="multiprocessor_plank_"+str(j)+".py"
    f=open(fname,'w')
    f.write('import threading\n')
    f.write('import subprocess\n')
    f.write('\n')
    f.write('def run_script(script_name,argument):\n')
    f.write("   subprocess.run([\"python3\", script_name,str(argument)])")
    f.write('\n')
    f.write('\n')
    for k in range(work_done+j*num_cores,work_done+(j+1)*num_cores):
        i=int(remain_chunks[k])
        txt="p"+str(i)+"_thread = threading.Thread(target=run_script, args=(\"Planck_elliptical_multiprocess"+".py\","+str(i)+"))\n"
        f.write(txt)
    f.write('\n')
    for k in range(work_done+j*num_cores,work_done+(j+1)*num_cores):
        i=int(remain_chunks[k])
        txt="p"+str(i)+"_thread.start()\n"
        f.write(txt)
    f.write('\n')
    for k in range(work_done+j*num_cores,work_done+(j+1)*num_cores):
        i=int(remain_chunks[k])
        txt="p"+str(i)+"_thread.join()\n"
        f.write(txt)
    f.write('\n')
    f.write("print(\"All the processes has been finished executing.\")")
    f.close()'''

import numpy as np
day=1
num_cores=12
work_done=12*4*(day-1)
remain_chunks=np.loadtxt('extra_ids.txt',delimiter=',')
for j in range(0,3):
    if j<2:
        fname="multiprocessor_plank_"+str(j)+".py"
        f=open(fname,'w')
        f.write('import threading\n')
        f.write('import subprocess\n')
        f.write('\n')
        f.write('def run_script(script_name,argument):\n')
        f.write("   subprocess.run([\"python3\", script_name,str(argument)])")
        f.write('\n')
        f.write('\n')
        for k in range(work_done+j*num_cores,work_done+(j+1)*num_cores):
            i=int(remain_chunks[k])
            txt="p"+str(i)+"_thread = threading.Thread(target=run_script, args=(\"Planck_elliptical_multiprocess"+".py\","+str(i)+"))\n"
            f.write(txt)
        f.write('\n')
        for k in range(work_done+j*num_cores,work_done+(j+1)*num_cores):
            i=int(remain_chunks[k])
            txt="p"+str(i)+"_thread.start()\n"
            f.write(txt)
        f.write('\n')
        for k in range(work_done+j*num_cores,work_done+(j+1)*num_cores):
            i=int(remain_chunks[k])
            txt="p"+str(i)+"_thread.join()\n"
            f.write(txt)
        f.write('\n')
        f.write("print(\"All the processes has been finished executing.\")")
        f.close()
    else:
        #num_cores=12
        fname="multiprocessor_plank_"+str(j)+".py"
        f=open(fname,'w')
        f.write('import threading\n')
        f.write('import subprocess\n')
        f.write('\n')
        f.write('def run_script(script_name,argument):\n')
        f.write("   subprocess.run([\"python3\", script_name,str(argument)])")
        f.write('\n')
        f.write('\n')
        for k in range(work_done+j*num_cores,work_done+j*num_cores+8):
            i=int(remain_chunks[k])
            txt="p"+str(i)+"_thread = threading.Thread(target=run_script, args=(\"Planck_elliptical_multiprocess"+".py\","+str(i)+"))\n"
            f.write(txt)
        f.write('\n')
        for k in range(work_done+j*num_cores,work_done+j*num_cores+8):
            i=int(remain_chunks[k])
            txt="p"+str(i)+"_thread.start()\n"
            f.write(txt)
        f.write('\n')
        for k in range(work_done+j*num_cores,work_done+j*num_cores+8):
            i=int(remain_chunks[k])
            txt="p"+str(i)+"_thread.join()\n"
            f.write(txt)
        f.write('\n')
        f.write("print(\"All the processes has been finished executing.\")")
        f.close()
