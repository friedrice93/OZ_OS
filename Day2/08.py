# 내 파이썬 프로그램의 이름을 알아보자.

import psutil
import os

if __name__ == '__main__' :
    print('08.py 프로세스 아이디:', os.getpid())

for proc in psutil.process_iter() :
  ps_name = proc.name()
  
  if "Python" in ps_name :
    print(ps_name, proc.pid)

