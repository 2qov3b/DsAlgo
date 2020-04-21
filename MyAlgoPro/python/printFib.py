# Print out fibonacci's sequence up to 20.
# O(2^n) time / O(n) space
def fib1(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return fib1(n-2)+fib1(n-1)    

# O(n) time / O(n) space
def fib2(n, mem = {1:0, 2:1}):
    if n in mem:
        return mem[n]
    else:
        mem[n] = fib2(n - 1, mem) + fib2(n - 2, mem)
        return mem[n]    

# O(n) time / O(1) space
def fib3(n):
    lastTwo = [0, 1]
    counter = 3
    while counter <= n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter += 1
    return lastTwo[1] if n > 1 else lastTwo[0]     

#num = int(input("Enter an integer: "))
for i in range(1,101):
    print(fib3(i))        