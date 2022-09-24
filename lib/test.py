import os
import time

for i in range(5):
    for j in range(5):
        print("'",end=" ")
    print("")


time.sleep(2)
index = [[2,4],[3,4],[4,4]]

os.system("cls")

for i in range(5):
    for j in range(5):
        if [i,j] in index:
            print("0",end=" ")
        else:
            print("'",end=" ")
    print("")
    

time.sleep(2)

index2 = [[1,0],[2,1],[4,2]]

os.system("cls")

for i in range(5):
    for j in range(5):
        if [i,j] in index2:
            print("X",end=" ")
        elif [i,j] in index:
            print("0",end=" ")
        else:
            print("'",end=" ")
    print("")