import random


a=random.randrange(20)
print(a) #Gnerete any interger value between the paramenters

b=random.random()
print(b) #Gnerete any floating value between the paramenters


c= random.randint(2,6)
print(c) #Gnerete any interger value between the paramenters

d=random.uniform(2,6)
print(d) # Gnerete any floating value between the paramenters


e=["c","python","cpp","php","java"]
print(random.choice(e)) # Will give any random name or value
print(random.choice("PYTHON")) # Will return any  random character of any position

f=["c","python","cpp","php","java"]
print(random.shuffle(f))  # shuffle the order of the list

