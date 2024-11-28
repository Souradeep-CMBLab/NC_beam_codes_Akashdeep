day=5
num_cores=24
work_done=24*4*(day-1)
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
    for i in range(work_done+j*num_cores,work_done+(j+1)*num_cores):
        txt="p"+str(i)+"_thread = threading.Thread(target=run_script, args=(\"Planck_elliptical_multiprocess"+".py\","+str(i)+"))\n"
        f.write(txt)
    f.write('\n')
    for i in range(work_done+j*num_cores,work_done+(j+1)*num_cores):
        txt="p"+str(i)+"_thread.start()\n"
        f.write(txt)
    f.write('\n')
    for i in range(work_done+j*num_cores,work_done+(j+1)*num_cores):
        txt="p"+str(i)+"_thread.join()\n"
        f.write(txt)
    f.write('\n')
    f.write("print(\"All the processes has been finished executing.\")")
    f.close()
