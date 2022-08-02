from multiprocessing import Process
import os
import speedtest
from time import sleep
from threading import *

def screen_clear():
    #print("CLEAR")
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system("clear")
    else:
        # for windows platfrom
        _ = os.system('cls')

rocket = 0

def speed_check():
    speed_network = speedtest.Speedtest()
    #print("     Calculating Download speed......\n")
    print("     Download speed : " + str(round((speed_network.download() / 1024 / 1024), 2)) + " Mb/s                   \n")
    print("     Upload speed : " + str(round((speed_network.upload() / 1024 / 1024), 2)) + " Mb/s                       \n")
    print("                                                                  ")
    global rocket
    rocket = 1


def loading_animation():
    # print("Hai")
    animation = [
        "        ",
        "█       ",
        "  █     ",
        "   █    ",
        "    █   ",
        "     █  ",
        "      █ ",
        "       █",
        "      █ ",
        "     █  ",
        "    █   ",
        "   █    ",
        "  █     ",
        " █      ",
        "█       ",
        "        ",
        "        ", #extended
        "█       ",
        "  █     ",
        "   █    ",
        "    █   ",
        "     █  ",
        "      █ ",
        "       █",
        "      █ ",
        "     █  ",
        "    █   ",
        "   █    ",
        "  █     ",
        " █      ",
        "█       ",

    ]
    i = 0
    global rocket
    while True:
        print(("        Please wait.Acquiring speed"+str(animation[i % len(animation)])), end='\r')
        sleep(0.05)
        i += 1
        if rocket == 1:
            break

screen_clear()
print("\n")
print("                                         INTERNET SPEED TEST")
print("-----------------------------------------------------------------------------------------------------------")
print("\n\n")

if __name__=='__main__':
    t1 = Thread(target = speed_check)
    t1.start()
    t2 = Thread(target = loading_animation)
    t2.start()

    t1.join()
    t2.join()

#print("Rocket : "+str(rocket))

print("\n")
k = input("Print Enter key to Exit")
