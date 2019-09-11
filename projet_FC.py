from tkinter import *
from pip import *

window1 = Tk()

# Function Child Window
def open_window2():
    window2 = Tk()
    # child = Toplevel()
    window2.title('GESTION DES EMPLOYES')
    window2.geometry("700x400")
    window2.resizable(width=False, height=False)
    window2.config(bg='#4065A4')

    # Title
    titre = Label(window2, text="GESTION DES EMPLOYES", font=("Century Gothy", 18), bg="#4065A4", fg="WHITE")
    titre.place(x=180, y=10)
    titre1= Label(window2, text="ID Employe:",font=("Open Sans", 13), bg="#4065A4", fg="WHITE").place(x=20, y=50)
    titre2= Label(window2, text="Nom:",font=("Open Sans", 13), bg="#4065A4", fg="WHITE").place(x=20, y=80)
    titre3= Label(window2, text="Prenom:",font=("Open Sans", 13), bg="#4065A4", fg="WHITE").place(x=20, y=110)
    titre4= Label(window2, text="Date de naissance:",font=("Open Sans", 13), bg="#4065A4", fg="WHITE").place(x=20, y=140)
    titre5= Label(window2, text="Lieu de naissance:",font=("Open Sans", 13), bg="#4065A4", fg="WHITE").place(x=20, y=170)
    titre6= Label(window2, text="Adresse:",font=("Open Sans", 13), bg="#4065A4", fg="WHITE").place(x=20, y=200)
    titre7= Label(window2, text="Email:",font=("Open Sans", 13), bg="#4065A4", fg="WHITE").place(x=20, y=280)
    titre8= Label(window2, text="Telephone:",font=("Open Sans", 13), bg="#4065A4", fg="WHITE").place(x=20, y=310)

    # Buttons
    button_quit = Button(window2, text="QUITTER", height="1", width="7", font=("Open Sans", 13), bg="WHITE", fg="#44749D", command=window2.destroy).place(x=580, y=340)
    button_save = Button(window2, text="SAVE", height="1", width="7", font=("Open Sans", 13), bg="WHITE", fg="#44749D").place(x=480, y=340)
    
    
    


# Personalisation Fenetre
window1.title('Syteme de Gestion des employes')
window1.geometry("700x350")
window1.resizable(width=False, height=False)
window1.config(background='#4065A4')
cadre = Frame(window1, bg="#4065A4").pack(side=TOP)

# Create titles project
title = Label(cadre, text="\nPROJET DE FIN DE SESSION", font=("Century Gothy", 30), bg="#4065A4", fg="WHITE").pack()
title = Label(cadre, text="\nPython", font=("Lato Bold", 20), bg="#4065A4", fg="WHITE").pack()
title = Label(cadre, text="Systeme de Gestion de RH", font=("Open Sans", 14), bg="#4065A4",fg="WHITE").pack()
title = Label(cadre, text="Etudiant: Johnny JOSEPH\n\n", font=("Open Sans", 12), bg="#4065A4", fg="WHITE").pack()

# Create Button
button_suivant = Button(cadre, text="SUIVANT", height="1", width="10", font=("Open Sans", 20), bg="WHITE", fg="#44749D", command=open_window2).pack(side=RIGHT, padx=15, pady=15)

window1.mainloop()
window2.mainloop()