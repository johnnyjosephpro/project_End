import tkinter as tk

window1 = tk.Tk()

window1.title('Syteme de Gestion des employes')

window1.geometry("800x400")

# Create titles project
title1 = tk.Label(window1, text="\nPROJET DE FIN DE SESSION \n", font="Open 13 bold", fg="BLACK", compound=tk.CENTER).pack()
title2 = tk.Label(window1, text="MATIERE: Python\n", font="Open 10", compound=tk.CENTER).pack()

# Proprieties the window
title3 = tk.Label(window1, text="PROJET: Systeme de Gestion des employes", font="Open 12 bold").pack(padx=5, pady=5)
title4 = tk.Label(window1, text="PRENOM: Johnny", font="Open 12 bold").pack()
title5 = tk.Label(window1, text= "NOM: JOSEPH", font="Open 12 bold").pack()


tk.mainloop()
