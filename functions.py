# def sum(a,b):
#     c = a+b
#     print(c)
# sum(5,5)

# def multi(c,d):
#     x = c*d
#     return x
# y = multi(5,5)
# print(y)

#local and global variables
def cal(a,b):
    a = 5  #local variable
    b = 6
    c = a*b
    return c

x = cal(5,10)
print(x)

# even odd using function
# def odd_even():
#     n = int(input("enter a number:"))
#     if n%2 == 0:
#         print("even")
#     else:
#         print("odd")
#     print(n)

# odd_even()


def lines():
    line = int(input("enter number of lines:"))
    for i in range(1, line+1):
        for j in range(i):
            print("*", end=" ")
        print()
    
    print(line)
lines()


#squre of a number
# def sqr(number):
#     print(number**2)
# sqr(5)

# def mul(p1,p2):
#     print(p1*p2)
# mul(3,"a")


# def circle(radius):
#     print(3.14*radius**2)

# circle(2)


#greet
# def greet(name):
#     return "hello," + name +" good morning"
# print(greet("samay"))

#args

# def sum_all(*args):
#     print(args)
#     return sum(args)

# print(sum_all(1,2))
# print(sum_all(2,3,4))

#recursive
# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n * fact(n-1)
    
# print(fact(5))

