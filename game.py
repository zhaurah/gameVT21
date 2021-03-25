import os

def runtestcode(l):
    print("-"*20)
    for e in l:
        print(e)
    print("-"*20)

runtestcode([5, 3, 2, 4, 1, 7, 9])
input()
os.system('cls' if os.name == 'nt' else 'clear')
runtestcode([5])
input()
os.system('cls' if os.name == 'nt' else 'clear')