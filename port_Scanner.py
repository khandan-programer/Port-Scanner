from socket import *

import os

from datetime import datetime

from colorama import init, AnsiToWin32, Fore, Back

import sys

init(wrap=False)

stream = AnsiToWin32(sys.stderr).stream

print("")

print(Fore.RED, '''
_____           _      _____                                 
|  __ \         | |    / ____|                                
| |__) |__  _ __| |_  | (___   ___ __ _ _ __  _ __   ___ _ __ 
|  ___/ _ \| '__| __|  \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
| |  | (_) | |  | |_   ____) | (_| (_| | | | | | | |  __/ |   
|_|   \___/|_|   \__| |_____/ \___\__,_|_| |_|_| |_|\___|_|        ''', file=stream)         
                                                             

print (Fore.RESET,  " ", file=stream)

get = input("Enter a url : ")

print ("")

target = gethostbyname(get)

print ("Scan Started => %s" %target)

t1 = datetime.now()

print("")

for i in range(1 , 9000):

    s = socket(AF_INET , SOCK_STREAM)

    result = s.connect_ex((target, i))

    if (result == 0):

        print ("Port %d: Open" %(i, ))
        t2 = datetime.now()
        t3 = t2-t1
        #t1 = datetime.now()
        s.close

print ("")
print("Scan Finished in : ",t3)
