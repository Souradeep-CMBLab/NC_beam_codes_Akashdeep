import threading
import subprocess

def run_script(script_name,argument):
   subprocess.run(["python3", script_name,str(argument)])

p213_thread = threading.Thread(target=run_script, args=("Planck_elliptical_multiprocess.py",213))
p217_thread = threading.Thread(target=run_script, args=("Planck_elliptical_multiprocess.py",217))
p230_thread = threading.Thread(target=run_script, args=("Planck_elliptical_multiprocess.py",230))
p237_thread = threading.Thread(target=run_script, args=("Planck_elliptical_multiprocess.py",237))
p239_thread = threading.Thread(target=run_script, args=("Planck_elliptical_multiprocess.py",239))
p244_thread = threading.Thread(target=run_script, args=("Planck_elliptical_multiprocess.py",244))
p245_thread = threading.Thread(target=run_script, args=("Planck_elliptical_multiprocess.py",245))
p251_thread = threading.Thread(target=run_script, args=("Planck_elliptical_multiprocess.py",251))
p264_thread = threading.Thread(target=run_script, args=("Planck_elliptical_multiprocess.py",264))
p296_thread = threading.Thread(target=run_script, args=("Planck_elliptical_multiprocess.py",296))
p308_thread = threading.Thread(target=run_script, args=("Planck_elliptical_multiprocess.py",308))
p314_thread = threading.Thread(target=run_script, args=("Planck_elliptical_multiprocess.py",314))

p213_thread.start()
p217_thread.start()
p230_thread.start()
p237_thread.start()
p239_thread.start()
p244_thread.start()
p245_thread.start()
p251_thread.start()
p264_thread.start()
p296_thread.start()
p308_thread.start()
p314_thread.start()

p213_thread.join()
p217_thread.join()
p230_thread.join()
p237_thread.join()
p239_thread.join()
p244_thread.join()
p245_thread.join()
p251_thread.join()
p264_thread.join()
p296_thread.join()
p308_thread.join()
p314_thread.join()

print("All the processes has been finished executing.")