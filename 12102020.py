x = input("string: ")
a = 0
for item in x:
    a+= 1
print(x, "=>", a)

#####
# def read_char ():
#     b=0
#     a=input("Scrie un cuvant: ")
#
#     for character in a:
#         if character !=" ":
#             return 0
#         else:
#             b+=1
#     print(b)
# read_char()

######
# print(2>3)
# if 2>3
#     a=True
# else
#     a=False
#
# print(a)
########
# a = False
# b = True
# if a is False:
#     print(a)
#####
# a = input("introdu un numar")
# b = None
# if a.isdigit() or int(a) < 100:
#     b = False
# else:
#     b = True
# print (b)

##sau

# a = input("introdu un numar")
# b = None
# if a.isdigit() or int(a) < 100:
#     b = False
# elif a.isdigit():
#     b=True
# print (b)
#####
# nr1 = input("nr1")
# nr2 = input("nr2")
# if int(nr1) > int(nr2): a=nr1
# else
#     a=nr2
#######
# nr1 = input("Introdu nr.1: ")
# nr2 = input("Introdu nr.2: ")
# nr3 = input("Introdu nr.3: ")
# if nr1.isdigit() and nr2.isdigit() and nr3.isdigit()
#     print(max(nr1, nr2, nr3))
# else:
#     print("Nu se poate calcula")

# while conditionare:
#     atribuire1 / instructiune1
#     atribuire2 / instructiune2
#     ...
#     atribuiren / instructiunen
# while True:
#     print("ruleaza")
#   #break
# ce_lmai_mare_numar = 999999
# number = int(input("Introdu un numar: "))

# while number != -1:
#     if number > ce_lmai_mare_numar or ce_lmai_mare_numar > number > -1:
#         number -= 1
#     elif number < -1:
#         number += 1
#         else
#             print(ce_lmai_mare_numar)
#         print(number)
#######
lista = int(input("Introdu un sir de numere: "))
nrPare = 0
nrImpare = 0

while lista != 0:

    if lista % 2 == 0:
        nrPare+= 1
    else:
        nrImpare+= 1
    lista = int(input("Introdu un sir de numere: "))
print("Aveti {} nr pare si {} nr impare".format(nrPare, nrImpare))



# ######
#      a=int(input("Scrieti numerele: "))
#     nrPare = 0
#     nrImpare = 0
#     while input !+ 0:
#         if input_number % 2 == 0:
#             nrPare+= 1
######







