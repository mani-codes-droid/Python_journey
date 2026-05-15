#que
def calc_sum(a , b): #functional statement; parameters
    sum = a + b
    print(sum)
    return sum 
 
calc_sum(3,4) #function call; argument
calc_sum(8,9)

#que
def calc_sum(a , b): 
    return a + b
sum = calc_sum(178 , 897)
print(sum)

#que
def prt_hello():
    print("Hello")

prt_hello()
prt_hello()
prt_hello()
prt_hello()

#average of 3 numbers
def calc_avg(a, b, c):
    avg= (a + b + c)/3
    print(avg)
    return avg

calc_avg(2,7,3)

#que
def calc_mul(a ,b=9):
    mul= a*b
    print(mul)
    return mul

calc_mul(1)

#que
heroes = ["superman", "batsman", "spiderman"]
def prt_len(heroes):
    print(len(heroes))
    return prt_len
prt_len(heroes)

#que
def prt_element(heroes):
    for i in heroes:
        print(i, end= " ")
prt_element(heroes)

#que
def calc_fact(n):
    fact=1
    for i in range(1,n+1):
         fact *= i
    print(fact)
calc_fact(5)
calc_fact(7)

#que
def cal_INR(USD):
    INR= USD*83
    print(USD, "USD =", INR, "INR")
    return cal_INR

cal_INR(100)
cal_INR(4)

#que
n = int(input("Enter Number: "))
def check(n):
    if (n%2==0):
        print(n,"is EVEN number")
    else:
        print(n,"is ODD number")

check(n)

#que
def show(n):
    if (n==0):
        return
    print(n)
    show(n-1)
    print("LOOP ended")

show(9)

#que 
def fact(n):
    if (n==1 or n==0):
        return 1
    else:
        return n * fact(n-1)
    
print(fact(5))

#que
def sum(n):
    if (n==0):
        return 0
    else:
        return n + sum(n-1)
    
print(sum(5))

#que
def prt_element(list, idx):
    if (idx == len(list)):
        return
    print(list[idx])
    prt_element(list,idx+1)
    
heroes= ["superman", "spiderman", "krish"]
prt_element(heroes, 0)

