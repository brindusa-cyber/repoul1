# for variabila_temporara in functie / lista / string:
#     pass
# functie =>> range, enumerate, item
# for i in range(10):
#     print(i)
# #    -----
# range(pas_inceput, pas_final, pasul)
# incepe mereu de la 0 daca nu e specificat pasul de inceput
# ----
# for i in range(2,5):
#     print(i)
#
# for i in range(3, 7, 2):
#     print(i)
# for i in range (3, 7, -2):
#     print(i)
# for i in range (10, 11, -2):
#     print(i)
# list_a = [1, 2, 3, 4]
# for index, value in enumerate(list_a):
#     print(index, "=>", value)
####
# a = "Ana are mere"
# for i in a:
# print(list(a)):
# for i in a:
#     print(i)
#######
# a="Ana are mere"
# print(a[0])
# print(a[-1])
# print(a[1:5])
# print(a[2:1])
# print(a[12])
# print(a[12:13])#ca sa nu dea eroare, si va afisa spatiu
# print(a.find("are"))
# cnp = "1234567890123"
# an = cnp[3:5]
# zi = cnp[5:7]
# print(f"19{an}", luna, zi)
# print(datetime.datetime.strtime())
#
# x = "mere"
# x[0] = "p"
# #stringul este imutabil, dar se face cu replace
# print(x.replace("e", "p"))# inlocuieste peste tot
# print(y)
# print(x.find("e"))
#
# for i, v in enumerate(x):
#     print(i,v)
####
# a = "ana are mere"
# print(a.split(" "))
# print(a.split(a[0], "e"))
# a = a.replace(a[0:3], "e")
# ####tuplu
# a = ("re",)
# y = ("b", 4)
# for i in y:
#     print(i)
# print(a+y)
# ####
# #Daca interez in tupluri,functioneaza. La fel ca stringurile
# print(y[0])
# print()
# y[0] = "a" ## nu merge, este imutabil
# #lista
# x = ["a", False, 4, ("tuple", 3), "soare""]
# x[0] = "b"
# print(x)
##convertire tuplu in lista
# print(type(list(a)))### AICI
# x = [A, True]
##Seturi
# s = {1, 2, 3, 4, 5}
# print(type(s))
# s.add(6)
# print(list(s))
# print(s[1])
# for x in s:
#     print(x)
# ##sau
# for x in set(s):
#     print(x)
#     ##
# s = {1, 7, "A", "a", 3, 4, 5}
# ###
# a = [1, 2, 3]
# b = [4, 5, 2]
# print(set(a))
######

taskuri = ["citit", "scris", "vorbit"]
print(taskuri)
a = ""
while a!= "0":
   a = input("Adauga elemente noi la lista")
   if(a=="0"):
       break
   taskuri.append(a)
   print("Lista noua este {}".format(taskuri))
print("Lista noua este {}".format(taskuri))

