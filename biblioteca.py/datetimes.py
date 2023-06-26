'''import datetime

print(datetime.date.today())

print(datetime.date.today().strftime('%d/%m/%Y'))
print(datetime.datetime.now())
import os
while True:

 print(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
 os.system("cls")'''
import time
a=0
x=time.perf_counter()
while a <10000:
  print(a)
  a+=1
y= time.perf_counter()
print(y-x)