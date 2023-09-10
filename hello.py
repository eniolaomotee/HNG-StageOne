# meaning = 42
# print('')

# # if meaning > 10 :
# #     print('Right on')
# # else: 
# #     print('Not today')

# print('Right on') if meaning > 10 else print('Not today')

##String Dats types in python
#Literal assignment

first = "Dave"
last = "Gray"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))


##Constructor Function
# pizza = str('Pepperoni')
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))



##Conactenation
fullname = first + " " + last 
print(fullname)

fullname += "!"
print(fullname)

#Casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)


statement = "I like rock music from the " + decade + "s."

print(type(statement))

##Multiple Lines
multiline = '''
Hey, how are you?

I was just checking in.  
                                All good?

'''

print(multiline)

# Escaping Special characters
sentence = 'I \'m back at work!\tHey!\n\nWhere\'s this at\\located?'

print(sentence) 

##String Methods
print(first)
print(first.lower())
print(first.upper())
print(first)


print(multiline.title())
print(multiline.replace("good","ok"))
print(multiline)

print(len(multiline))
multiline += "                                                "
multiline= "     " + multiline
print(len(multiline))

# String method to remove white space
print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print(" ")
print(" ")


# Build a menu
title ="Menu".upper()
print(title.center(29, '='))
print("Coffee".ljust(24,".") + "$1".rjust(4))
print("Muffin".ljust(24,".") + "$2".rjust(4))
print("CheeseCake".ljust(24,".") + "$4".rjust(4))

print(" ");

# String Index Valiues
print(first[0])
print(first[1])
print(first[-1])
print(first[0:-1])
print(first[1:])

# Some Methods that return boolean data
print(" ")

print(first.startswith('D'))
print(first.endswith('Z'))

#Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))      


# Numeric DT
# integer type
num = 1
mynum = int(30)
print(type(num))
print(isinstance(mynum, int))
print(mynum)

# Float 
value = 2.0
myvalue = float(40)

print(myvalue)
print(isinstance(myvalue, float))
print(type(value))