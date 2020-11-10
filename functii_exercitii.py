
joc = True


def adunare(x: float,y: float) -> float:
    """
    :param x: primul nr introdus
    :param y: al doilea numar introdus
    :return: suma numerelor
    """
    return x + y


def scadere(x: float,y: float) -> float:
    """
    :param x: primul nr introdus
    :param y: al doilea numar introdus
    :return: diferenta numerelor
    """
    return x - y


def inmultire(x: float,y: float) -> float:
    """
    :param x: primul nr introdus
    :param y: al doilea numar introdus
    :return: produsul numerelor
    """
    return x * y

def impartire(x: float, y: float) -> float:
    """
    :param x: primul nr introdus
    :param y: al doilea numar introdus
    :return: rezultatul impartirii 
    """
    return x / y

def calculator(primul_input: float, al_doilea_input: str, al_treilea_input: float):
    if al_doilea_input == "+":
        calcul = adunare(primul_input, al_treilea_input)
    elif al_doilea_input == "-":
        calcul = scadere(primul_input, al_treilea_input)
    elif al_doilea_input == "*":
        calcul = inmultire(primul_input, al_treilea_input)
    elif al_doilea_input == "/":
        calcul = impartire(primul_input, al_treilea_input)

    return f"Rezultatul este {calcul}"


def recalculare():
    """
    :return: inceperea unei noi operatii sau nu
    """
    alta_operatie = input("Doriti iar: Da / Nu: ").upper()
    joc = False
    if alta_operatie == "DA":
        joc = True
    return joc


def main():

    reincercare = True
    while reincercare:
        primul_input = float(input("Alegeti un numar: "))
        al_doilea_input = input("Alegeti semnul matematic: ")
        al_treilea_input = float(input("Alegeti un numar: "))
        if al_treilea_input == 0 and al_doilea_input == "/":
            print("Nu stiu deastea.")
        else:
            print(calculator(primul_input, al_doilea_input, al_treilea_input))
            reincercare = recalculare()


main()