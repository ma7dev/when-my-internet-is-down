import os
import time
from datetime import datetime
import platform

print(f'({datetime.now().strftime("%d/%m/%Y %H:%M:%S")}) Running when-my-internet-is-down...')
# set hostname to ping and file name to store data to
HOSTNAME = "google.com"
FILE_NAME = 'logs.txt'

cmd = ""
# set command
# windows
if platform.system().lower()=="windows":
    cmd = "ping -n 1 " + HOSTNAME + " > NUL"
# linux/mac
else:
    cmd = "ping -c 1 " + HOSTNAME + " > /dev/null"

start = -1
first_disconnect = ""
while True:
    # ping hostname
    response = os.system(cmd)

    # check if failed to ping first time
    if(response != 0 and start == -1):
        first_disconnect = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        start = time.time()

    # check if succeeded and failed before
    elif(response == 0 and start != -1):
        last_disconnect = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        seconds = round(time.time() - start)
        seconds = int(seconds)
        minutes=round((seconds/(60))%60)
        minutes = int(minutes)
        hours=round((seconds/(60*60)))
        output = f'First/Last Disconnect (difference): {first_disconnect} / {last_disconnect} ({hours}h:{minutes}m:{seconds}s)\n'
        print(output)
        with open(FILE_NAME, "a+") as logs_file:
            logs_file.write(output)
        start = -1

    time.sleep(1)
