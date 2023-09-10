# List holds multiple values in python then you can also reverse them
# You can use (-1) to know the last element of a list
# Lists and Tuples


users = ['Dave','John','Sara']

data = ['Dave',42,True]

emptylist= []


# Check the value is in a list
print("Dave" in emptylist)

# Check the position
print(users[0])
print(users[-1])

# Postiton of a specific Value
print(users.index("Sara"))

# Get a range of value
print(users[0:2])
# Only output the values from the 0 position to the 1 position

# Get elements from the first position till the end of the list
print(users[1:])

print(users[-3:-1])

print(" ")
print(" ")
print(len(users))