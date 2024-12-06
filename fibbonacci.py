n=int (input ("enter the nth term: "))
def fibbonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibbonacci(n-1) + fibbonacci(n-2)

print(fibbonacci(n))