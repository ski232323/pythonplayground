# /usr/bin/env python
# -*- coding:Utf-8 -*-

# Importation des modules
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random

# Définition des variables
global password
global liste
global selection
selection = ["ABCDEFGHJKMNPQRSTUVWXYZ", "abcdefghjkmnpqrstuvwxyz", \
             "23456789", "#*/-+:\_&%!?"]
liste = ["ABCDEFGHJKMNPQRSTUVWXYZ", "abcdefghjkmnpqrstuvwxyz", "23456789"]
random.shuffle(liste)


def combine(x):
    option = ((var_maj, 0), (var_min, 1), (var_num, 2), (var_spe, 3))
    if option[x][0].get() == True:
        liste.append(selection[option[x][1]])
    else:
        liste.remove(selection[option[x][1]])


def generate(event):
    "Génération du mot de passe"
    if liste == []:
        messagebox.showinfo(message="Veuillez choisir au moins une option")
    else:
        try:
            nb = nbcar.get()
            if nb < 4 or nb > 30:
                messagebox.showinfo(message="minumum 4 caractères, maximum 30 caractères")
            else:
                compteur = 0
                position = -1
                D = []
                while compteur < nb:
                    if position < len(liste) - 1:
                        position += 1
                    else:
                        position = 0
                    D = D + random.sample(liste[position], 1)
                    compteur += 1
                random.shuffle(D)
                D = "".join(D)
                password.set(D)
        except:
            messagebox.showinfo(message="Veuillez indiquer un nombre de caractère pour le mot de passe")


def addtoclip():
    text = password.get()
    if text == "":
        messagebox.showinfo(message="Merci de générer un mot de passe en appuyant sur -Entrée-")
    else:
        fenetre.clipboard_clear()
        fenetre.clipboard_append(text)


def windowcenter(w, h):
    "Placer la fenêtre principal au centre"
    px = (fenetre.winfo_screenwidth() / 2) - (w / 2)
    py = (fenetre.winfo_screenheight() / 2) - (h / 2)
    fenetre.geometry("%dx%d+%d+%d" % (w, h, px, py))


# Création de l'interface graphique
fenetre = Tk()
fenetre.title("Gpwd")
fenetre.resizable(width=False, height=False)

# Création des widgets checkbutton
var_maj = BooleanVar()
var_min = BooleanVar()
var_num = BooleanVar()
var_spe = BooleanVar()

var_maj.set(True)
var_min.set(True)
var_num.set(True)
var_spe.set(False)

chk_maj = ttk.Checkbutton(fenetre, text="Majuscules",
                          variable=var_maj, command=lambda: combine(0),
                          onvalue=True, offvalue=False)
chk_min = ttk.Checkbutton(fenetre, text="Minuscules",
                          variable=var_min, command=lambda: combine(1),
                          onvalue=True, offvalue=False)
chk_num = ttk.Checkbutton(fenetre, text="Chiffres",
                          variable=var_num, command=lambda: combine(2),
                          onvalue=True, offvalue=False)
chk_spe = ttk.Checkbutton(fenetre, text="Spéciaux",
                          variable=var_spe, command=lambda: combine(3),
                          onvalue=True, offvalue=False)

# Création des widgets label
label_nbcar = ttk.Label(text="Nbre de caractère pour le mot de passe")
label_pwd = ttk.Label(text="Mot de passe")

# Création des widgets entry
nbcar = IntVar()
nbcar.set(7)
entree_nbcar = ttk.Entry(textvariable=nbcar)
password = StringVar()
entree_pwd = ttk.Entry(textvariable=password)

# Création du widget button
bouton = ttk.Button(text="Copier dans le presse-papier", command=addtoclip)

# Placement des widgets
# Checkbutton
chk_maj.grid(column=1, row=1, sticky=W, padx=3, pady=3)
chk_min.grid(column=1, row=2, sticky=W, padx=3, pady=3)
chk_num.grid(column=2, row=1, sticky=W, padx=3, pady=3)
chk_spe.grid(column=2, row=2, sticky=W, padx=3, pady=3)

# Label et Entry pour nombre de caractères
label_nbcar.grid(column=1, row=3, columnspan=2, sticky='W', padx=3, pady=1)
entree_nbcar.grid(column=1, row=4, columnspan=2, sticky='WE', padx=3, pady=3)

# Label et Entry pour mot de passe
label_pwd.grid(column=1, row=5, columnspan=2, sticky='W', padx=3, pady=1)
entree_pwd.grid(column=1, row=6, columnspan=2, sticky='WE', padx=3, pady=3)

# Button pour copie du mot de passe dans le presse-papier
bouton.grid(column=1, row=7, columnspan=2, sticky='WE', padx=3, pady=3)

fenetre.bind('<Return>', generate)
fenetre.update_idletasks()
w = fenetre.winfo_reqwidth()
h = fenetre.winfo_reqheight()
windowcenter(w, h)

fenetre.mainloop()