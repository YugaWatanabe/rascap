import subprocess
import time
import datetime

def cap():
    
    now = datetime.datetime.now()
    
    cmd = now.strftime('fswebcam -d /dev/video0 -D 2 -F 1 -S 10 /home/pi/Prog/capicture/%Y%m%d%H%M.jpg')
    r = subprocess.check_output(cmd, shell=True)
    
    time.sleep(10)
    
    return now.strftime('%Y%m%d%H%M.jpg')
    
#----------
if __name__ == '__main__':
    res = cap()
    print(res)