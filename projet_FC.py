from tkinter import *

window1 = Tk()

# Personalisation Fenetre
window1.title('Syteme de Gestion des employes')
window1.geometry("700x350")
window1.resizable(width=False, height=False)
window1.config(background='#4065A4')
cadre = Frame(window1, bg="#4065A4").pack(side=TOP)

# Create titles project
title = Label(cadre, text="\nPROJET DE FIN DE SESSION", font=("Century Gothy", 30), bg="#4065A4", fg="WHITE").pack()
title = Label(cadre, text="\nMATIERE: Python", font=("Open Sans", 15), bg="#4065A4", fg="WHITE").pack()
title = Label(cadre, text="Systeme de Gestion des employes", font=("Open Sans", 12), bg="#4065A4",fg="WHITE").pack()
title = Label(cadre, text="Etudiant: Johnny JOSEPH\n\n", font=("Open Sans", 12), bg="#4065A4", fg="WHITE").pack()

# Create Button
button_suivant = Button(cadre, text="SUIVANT", height="1", width="15", font=("Open Sans", 20), bg="WHITE", fg="#44749D").pack()

window1.mainloop()
