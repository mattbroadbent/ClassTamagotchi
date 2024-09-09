from threading import Timer
import os

iteration = int(0)

def tryThis():
    t = Timer(1.0, tryThis)
    t.start()
    
    global iteration
    iteration += 1
    #print(iteration)

t = Timer(1.0, tryThis)
t.start()

##################################

value = input("enter something. ")

while value:
    os.system('cls')
    print(iteration)
    value = input("enter something. ")