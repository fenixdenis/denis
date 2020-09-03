import sys

def fibbonachi(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        print(n)
        return fibbonachi(n - 1) + fibbonachi(n - 2)
        print(n)

print(fibbonachi(25))