
Exercitiul 1(b)
sir_user = input('Introduceti sir:')
a = 0
for item in sir_user:
    a += 1
    print("Sirul introdus are", a, "caractere")
#########################
import random
lista_cuvinte = ["palarie", "deget", "picior", "abecedar"]

cuv_ales = random.choice(lista_cuvinte)
len_cuv_ales = len(cuv_ales)

len_litere_lipsa = len_cuv_ales-2
display = cuv_ales.replace(cuv_ales[1:-1],"-"*(len_litere_lipsa))
display_lista = list(display)

nr_incercari = 0
litere_incercate = ""
displayObtinut = list(cuv_ales)

for i in range(len_cuv_ales):
    display_lista[i] = "-"
display_lista[0] = cuv_ales[0]
display_lista[len_cuv_ales-1] = cuv_ales[len_cuv_ales - 1]

for i in range(1, len_cuv_ales - 1, 1):
    if display_lista[0] == cuv_ales[i]:
        display_lista[i] = cuv_ales[i] # ii cer sa arate litera
    elif display_lista[len_cuv_ales-1] == cuv_ales[i]:
        display_lista[i] = cuv_ales[i]
    else: display_lista[i] = "-"
print("".join(display_lista))

while nr_incercari<7:
    incercare = input("Alegeti o litera: ")
    dejaincercata = True
    if litere_incercate.find(str(incercare)) != -1:
        print("Ati mai incercat aceasta litera!")
        dejaincercata = False
    if dejaincercata:
        litere_incercate = litere_incercate + str(incercare)
        if incercare in cuv_ales:
            for (index, value) in enumerate(cuv_ales):
                if value == str(incercare):
                    display_lista[index] = str(incercare)
            displayTwo = "".join(display_lista)
            print(displayTwo)
            if displayTwo.find("-") == -1:
                print("Ati castigat!")
                break
        else: 
            nr_incercari += 1
            incercari_ramase = 7 - nr_incercari
            print("Ati gresit. Numar incercari ramase: ", incercari_ramase)
            if incercari_ramase == 0:
                print("Ati pierdut")
            print("".join(display_lista)) 

###################################
#Inca nu am reusit, imi mai trebuie timp
nr_telefon = input(str("Scrieti numarul de telefon:"))
lungime = len(nr_telefon),
pos1 = nr_telefon.find("@")
pos2 = nr_telefon.find(".")
if (nr_telefon[0])!="0":
    print("Nr de telefon trebuie sa inceapa cu 0")
elif (nr_telefon[0]) == "0":
    pass
elif len(nr_telefon)>10 or len(nr_telefon) < 10:
print("Nr de telefon trebuie sa aiba 10 cifre")
if "@" in nr_telefon = True and "." in nr_telefon = True and pos1 < pos2:
    elif pos1 > pos2
    print ("Nr de tel este incorect, mai verificati")
    elif
# trebuie sa adaug inca o conditie pentru ca  @ si . sa se regaseasca o sg data in nr., dar e prea tarziu
else print("Nr. de telefon => valid")
#####################################
