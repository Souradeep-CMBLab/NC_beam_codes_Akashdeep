import threading
import subprocess

def run_script(script_name,argument):
   subprocess.run(["python3", script_name,str(argument)])

p16_thread = threading.Thread(target=run_script, args=("Planck_elliptical_multiprocess.py",16))
p17_thread = threading.Thread(target=run_script, args=("Planck_elliptical_multiprocess.py",17))
p18_thread = threading.Thread(target=run_script, args=("Planck_elliptical_multiprocess.py",18))
p19_thread = threading.Thread(target=run_script, args=("Planck_elliptical_multiprocess.py",19))
p20_thread = threading.Thread(target=run_script, args=("Planck_elliptical_multiprocess.py",20))
p21_thread = threading.Thread(target=run_script, args=("Planck_elliptical_multiprocess.py",21))
p22_thread = threading.Thread(target=run_script, args=("Planck_elliptical_multiprocess.py",22))
p23_thread = threading.Thread(target=run_script, args=("Planck_elliptical_multiprocess.py",23))

p16_thread.start()
p17_thread.start()
p18_thread.start()
p19_thread.start()
p20_thread.start()
p21_thread.start()
p22_thread.start()
p23_thread.start()

p16_thread.join()
p17_thread.join()
p18_thread.join()
p19_thread.join()
p20_thread.join()
p21_thread.join()
p22_thread.join()
p23_thread.join()

print("All the processes has been finished executing.")