for i in range(1,6):
    for j in range(1,6):
        print("*", end=" ")
    print() #empty

print("----------------------")

r =5
for i in range(1, r+1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()

print("----------------------")

n =5
for i in range(n,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()

print("----------------------")
 
x= 6
for i in range(1,6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

print("----------------------")

a = 5
for i in range(a, 0, -1):
    for j in range(i,0,-1):
        print(j, end=" ")
    print()

print("----------------------")

#1
#22
#333
#4444

n =5
for i in range(1,5):
    for j in range(i):
        print(i, end=" ")
    print()