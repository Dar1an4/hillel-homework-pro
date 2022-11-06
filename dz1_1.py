#!/usr/bin/python3
import random
import subprocess
from datetime import datetime


whoami = subprocess.run('whoami')
pwd = subprocess.run(['pwd', ])
print(f'Username is: {whoami = }')
print(f'PWD (current dir) is: {pwd = }')


subprocess.run('mkdir dz1', shell=True)
print('directory with name dz1 was created')


command_list = ['touch']
filenames_list = ['./dz1/' + f'{("0" + str(i))[-2:3]}' + f'{datetime.now().strftime("-%m-%Y")}.log' for i in range(1, 31)]
command_list.extend(filenames_list)
subprocess.run(command_list)
print(f'nn-{datetime.now().strftime("-%m-%Y")}.log files in dir dz1 was created')


subprocess.run('sudo chown -R root ./dz1', shell=True)
print(f'owner was changed.')


ls_files = subprocess.run(['ls', 'dz1'], capture_output=True, text=True)
files_list = ls_files.stdout.split('\n')
files_list.remove('')
del_com = ['rm']
random_fnames = ['./dz1/' + random.choice(files_list) for i in range(5)]
del_com.extend(random_fnames)
print(del_com)
subprocess.run(del_com)
print('5 random files was deleted successfully')
