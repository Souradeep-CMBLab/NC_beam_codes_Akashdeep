import threading
import subprocess

def run_script(script_name,argument):
   subprocess.run(["python3", script_name,str(argument)])

p315_thread = threading.Thread(target=run_script, args=("Planck_elliptical_multiprocess.py",315))
p316_thread = threading.Thread(target=run_script, args=("Planck_elliptical_multiprocess.py",316))
p317_thread = threading.Thread(target=run_script, args=("Planck_elliptical_multiprocess.py",317))
p318_thread = threading.Thread(target=run_script, args=("Planck_elliptical_multiprocess.py",318))
p337_thread = threading.Thread(target=run_script, args=("Planck_elliptical_multiprocess.py",337))
p338_thread = threading.Thread(target=run_script, args=("Planck_elliptical_multiprocess.py",338))
p347_thread = threading.Thread(target=run_script, args=("Planck_elliptical_multiprocess.py",347))
p361_thread = threading.Thread(target=run_script, args=("Planck_elliptical_multiprocess.py",361))

p315_thread.start()
p316_thread.start()
p317_thread.start()
p318_thread.start()
p337_thread.start()
p338_thread.start()
p347_thread.start()
p361_thread.start()

p315_thread.join()
p316_thread.join()
p317_thread.join()
p318_thread.join()
p337_thread.join()
p338_thread.join()
p347_thread.join()
p361_thread.join()

print("All the processes has been finished executing.")