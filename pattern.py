import math

a = 3
b = 0

i = 1

while(i<=5):
    j = 1
    while(j<=i+a):
        print(" ",end="")
        j = j+1

    j = 1
    while(j<=i+b):
        print("*",end="")
        j = j+1

    print()
    i = i+1
    a = a-2
    b = b+1


    
a = 0
b = 6

i = 1

while(i<=4):
    j = 1
    while(j<=i+a):
        print(" ",end="")
        j = j+1

    j = 1
    while(j<=i+b):
        print("*",end="")
        j = j+1

    print()
    i = i+1
    b = b-3
