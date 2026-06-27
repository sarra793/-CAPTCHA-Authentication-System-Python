# =====================================================
# CAPTCHA Authentication Program
# =====================================================

import random

def Saisir_N():
    while True:
        N = int(input("Donner la taille N (4 à 20) : "))
        if 4 <= N <= 20:
            return N


def Remplir(T1, T2, N):
    for i in range(N):

        Nbre1 = random.randint(0, 20)
        Nbre2 = random.randint(0, 20)

        choix = random.randint(0, 2)

        if choix == 0:
            op = "+"
            resultat = Nbre1 + Nbre2

        elif choix == 1:
            op = "-"
            resultat = Nbre1 - Nbre2

        else:
            op = "*"
            resultat = Nbre1 * Nbre2

        T1[i] = str(Nbre1) + " " + op + " " + str(Nbre2) + " = ?"
        T2[i] = resultat


def Authentification(T1, T2, N):

    indice = random.randint(0, N-1)

    print("\nRésoudre cette opération :")
    print(T1[indice])

    reponse = int(input("Votre réponse : "))

    if reponse == T2[indice]:
        print("Authentification valide")
    else:
        print("Authentification invalide")


def CAPTCHA():

    N = Saisir_N()

    T1 = [""] * N
    T2 = [0] * N

    Remplir(T1, T2, N)

    Authentification(T1, T2, N)


CAPTCHA()