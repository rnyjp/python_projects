import urllib.request
import datetime
from time import sleep
import os

def screen_clear():
    #print("CLEAR")
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system("clear")
    else:
        # for windows platfrom
        _ = os.system('cls')

def conection_check():
    host = 'http://google.com'
    try:
        urllib.request.urlopen(host)
        return 1
    except:
        return 0

flag = 0
count_no_connection = 0
switch_position = 0

while True:

    print("\n")
    present_time = datetime.datetime.now().time()
    end_time = datetime.time(11, 18, 0)
    print_time = present_time.strftime("%H:%M:%S")

    host = 'http://google.com'
    try:
        urllib.request.urlopen(host)
        print("     Internet connection status : CONNECTED. at "+str(print_time))
        switch_position = 0
    except:
        print('\a')
        switch_position += 1
        print("     Internet connection status : DISCONNECTED !! at " + str(print_time))

    if switch_position == 1:
        count_no_connection += 1
    else:
        count_no_connection = count_no_connection

    print("\n     Number of times internet connection got disconnected : " + str(count_no_connection) + "\n")

    sleep(3)
    screen_clear()

#-----------------------------------------------------------------------------
