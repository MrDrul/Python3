import subprocess
#int = 1,2,3,-4,-5  Baic 2.6 no

#float = 1.0,2.3,3.5,-4.7 baic 1 no

#str = "Hello" 'Hi' '34'

#list = [1, 1, 3, 4, "hello"]

#dict = {"a":"b", "negr":"+1324"} a-n banali b znachenie

#tuple = same us list but you cant change it after adding

#set = {"a", "b" "a"no} chi karogh krknvel

#bool = True, False




#Simple Math


#Gumarum
print(3 + 2)

print(3.5 + 6.5)

print(-4 + 5)

print(5 + -6)


#Hanum
print(2 - 3)

print(3 - 2)

print(-3 - 5)

print(4 - -2)

print(4.5 - 3.5)


#Bajanum (always brings back float)
print(3/3)

print(6/10)


#Bazmapatkum
print(3*8)


#% mnacort
print(4%4)

print(6%4)


# round() kloracnuma
print(1.2354 * 8)

print(round(1.2354*8, 3))

print(round(1.2354*8, 2))

print(round(1.2354*8))

#Variables

a = "negr"
b = float(89)

print(type(a))
print(type(b))

'''
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
'''

#Python allows you to assign values to multiple variables in one line:

x, y, z = "Orange", 4, 7.9
print(x)
print(y)
print(z)

#And you can assign the same value to multiple variables in one line:

d = f = g = 12
print(d)
print(f)
print(g)

#If you have a collection of values in a list, tuple etc. Python allows you extract the values into variables. This is called unpacking
#Bajanuma variablneri mech
mrger = ["xndor", "tand", "cherry"]
X, Y, Z = mrger
print(X)
print(Y)
print(Z)

# +

aw = "meh hrashq"
print("Python = " + aw)

#kam

_1 = "Python qunem"
_2 = "boz berant"
_3 = _1 + _2
print(_3)

#functions


Aghas = "simpo tgha"#Global variable sagh karan ogtagorten

def first_func():
  Aghas = "negr tgha"#function variable menka tvial funkcian kara ogtagorti
  global negr #Make variable global
  negr = "aghas tgha"
  print(Aghas)

first_func()

print(Aghas)
print(negr)

