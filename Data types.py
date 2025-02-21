# integer
a = 5
print(a)
print(type(a))

# string
a = 5.5
print(a,type(a))

# complex
b = 2+3j
print(b, type(b))

# string
c = "hello@123"
print(c,type(c))

s = '''
    hello world
'''
print(s,type(s))


#List (mutable)
l =[1,"hw,",8.9]
l[1]="world"
print(l,type(l))


# tuple (immutable)
t = (10,20.9,"hello")  
print(t,type(t))

#dictionry 
d = {"name": "sachin",
     "age":20,
     "city":"jaipur"}
print(d,type(d))
print(d["age"])

#set 
s = {10,20,30,10}
print(s,type(s))