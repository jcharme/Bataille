# ----------------------------------------------------------
# Nom : Julia Ducharme
# Titre : Bataille
# Description : Compare les cartes les unes par rapport aux autres.
# Le joueur avec la valeur la plus élevée place les deux cartes au bas de son deck.
# La personne qui obtient les 52 cartes gagne.
# ----------------------------------------------------------

# - Importation des modules -------------------------------
import random
import tkinter as tk

# - Déclaration des variables globales --------------------
points1 = 0
points2 = 0

# - Déclaration des fonctions ------------------------------
def carteValeur(carte):
    return carte % 13 + 1  # Assuming cards are numbered 1-52, with 1-13 being Ace-King

def tirer():
    global main1, main2, lblCarte1, lblCarte2, lblMessage, lblNbCartes1, lblNbCartes2, points1, points2

    pot = []

    while main1 and main2:
        carte1 = main1.pop(0)
        carte2 = main2.pop(0)

        pot.extend([carte1, carte2])

        lblCarte1['image'] = imgPaquet[carte1-1]
        lblCarte2['image'] = imgPaquet[carte2-1]

        valeur1 = carteValeur(carte1)
        valeur2 = carteValeur(carte2)

        if valeur1 > valeur2:
            points1 += len(pot)
            pot = []
            break
        elif valeur1 < valeur2:
            points2 += len(pot)
            pot = []
            break

        fenetre.update()  # Update the GUI

    lblNbCartes1['text'] = "Ordinateur : {}".format(len(main1))
    lblNbCartes2['text'] = "Toi : {}".format(len(main2))
    lblPoints1['text'] = "Points: {}".format(points1)
    lblPoints2['text'] = "Points: {}".format(points2)

    if len(main1) == 0:
        if points1 > points2:
            lblMessage['text'] = "Vous avez perdu."
        elif points2 > points1:
            lblMessage['text'] = "Vous avez gagné!"
        else:
            lblMessage['text'] = "C'est un match nul."

# - Programme principal ------------------------------------

paquet = list(range(1, 53))
random.shuffle(paquet)

main1 = paquet[:26]
main2 = paquet[26:]

fenetre = tk.Tk()
fenetre.title("Bataille")
fenetre['bg'] = "#b0e1ff"
fenetre.geometry("500x500")

lblTitre = tk.Label(fenetre, text="Bataille", font="Verdana 30", bg="#b0e1ff")
lblTitre.pack()

# importe les images
imgPaquet = [tk.PhotoImage(file="Bataille/{}.gif".format(i)) for i in range(1, 53)]

# bouton pour tirer cartes ** ne fonctionne pas
btnTirer = tk.Button(fenetre, text="Tirer", command=tirer, font="Verdana 10")
btnTirer.pack()

# Montre le montant de cartes chaque joueur a
lblNbCartesT = tk.Label(fenetre, text="Nombre de cartes:", font="Verdana 10", bg="#b0e1ff")
lblNbCartesT.pack()

lblNbCartes1 = tk.Label(fenetre, text="Ordinateur : {}".format(len(main1)), font="Verdana 10", bg="#b0e1ff")
lblNbCartes1.pack()

lblNbCartes2 = tk.Label(fenetre, text="Toi : {}".format(len(main2)), font="Verdana 10", bg="#b0e1ff")
lblNbCartes2.pack()

# Pour message gagner ou perdu
lblMessage = tk.Label(fenetre)
lblMessage.pack()

# Cartes
lblCarte1 = tk.Label(fenetre)
lblCarte1.pack()

lblCarte2 = tk.Label(fenetre)
lblCarte2.pack()

# Create labels for points
lblPoints1 = tk.Label(fenetre, text="Points: 0", bg="#b0e1ff")
lblPoints1.pack()
lblPoints2 = tk.Label(fenetre, text="Points: 0", bg="#b0e1ff")
lblPoints2.pack()

fenetre.mainloop()
