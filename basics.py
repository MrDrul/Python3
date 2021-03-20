import random

#int = 1,2,3,-4,-5  Baic 2.6 no

#float = 1.0,2.3,3.5,-4.7 baic 1 no

#str = "Hello" 'Hi' '34'

#dict = {"a":"b", "negr":"+1324"} a-n banali b znachenie


#set = {"a", "b" "a"no} chi karogh krknvel

#frozenset nuin set ughaki anpopox

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

print(9 // 2)#Bajanum kloracum ov


#Bazmapatkum
print(3*8)
print(2 ** 5)#qarakusina -> 2*2*2*2*2


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
puc = 1

def first_func():
  Aghas = "negr tgha"#function variable menka tvial funkcian kara ogtagorti
  global negr, puc #Make variable global
  puc = 2#darnuma global u poxuma arajini arjeqy
  negr = "aghas tgha"
  print(Aghas)

first_func()

print(Aghas)
print(negr)
print(puc)

#random
print(random.randrange(1, 10))#random tiv 1ic 10 (pti import random anes)

#len()
str_1 = "01234"
str_2 = "12345"
print(len(str_1))#tareri qanak
print(str_2[3])#hasvel 0 ic!!!

#in
txt = "Barev Aghasi qunem boz berant"
print("Aghasi" in txt)#ete ka True ete che False

tzt = "Barev Garniik qunem boz berant"
print("Aghasi" not in tzt)#chka et bary True ka Flase

#a[a:f]
Slicing = " Barev EZ "
print(Slicing[2:7])#Hashvel 0c -> rev E   7 is not included
print(Slicing[:7])#skzbic minchev 7rd teghy 7y chnerarial
print(Slicing[2:])#2ic minchev verch
print(Slicing[-5:-2])#hetevica hashvum


#\


print("They called me \"super Nigga\" how was that??")
print("They called me \bsuper Nigga how was that??")#backspace
print("They called me\tsuper Nigga how was that??")#4hat space
print("They called me \\super Nigga\\ how was that??")#\\ teqsti mech havasara \
print("They called me \nsuper Nigga how was that??")#nor togh linux and mac os
print("They called me \rsuper Nigga how was that??")#nor togh windows


#format()
tariq = 97
boi = 1.93
havai = 123
Anun = "Aghasi {1} tarekan Hors asrev hly sra {0} boiy naeq"
print(Anun.format(boi, tariq))#{} sranc teghy tariqna dnelu!!
#{:<x} achic x qanakutyamb prabel
#{:>x} daxic x qanakutyamb prabel
#{:^x} erku yanic x/2 qanakutyamb prabel
#{:>x} y tvi meshteghic x qanakutyamb prabel
#{:+}  positive tvei demy +a dnum
#{:-}  minusov tverna qtnum
#{: }  pozitiv tveri demy prabel
#{:,}  orinak x = 1000000 = 1,000,000
#{:_}  orinak x = 1000000 = 1_000_000
#{:b}  binary system
#{:d}  binary system sovorakan
#{:e}  to convert a number into scientific number format (with a lower-case e):
#{:E}  to convert a number into scientific number format (with a upper-case E):
#{:0}  8akan system
#{:f}  16akan hamakarg
#{:%}  %a sarqum
#{:c}  Converts the value into the corresponding unicode character
#{:g}  General format
#{:G}  General format (using upper-case E for science)
#{:n}  Number format

#String methods
Lorem = "Lorem IPSUM dolor sit amet, consectetur adipiscing eli"
lorem = "lorem IPSUM dolor sit amet, consectetur adipiscing eli?"
tab = "p\tu\tc q\tu\tn\te\ts\t????"
splitlines = "Fuck\nyou\nnigga"

print(splitlines.splitlines())#sarquma list

print(lorem.capitalize())#arajin tary metatar

print(Lorem.swapcase())#metatary sarquma poqr. poqr. metatar

print(Slicing.upper())#sagh metatar

print(Slicing.lower())#sagh poqratar

print(Slicing.strip())#rstrip()   skzbi u verchi bacatnery hanuma

print(Slicing.split("e"))#texty kisuma nshatt teghic

print(Slicing.rsplit("e"))#sarquma list str-n

print(Slicing.replace("Barev", "Hajogh"))#yntratt poxuma go gratov(Hajogh)

print(Lorem.casefold())#lower ultimate edition

print(Lorem.center(10))#erku komic space qo nshat qanakov

print(lorem.count("lorem", 0, 5))#hashvuma textum es baric qani hat ka 0start 5end of search positions

#.encode()  UTF-8 encode the string:

print(lorem.endswith("?"))#stuguma qo tvat nshanova prte texty te che
print(lorem.startswith("?"))#stuguma qo tvat nshanova skseum texty te che

print(tab.expandtabs(10))#tabi chaps (probelneri qanak)

print(Lorem.rfind("dol", 1, 30))#nuin find hetevica hashvum

print(Lorem.rindex("dol", 1, 30))#nuin index hetevica hashvum

print(Lorem.find("dol", 1, 30))#inch paziciauma gtnvum nshatt tvov

print(Lorem.index("dol", 1, 30))#nuin find na prosty ete chi qtnum errora tali (finy -1a tali)

print(lorem.title())#luboi bari 1in tary Upercase

Pokem = "mPkoe"
boxk = "mLroe"
mytable = Lorem.maketrans(boxk, Pokem)#tegherov poxuma
print(Lorem.translate(mytable))

print(Lorem.zfill(100))#0nera avelcnum minchev opshi qon nshat tivy chilinium

print(Lorem.isalnum())# Sagh tar u tiv en te che Example of characters that are not alphanumeric: (space)!#%&? etc.
print("negr2228".isalnum())#True a galu vereviny False

print(Lorem.isalpha())#Sagh taren te che
print("negr".isalnum())#True a galu vereviny False

print(Lorem.isdigit()) #sagh tiven te che Example of characters that are not alphanumeric: (space)!#%&? etc.
print("2228".isdigit())#True a galu vereviny False

print(Lorem.isidentifier())#A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.
print("Aghas_gangster_5498".isidentifier())#True a galu vereviny False

print(Lorem.islower())#sagh poqratar en te che
print("dfghjk324".islower()) #True a galu vereviny False

print(Lorem.isupper())#sagh metatar en te che

isnum = "4560978"
print(isnum.isnumeric())#kotorak qarakusi kam 0-9   -> -3 kam 1.5 false

print(Lorem.isprintable())#stuguma pritabl a te che

print(lorem.isspace())#sagh prabel en te che

print(Lorem.istitle())#stuguma te sagh barei 1in tarery metatar en u mnacaty poqratar

Tuple = ("qunem", "vort", "boz")
print("_".join(Tuple))#miacnuma tupli mechiny qo drat znakov

print(Pokem.ljust(20, "#"), Lorem)#achic prabelner kam qo drat nshany(#) qo nshat tvov(20) karas gres rjust(daxic kani)

print(Lorem.lstrip("sitdol"))#texti dax masum inshqan gerakshrogh zibil ka qo nshat siktira anum nuiny achic rstrip

poqr = "I clould eat bananas all day"

print(poqr.partition("bananas"))#qtnuma gratt 3bajinanoc tupla sarqum 1.minchev bary 2.bary 3.baric heto
#r.patrition() hetevica hashvum

print(isinstance("qwerty", int))#stuguma tvatt konkrent type i a te che -> Flase

#Booleans

print(10 > 9)#True
print(10 == 9)#False
print(10 < 9)#False

Iphone = 300
Seven_Plus = 76

if Seven_Plus > Iphone:
	print("7PLus@ meta")
else:
	print("Iphone meta")
print(bool("nigga"))#True ete datarka False
print(bool(234))#True ete datarka False

#False orinakner
'''
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({}) 
'''
#operation types
OP = 6

OP += 3 #OP + 3

OP -= 3 #OP - 3

OP *= 3 #OP * 3

OP /= 3 #OP /3

OP %= 3 #OP % 3

OP //= 3 #OP // 3

OP **= 3 #OP ** 3

'''
== Havasar
!= Havasar che
> met
< Poqr
>= Met kam havasar
<= poqr kam havasar
'''
print(not(7 > 3 and 7 < 10))#Flase vortev not ka atasxany shrjuma isk sovorakan True

print(10 > 4 or 4 < 10)#True vortev gone meky tishta

Is = ["apples", "bananas"]
Love = ["apples", "bananas"]
Si =Is

print(Is is Love)#True nuin obiektnen
print(Is is Si)#False vortev irar havasar en baic tarber obiektneren
print(Is == Si)#True vortev irar havasar en


#List

#list = [1, 1, 3, 4, "hello"]

#how to change whats in the list

w3 = ["apple", 67, True]
print(w3)
w3[1] = False #poxel 67-y Falsov
print(w3)
w3[1:2] = [True, "super"]#Fasle poxharinum es True superov
print(w3)
w3[1:3] = [69]#2haty poxharinum es mihatov
print(w3)
w3.insert(3, "Chines like a melody")#(vode avelcni, inch avelcni)
print(w3)
w3.append("riders")#avelcnuma verchic
print(w3)
w4 = ["apple", 865, False]
w3.extend(w4)#listery kpcnuma irar
print(w3)
w3.remove(69)#jnjuma listic
print(w3)
w3.pop(3)#nuin jnjely baic indexov ete ches nshum verchinna jnjum
print(w3)
del w3[0]#eli jnjuma ete [n-tiv] chgres sagh kjnji
print(w3)
#w3.clear() maqruma listy
for w5 in w3:
	print(w5)#sagh listy arandin tpuma

fruits = ["xndor", "tand", "hndkakan pnduk", "abelsin", "Ananas"]
newlist = []

for k in fruits:
	if "a" in k:
		newlist.append(k)

print(newlist)#a ov sksvogh banery qcuma qo listy

newlist.sort()#yst hertakanutyaba hasavorum ex ` 6,3,2,9,4 -> 2,3,4,6,9    b,a,d,c -> a,b,c,d
#sort(reverse = True) hakaraka dasavorum
print(newlist)

newlist.sort(key = str.lower)#sort by deafoult is writing upppercase first with this we can fix it

'''
#you can copy the list bc list1 = list2 is wrong cause any changes made to list1  automaticaly are made in list2
1 metod to copy list is`

list2 = list1.copy()

2nd method`

list2 = list(list1)

!!!Connct list by `
list3 = list1 + list2
'''



#Tuples

#tuple = same us list but you cant change it after adding

thistuple1 = ("apple",)
print(type(thistuple1))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple)) 

#thistuple1 = tuple(12, "asd", True)#this is also tuple

#also tuple is unchangable so if you wnat to change it you must make it tuple

mode = ("apple", "banana", "cherry", "strawberry")
game = list(mode)
game[1] = "kiwi"
mode = tuple(game)

print(mode)

(tp, erkar, *vairi) = mode #its called unpacking you just created variables ` tp = apples, erkar = banana etc. but bc of *vairi = [stawberry, cherry] cause there is not unaf variables

print(tp)
print(erkar)
print(vairi)

thistuple3 = thistuple1 * 2 #2angam shatacav
print(thistuple3)

#While For loop
mc = 0

#loop until mc == 9
while mc < 10:
  print(mc)
  mc += 1

#break
ma = 1
while ma < 11:
  print(ma)
  if ma == 7:
    break #henc havasar ylni 7in kangnacni loopy
  ma += 1

mb = 1
while mb < 5:
  mb += 1
  if mb == 3:
    continue #henc mb == 3 anteselu a u ancni miusin
  print(mb)

md = 1

while md < 8:
  print(md)
  md += 1
else:
  print("md is no longer less than 8!!")

#For
mrgeghen = ["ananas", "tand"]
abrikos = "tand"
for abrikos in mrgeghen:
  print("ayo")
else:
  print("no")
  #The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
#if your for statment is empty you can putt pass in it to avoid errors
for h in [0, 1, 2]:
  pass

#Function

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")#Emil fname i teghy
my_function("Tobias")
my_function("Linus")

#ete chgides qani hat argumenta linelu karas dnes * nshany
def my_function8(*kids):
  print("The youngest child is " + kids[2])

#nuin bany popoxakannerov
def my_function9(**kid):
  print("His last name is " + kid["laname"])

my_function9(faname = "Tobias", laname = "Refsnes")

my_function8("Emil", "Tobias", "Linus")

def my_function5(child3, child2, child1):
  print("The youngest child is " + child3)


my_function5(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

def y_function(country = "Norway"):
  print("I am from " + country)

y_function("Sweden")
y_function("India")
y_function()
y_function("Brazil")\

#Lambda
lam = lambda you, Me : you + Me
print(lam(10, 11))#you = 10

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
#chem jogum incha baic 22