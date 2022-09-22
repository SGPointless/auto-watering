# Probierwiese
hallo=input("Bock?")
Data = []
Data.append(1)
Data.append(2)
Data.append(3)
print(Data[2])

for x in Data:
    print(x)

number = 11 * 3 + 2 / 4
Modulo = 11 % 3
ImQuadrat = 2 ** 2
helloworld = "hello" + " " + "world"
lotsofhellos = "hello" * 10

print([1, 2, 3] * 3)
print("Ergebnis %d" % number)
print("Ergebnis %d und %d" % (Modulo, ImQuadrat))

mylist = [1, 2, 3]
print("A list: %s" % mylist)
# %d for integers %f for floats %s for strings


# String Stuff
astring = "Hello world!"
print("single quotes are ' '")
print(len(astring))

astring = "Hello world!"
print(astring.index("o"))

astring = "Hello world!"
print(astring.count("l"))

astring = "Hello world!"
print(astring[3:7])

astring = "Hello world!"
print(astring[3:7:2])

astring = "Hello world!"
print(astring[3:7])
print(astring[3:7:1])

# Conditions

x = 2
print(x == 2)  # prints out True
print(x == 3)  # prints out False
print(x < 3)  # prints out True

name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif another_statement is True:  # else if
    # do something else
    pass
else:
    # do another thing
    pass
ende=input("Bitte Taste drücken...")
