from tkinter import *
# from pip import *


# Function Child Window
def open_window2():
    # Second window
    window2 = Tk()

    window2.title('GESTION DES EMPLOYES')
    window2.geometry("700x400")
    window2.resizable(width=False, height=False)
    window2.config(bg='#4065A4')


    # Title
    titre = Label(window2, text="GESTION DES EMPLOYES", font=("Century Gothy", 18), bg="#4065A4", fg="WHITE").place(x=190, y=10)
    titre1= Label(window2, text="ID Employe:",font=("Open Sans", 13), bg="#4065A4", fg="WHITE").place(x=20, y=50)
    titre2= Label(window2, text="Nom:",font=("Open Sans", 13), bg="#4065A4", fg="WHITE").place(x=20, y=80)
    titre3= Label(window2, text="Prenom:",font=("Open Sans", 13), bg="#4065A4", fg="WHITE").place(x=20, y=110)
    titre4= Label(window2, text="Date de naissance:",font=("Open Sans", 13), bg="#4065A4", fg="WHITE").place(x=20, y=140)
    titre5= Label(window2, text="Lieu de naissance:",font=("Open Sans", 13), bg="#4065A4", fg="WHITE").place(x=20, y=170)
    titre6= Label(window2, text="Adresse:",font=("Open Sans", 13), bg="#4065A4", fg="WHITE").place(x=20, y=200)
    titre7= Label(window2, text="Email:",font=("Open Sans", 13), bg="#4065A4", fg="WHITE").place(x=20, y=230)
    titre8= Label(window2, text="Telephone:",font=("Open Sans", 13), bg="#4065A4", fg="WHITE").place(x=20, y=260)

    
    # Entry
    entrer1= Entry(window2, width="23")
    entrer1.place(x=180, y=60)
    entrer2= Entry(window2, width="23")
    entrer2.place(x=180, y=90)
    entrer3= Entry(window2, width="23")
    entrer3.place(x=180, y=120)
    entrer4= Entry(window2, width="23")
    entrer4.place(x=180, y=150)
    entrer5= Entry(window2, width="40")
    entrer5.place(x=180, y=180)
    entrer6= Entry(window2, width="40")
    entrer6.place(x=180, y=210)
    entrer7= Entry(window2, width="40")
    entrer7.place(x=180, y=240)
    entrer8= Entry(window2, width="40")
    entrer8.place(x=180, y=270)

    def delete_items():
        entrer1.delete(first=0, last=100)
        entrer2.delete(first=0, last=100)
        entrer3.delete(first=0, last=100)
        entrer4.delete(first=0, last=100)
        entrer5.delete(first=0, last=100)
        entrer6.delete(first=0, last=100)
        entrer7.delete(first=0, last=100)
        entrer8.delete(first=0, last=100)  
        return

    # Button of Window2
    button_quit = Button(window2, text="QUITTER", height="1", width="7", font=("Open Sans", 13), bg="WHITE", fg="#44749D", command=window2.destroy).place(x=600, y=340)
    button_effacer = Button(window2, text="EFFACER", height="1", width="8", font=("Open Sans", 13), bg="WHITE", fg="#44749D", command=delete_items).place(x=500, y=340)
    button_Rechercher = Button(window2, text="RECHERCHER", height="1", width="12", font=("Open Sans", 13), bg="WHITE", fg="#44749D").place(x=360, y=340)
    button_Enregistrer = Button(window2, text="ENREGISTRER", height="1", width="12", font=("Open Sans", 13), bg="WHITE", fg="#44749D").place(x=220, y=340)
    return


    window2.mainloop()   

    
# Personalisation of Main Window
window1 = Tk()

window1.title('Syteme de Gestion des employes')
window1.geometry("700x350")
window1.resizable(width=False, height=False)
window1.config(background='#4065A4')

# Create titles for Main Window
title = Label(window1, text="PROJET DE FIN DE SESSION", font=("Century Gothy", 30), bg="#4065A4", fg="WHITE").pack()
title = Label(window1, text="Python", font=("Lato Bold", 20), bg="#4065A4", fg="WHITE").pack()
title = Label(window1, text="Systeme de Gestion de RH", font=("Open Sans", 14), bg="#4065A4",fg="WHITE").pack()
title = Label(window1, text="Etudiant: Johnny JOSEPH", font=("Open Sans", 12), bg="#4065A4", fg="WHITE").pack()

# Create Button for Main Window
button_suivant = Button(window1, text="SUIVANT", height="1", width="10", font=("Open Sans", 14), bg="WHITE", fg="#44749D", command=open_window2).pack()

window1.mainloop()