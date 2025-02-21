# for i in range(1,6):
#     print(i ** 2, end=" ")


# for j in range(1,11):
#     if j%2 == 0:
#         print(j, end=" ")

# total = 0
# for i in range(1,11):
#     total += i
# print(total)


# word ="helloworld"
# for i in range(len(word) -1, -1, -1):
#     print(word[i], end = " ")


# vowels = 'aeiou'
# word = " enginering"
# count = 0

# for char in word:
#     if char in vowels:
#         count +=1
# print(count)

# fibonacci
# a=0
# b=1
# print(a,b, end=" ")

# for i in range(10):
#     next_term = a+b
#     print(next_term, end =" ")
#     a,b = b, next_term


# factorial
# n= 5
# factorial = 1
# for i in range(1, n+1):
#     factorial *= i
# print(factorial)


# prime check
# n = int(input("enter the number: "))
# if n%2 == 0:
#     print("not prime")
# else:
#     print("prime")

# word = "programing"
# char_count = {}

# for char in word:
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1
# for char, count in char_count.items():
#     print(char + ':', count )


# vowels = 'aeiou'
# word = " enginering"
# count = 0

# for char in word:
#     if char in vowels:
#         count +=1
# print(count)

count = {}
word = "seamless"
for i in word:
    if i in count:
        count[i] += 1
    else:
         count[i] = 1
for i, count in count.items():
    print(i + ':', count )
