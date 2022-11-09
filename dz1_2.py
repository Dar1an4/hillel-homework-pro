#!/usr/bin/python3
import subprocess


subprocess.run('cp dz1_1.py dz1_run.py', shell=True)
print('File successfully duplicated')

subprocess.run('chmod u+x dz1_run.py', shell=True)
print('access for bash run successfully created')

subprocess.run('chmod u=rx,g=,o= dz1_run.py', shell=True)
print('access successfully changed')

subprocess.call('./dz1_run.py', shell=True)
print('script dz1_run.py successfully finished')
