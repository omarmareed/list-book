# name: Omar Mareed ID: 215781386
# name: Ibraheem Amara ID: 215517673
from unicodedata import digit


### question 1 ###

def Xnor(a,b):
    if a == True and b == True:
        return True
    elif a == False and b == False:
        return True
    else:
        return False

### question 2 ###

def Digits(n):
    if n < 0 and n > 99999:
        print("maximum 5 digits")
        return
    if n < 10 and n%2 :
        print("one digit - even")
    elif n < 10 and n%2 == 1 :
        print("one digit - odd")
    elif n <100 and n//10 +n % 10%2==0:
        print("two digits - even")
    elif n <100 and n//10 +n % 10%2!=0:
        print("two digits - odd")
    elif n< 1000 and (n//100 +n % 10)%2==0:
        print("three digits - even")
    elif n<1000 and (n//100 +n % 10)%2!=0:
        print("three digits - odd")
    elif n<10000 and (n//100 +n // 10)%2!=0:
        print("four digits - odd")
    elif n<10000 and (n//100 +n // 10)%2==0:
        print("four digits - even")
    elif  n<100000 and (n//100)%2==0:
        print("five digits - even",)
    elif n<100000 and (n//100)%2!=0:
        print("five digits - odd")
    else:
        return "Error"

### question 3 ###

def GoodOrder(n):

    i = n % 10
    j = i % 2

    while n > 0:
        digit = n % 10
        if digit % 2 != j:
            return False
        n = n // 10

    return True

### question 4 ###

def Figure(n):
    for i in range(1,n):
        if i == 1:
            print(" "*(n-i) + str(i))
        else:
            print(" " * (n - i) + str(i) + " " * (2 * i - 3) + str(i))

    down = "".join(str(k) for k in range(n, 0, -1))
    up = "".join(str(k) for k in range(2, n + 1))
    print(down + up)

### question 5 ###

def count_digits(n):
    if n < 10:
        return 1
    else:
        return 1 + count_digits(n//10)

def max_digits(n):
    if n < 10:
        return n
    else:
        return max(n % 10,max_digits(n // 10))

def Weight(n):
    return count_digits(n) + max_digits(n)

### question 6 ###

def IsPrimary(n,i=2):
    if n <=1:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return IsPrimary(n,i + 1)

### question 7 ###
def Reduce(n):
    if n < 0 :
        return Reduce(-n)
    if n == 0:
        return 0

    i = n % 10
    j = Reduce(n//10)

    if i == 0:
        return j
    else:
        return j * 10 + i

### question 8 ###
def Pascal(n,m):
    if m > n or n < 0 or m < 0 :
        return -1
    if m == 0 or m == n:
        return 1
    return Pascal(n-1,m-1) + Pascal(n-1,m)







