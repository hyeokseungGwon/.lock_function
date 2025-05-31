## "isfile" vs "listdir(dir)" Method difference
#(1) isfile means checking the route and file
#(2) listdir(dir) means scan and brings a list at once

##The way How to know this file(* means variable mark)
#1) Time transfer
#1-1) Replacing Method
#2) for & While Method
#3) isfile Method >> Accurately exist file in the route
#3-1) listdir method >> Accurately in route
#*) The letter 'small' is a related to path or time
#*) The Capital letters are related to syntax
#----------------------------------------------------------
import os
from datetime import datetime
import time

path='/user/cso/hsgwon/Desktop/practice/.lock_function/data/tasks/1/.lock'#until .lock >> Reference 3)
now = datetime.now()

#1)Time transfer
a = now.strftime("%Y-%m-%d %H:%M:%S")
#1-1)Replacing method
b = datetime.now()
c = now.replace(microsecond=0)
#route self can be a variability
exists = os.path.isfile(path)

##if syntax(.lock exists)&using (a)
# if os.path.isfile(path):
#     print(f".lock exists.{a}")
# else:
#     print(f".lock does not exist.{a}")

## #os path setting
# if exists:
#     print(".lock exist")
# else:
#     print(".lock doesn't exist")

##Operating possible code(using if)/But this code is not important. Because the While syntax has a if grammar
if os.path.isfile(path):
    print(f".lock exists.{c}")
else:
    print(f".lock does not exist.{c}")

# #os path setting
# if exists:
#     print(".lock exist")
# else:
#     print(".lock doesn't exist")


#------------------<Syntax study Area>-------------------------
## for syntax is impossible
## A) for var in route >> route is a result about True or False
## True or false means it is not a repeatable object.
### A) if os.path.isfile(path):
    # for A in os.path.isfile(path): >> Error
        # print(f"[Syntax Area].lock exist{c}")
    # else :
        # print(f"[Syntax Area].lock doesn't exist{c}")

##while and for syntax difference
##For syntax means continuous object can apply,
##but, os.path.isfile means does file exist? answer is yes or no.
##so,the other way is 'if condition'

##[For Syntax]
# exists_on_another_way = os.path.isfile(".lock")
# for A in exists_on_another_way:
#     exist = os.path.isfile(path)
#     if exist:
#         print(f"{A} exists")
#     else:
#         print(f"{A} doesn't exist")
## Means Type Error. Because "isfile" is a situation to check file does exist, so, if you run this script, answer is a "TypeError:'bool' object is not iterable"

##[While Syntax]
#while condition:
# running code
## If you wanna use "time.sleep", you have to "import time" in this file.

##Operating code (using isfile)
# while (True):
#     if os.path.isfile(path):
#         print(f"[while&if condition] Syntax: .lock exists: {c}")
#         time.sleep(1)
#     else:
#         print(f"[while& if condition] Syntax: .lock not found: {c}")
#         break

#Operating code (using listdir)
listdir_path = '/user/cso/hsgwon/Desktop/practice/.lock_function/data/tasks/1'
while (True):
    if ".lock" in os.listdir(listdir_path):
        print(f"[ListDir method]:.lock exists : {c}")
    else:
        print(f"ListDir method]:.lock not found: {c}")
        break