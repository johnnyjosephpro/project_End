from tkinter import *
import webbrowser
from tkinter import Tk

window1: Tk = Tk()

# Personalisation Fenetre
window1.title('Syteme de Gestion des employes')
window1.geometry("700x350")
window1.minsize(600, 250)
# window1.iconbitmap("buffericon.ico")
window1.config(background='#4065A4')
cadre = Frame(window1, bg="#4065A4").pack(side=TOP)


# Create titles project
title1 = Label(cadre, text="\nPROJET DE FIN DE SESSION", font=("Open", 30), bg="#4065A4", fg="WHITE").pack()
title2 = Label(cadre, text="MATIERE: Python", font=("Open Sans", 15), bg="#4065A4", fg="WHITE").pack()
title3 = Label(cadre, text="PROJET: Systeme de Gestion des employes", font=("Open Sans", 12), bg="#4065A4", fg="WHITE").pack()
title4 = Label(cadre, text="Etudiant: Johnny JOSEPH\n\n", font=("Open Sans", 12), bg="#4065A4", fg="WHITE").pack()

# Create Button
button_suivant = Button(cadre, text="SUIVANT", font=("Open Sans", 15), bg="WHITE", fg="#44749D").pack()

window1.mainloop()
