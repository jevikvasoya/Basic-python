#list comphrehensoin
l = []
for i in range(100):
    if i%3==0:
        l.append(i)
print(l)

# l = [i for i in range(50) if i%3==0] #one line
# print(l)


#dict comphrehensoin
# dict = {i:f"item{i}" for i in range(0,10)}
# print(dict)

# set comphrehensoin
# s = {n for n in [1,2,3,2,3,4,1,1]}
# print(s)

# generator comphrehensoin
# evens = (i for i in range(10) if i%2==0)

# for items in evens:
#     print(items)