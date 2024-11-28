import threading
import subprocess

def run_script(script_name,argument):
   subprocess.run(["python3", script_name,str(argument)])

p44_thread = threading.Thread(target=run_script, args=("Planck_elliptical_multiprocess.py",44))
p88_thread = threading.Thread(target=run_script, args=("Planck_elliptical_multiprocess.py",88))
p118_thread = threading.Thread(target=run_script, args=("Planck_elliptical_multiprocess.py",118))
p126_thread = threading.Thread(target=run_script, args=("Planck_elliptical_multiprocess.py",126))
p137_thread = threading.Thread(target=run_script, args=("Planck_elliptical_multiprocess.py",137))
p148_thread = threading.Thread(target=run_script, args=("Planck_elliptical_multiprocess.py",148))
p161_thread = threading.Thread(target=run_script, args=("Planck_elliptical_multiprocess.py",161))
p163_thread = threading.Thread(target=run_script, args=("Planck_elliptical_multiprocess.py",163))
p167_thread = threading.Thread(target=run_script, args=("Planck_elliptical_multiprocess.py",167))
p186_thread = threading.Thread(target=run_script, args=("Planck_elliptical_multiprocess.py",186))
p187_thread = threading.Thread(target=run_script, args=("Planck_elliptical_multiprocess.py",187))
p211_thread = threading.Thread(target=run_script, args=("Planck_elliptical_multiprocess.py",211))

p44_thread.start()
p88_thread.start()
p118_thread.start()
p126_thread.start()
p137_thread.start()
p148_thread.start()
p161_thread.start()
p163_thread.start()
p167_thread.start()
p186_thread.start()
p187_thread.start()
p211_thread.start()

p44_thread.join()
p88_thread.join()
p118_thread.join()
p126_thread.join()
p137_thread.join()
p148_thread.join()
p161_thread.join()
p163_thread.join()
p167_thread.join()
p186_thread.join()
p187_thread.join()
p211_thread.join()

print("All the processes has been finished executing.")