import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

db = mysql.connector.connect(
host = "localhost",
user = "root",
password = "",
database = "boutique"
)

#GUI

white = '#ffffff'
black = ''#000000''

gui = Tk()
gui.geometry('700x300')
gui.title('Stock Manager')
gui.resizable(False,False)
gui.configure(bg=black)

# Ajout d'un produit

add_name = Entry(gui)
add_name.insert(0,"Nom")
add_name.grid(row=1,column=1,padx= 5,pady=3,)

add_desc = Entry(gui)
add_desc.insert(0,"Description")
add_desc.grid(row=2,column=1,padx= 5,pady=3,)

add_prix = Entry(gui)
add_prix.insert(0,"Prix")
add_prix.grid(row=3,column=1,padx= 5,pady=3,)

add_quantite = Entry(gui)
add_quantite.insert(0,"Quantite")
add_quantite.grid(row=4,column=1,padx= 5,pady=3,)

add_categorie = Entry(gui)
add_categorie.insert(0,"Categorie")
add_categorie.grid(row=5,column=1,padx= 5,pady=3,)

#Suppression d'un produit

supp_produit = Entry(gui)
supp_produit.insert(0,"Produit à supprimer")
supp_produit_id = Entry(gui)
supp_produit_id.insert(0,"Id du produit à supprimer")
supp_produit.grid(row=4, column=5,padx=5,pady=3)
supp_produit_id.grid(row=5,column=5,padx=5,pady=3)
#Modifier un produit

update_name = Entry(gui)
update_name.insert(0,"Nom à modifier")
update_name.grid(row=1,column=10,padx= 5,pady=3,)

update_desc = Entry(gui)
update_desc.insert(0,"Description à modifier")
update_desc.grid(row=2,column=10,padx= 5,pady=3,)

update_prix = Entry(gui)
update_prix.insert(0,"Prix à modifier")
update_prix.grid(row=3,column=10,padx= 5,pady=3,)

update_quantite = Entry(gui)
update_quantite.insert(0,"Quantité à modifier")
update_quantite.grid(row=4,column=10,padx= 5,pady=3,)

update_categorie = Entry(gui)
update_categorie.insert(0,"Catégorie à modifier")
update_categorie.grid(row=5,column=10,padx= 5,pady=3,)

#Fonctions
def ajouter_produit():
        nom = add_name.get()
        description = add_desc.get()
        prix = add_prix.get()
        quantite = add_quantite.get()
        id_categorie = add_categorie.get()

        cursor = db.cursor()
        cursor.execute(f"INSERT INTO produit (nom, description, prix, quantite, id_categorie) values ('{nom}', '{description}', {prix}, {quantite}, {id_categorie});")
        db.commit()
        cursor.close()

        messagebox.showinfo('ADD','Produit ajouté !')

def supprimer_produit():

        value = supp_produit.get()
        cursor = db.cursor()
        cursor.execute(f"DELETE FROM produit WHERE id = {value}")
        db.commit()
        cursor.close()

        messagebox.showinfo('DELETE','Produit supprimé !')

def modifier_produit():
        new_nom = update_name.get()
        new_description = update_desc.get()
        new_prix = update_prix.get()
        new_quantite = update_quantite.get()
        new_id_categorie = update_categorie.get()
        new_id = supp_produit_id()

        cursor = db.cursor()
        cursor.execute(f"UPDATE produit set nom = '{new_nom}', description = '{new_description}', prix = {new_prix}, quantite = {new_quantite}, id_categorie = {new_id_categorie} WHERE id = {new_id} ;")
        db.commit()
        cursor.close()


messagebox.showinfo('Modified', 'Produit modifié !')

#Fonction pour l'affichage des tableaux
def afficher_cat():
    display_cat = Toplevel()
    display_cat.title('Affichage des catégories')
    display_cat.configure(bg = white)
    display_cat.geometry('400x200')
    display_cat.resizable(False,True)
    cursor = db.cursor()

    tab_cat = ttk.Treeview(display_cat, columns=(1,2),show='headings')

    tab_cat.heading('1', text='ID')
    tab_cat.heading('2',text='Nom de la catégorie')

    tab_cat.grid(row=0, column=0)

    cursor.execute('SELECT * FROM categorie;')

    for categorie in cursor:
        tab_cat.insert('',END,values=categorie)
    cursor.close()

    display_cat.mainloop()


def afficher_produit():
    display = Toplevel()
    display.title('Affichage des stocks')
    display.configure(bg = white)
    display.geometry('1150x200')
    display.resizable(False,True)
    cursor = db.cursor()

    tab = ttk.Treeview(display, columns=(1,2,3,4,5,6),show='headings')

    tab.heading('1',text='ID')
    tab.heading('2',text='Nom')
    tab.heading('3',text='Description')
    tab.heading('4', text='Prix')
    tab.heading('5',text='Quantite')
    tab.heading('6',text='Categorie')

    tab.grid(row=0, column=0)

    cursor.execute("SELECT * FROM produit;")

    for produit in cursor:
        tab.insert('',END,values=produit)
    cursor.close()




    display.mainloop()

bouton_cat = Button(gui, text = "Afficher les catégories", command=afficher_cat).grid(row=13,column=5, pady=5, padx= 15)
bouton_stock = Button(gui, text = "Afficher le stock", command=afficher_produit).grid(row=10,column=5, pady=5, padx= 15)
bouton_ajout = Button(gui, text = "Ajouter un produit", command = ajouter_produit).grid(row=6,column=1, pady=5, padx= 15)
bouton_modifier= Button(gui, text = "Modifier un produit", command=modifier_produit).grid(row=6,column=10, pady=3, padx= 15)
bouton_supprimer = Button(gui, text = "Supprimer un produit", command=supprimer_produit).grid(row=6,column=5, pady=5, padx= 15)


gui.mainloop()
