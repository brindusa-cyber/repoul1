#Exercitiu 1
sir = str(input("Introduceti sir de caractere: "))
iterator=0
for caracter in sir:
   iterator+=1
print(iterator)

# Varianta2 ex. 2
# sir = str(input("Introduceti sir de caractere: "))
# if ...  Oare se poate face cu .find?




#Exercitiu 2
treciprincuvant = 0
arond_number = 0
arond_place = 0
punct_number = 0
punct_place = 0
adresa = str(input("Introduceti email: "))
for var in adresa:
 if var == '@':
    arond_number+=1
    arond_place = treciprincuvant
 if var == '.':
    punct_number+=1
    punct_place = treciprincuvant
 treciprincuvant = treciprincuvant + 1
if arond_number == 1 and punct_number == 1 and arond_place < punct_place:
    print("the email is correct")
else:
    print("the email is not correct")

#Varianta completa Exercitiu 2
treciprincuvant = 0
arond_number = 0
arond_place = 0
punct_number = 0
punct_place = 0
correct = True
adresa = str(input("Introduceti email: "))
for var in adresa:
 if var.isdigit() or var.isalpha():
    treciprincuvant+=1
 elif var == '@':
    arond_number+=1
    arond_place = treciprincuvant
    treciprincuvant+=1
 elif var == '.':
    punct_number+=1
    punct_place = treciprincuvant
    treciprincuvant+=1
 else:
    correct = False
    break
if correct and treciprincuvant>4 and arond_number == 1 and punct_number == 1 and punct_place > (arond_place+1):
    print("the email is correct")
else:
    print("the email is not correct")