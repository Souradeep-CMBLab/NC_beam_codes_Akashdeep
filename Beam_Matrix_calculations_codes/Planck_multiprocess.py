num_cores=24
f=open("multiprocessor_plank_0.py",'w')
f.write('import threading\n')
f.write('import subprocess\n')
f.write('\n')
f.write('def run_script(script_name,argument):\n')
f.write("   subprocess.run([\"python3\", script_name,str(argument)])")
f.write('\n')
f.write('\n')
for i in range(0,num_cores):
    txt="p"+str(i)+"_thread = threading.Thread(target=run_script, args=(\"Planck_elliptical_multiprocess"+".py\","+str(i)+"))\n"
    f.write(txt)
f.write('\n')
for i in range(0,num_cores):
    txt="p"+str(i)+"_thread.start()\n"
    f.write(txt)
f.write('\n')
for i in range(0,num_cores):
    txt="p"+str(i)+"_thread.join()\n"
    f.write(txt)
f.write('\n')
f.write("print(\"All the processes has been finished executing.\")")
f.close()

f=open("multiprocessor_plank_1.py",'w')
f.write('import threading\n')
f.write('import subprocess\n')
f.write('\n')
f.write('def run_script(script_name,argument):\n')
f.write("   subprocess.run([\"python3\", script_name,str(argument)])")
f.write('\n')
f.write('\n')
j=1
for i in range(j*num_cores,(j+1)*num_cores):
    txt="p"+str(i)+"_thread = threading.Thread(target=run_script, args=(\"Planck_elliptical_multiprocess"+".py\","+str(i)+"))\n"
    f.write(txt)
f.write('\n')
for i in range(j*num_cores,(j+1)*num_cores):
    txt="p"+str(i)+"_thread.start()\n"
    f.write(txt)
f.write('\n')
for i in range(j*num_cores,(j+1)*num_cores):
    txt="p"+str(i)+"_thread.join()\n"
    f.write(txt)
f.write('\n')
f.write("print(\"All the processes has been finished executing.\")")
f.close()

f=open("multiprocessor_plank_2.py",'w')
f.write('import threading\n')
f.write('import subprocess\n')
f.write('\n')
f.write('def run_script(script_name,argument):\n')
f.write("   subprocess.run([\"python3\", script_name,str(argument)])")
f.write('\n')
f.write('\n')
j=2
for i in range(j*num_cores,(j+1)*num_cores):
    txt="p"+str(i)+"_thread = threading.Thread(target=run_script, args=(\"Planck_elliptical_multiprocess"+".py\","+str(i)+"))\n"
    f.write(txt)
    
f.write('\n')
for i in range(j*num_cores,(j+1)*num_cores):
    txt="p"+str(i)+"_thread.start()\n"
    f.write(txt)
f.write('\n')
for i in range(j*num_cores,(j+1)*num_cores):
    txt="p"+str(i)+"_thread.join()\n"
    f.write(txt)
f.write('\n')
f.write("print(\"All the processes has been finished executing.\")")
f.close()

f=open("multiprocessor_plank_3.py",'w')
f.write('import threading\n')
f.write('import subprocess\n')
f.write('\n')
f.write('def run_script(script_name,argument):\n')
f.write("   subprocess.run([\"python3\", script_name,str(argument)])")
f.write('\n')
f.write('\n')
j=3
for i in range(j*num_cores,(j+1)*num_cores):
    txt="p"+str(i)+"_thread = threading.Thread(target=run_script, args=(\"Planck_elliptical_multiprocess"+".py\","+str(i)+"))\n"
    f.write(txt)
f.write('\n')
for i in range(j*num_cores,(j+1)*num_cores):
    txt="p"+str(i)+"_thread.start()\n"
    f.write(txt)
f.write('\n')
for i in range(j*num_cores,(j+1)*num_cores):
    txt="p"+str(i)+"_thread.join()\n"
    f.write(txt)
f.write('\n')
f.write("print(\"All the processes has been finished executing.\")")
f.close()
