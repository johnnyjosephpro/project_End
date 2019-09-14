from tkinter import *
import mysql.connector

# Function create Database and create a Table
def create_database():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=""
    )
    requete1 = "CREATE DATABASE project_db"
    requete2 = "CREATE TABLE employe (ID int(10) NOT NULL AUTO_INCREMENT PRIMARY KEY,nom varchar(20) NOT NULL,prenom varchar(20) NOT NULL,date_naissance date,lieu_naissance varchar(20),adresse varchar(50),email varchar(20),telephone varchar(15))"
    mycursor = mydb.cursor()
    mycursor.execute("")
    print("Data Base create")
    mydb.commit()

#Function Enregistrement
# def enregistrer():

#     return


# Function Child Window
def open_window2():
    # Second window
    window2 = Tk()

    window2.title('GESTION DES EMPLOYES')
    window2.geometry("700x450")
    window2.resizable(width=False, height=False)
    window2.config(bg='#3b3b3b')

    # Title
    titre = Label(window2, text="GESTION DES EMPLOYES", font=("Century Gothic Bold", 20), bg="#3b3b3b", fg="#FFCD00").place(x=200, y=10)
    titre1= Label(window2, text="ID Employe",font=("Century Gothic", 13), bg="#3b3b3b", fg="WHITE").place(x=30, y=50)
    titre2= Label(window2, text="Nom",font=("Century Gothic", 13), bg="#3b3b3b", fg="WHITE").place(x=30, y=110)
    titre3= Label(window2, text="Prenom",font=("Century Gothic", 13), bg="#3b3b3b", fg="WHITE").place(x=350, y=110)
    titre4= Label(window2, text="Sexe",font=("Century Gothic", 13), bg="#3b3b3b", fg="WHITE").place(x=30, y=170)
    titre5= Label(window2, text="Date de naissance",font=("Century Gothic", 13), bg="#3b3b3b", fg="WHITE").place(x=350, y=170)
    titre6= Label(window2, text="Lieu de naissance",font=("Century Gothic", 13), bg="#3b3b3b", fg="WHITE").place(x=30, y=230)
    titre7= Label(window2, text="Adresse",font=("Century Gothic", 13), bg="#3b3b3b", fg="WHITE").place(x=350, y=230)
    titre8= Label(window2, text="Email",font=("Century Gothic", 13), bg="#3b3b3b", fg="WHITE").place(x=30, y=290)
    titre9= Label(window2, text="Telephone",font=("Century Gothic", 13), bg="#3b3b3b", fg="WHITE").place(x=350, y=290)
    
    # def sel():
    #     selection = str(sexe.get())
    # return

    # Entry of Windows2
    entrer1= Entry(window2, width="15")
    entrer1.place(x=35, y=80)
    entrer2= Entry(window2, width="30")
    entrer2.place(x=35, y=140)
    entrer3= Entry(window2, width="30")
    entrer3.place(x=355, y=140)
    
    rbutton1= Radiobutton(window2, text="Masculin",value=1, font=("Century Gothic", 12), fg="WHITE", bg="#3b3b3b")
    rbutton1.place(x=35, y=195)
    rbutton2= Radiobutton(window2, text="Feminin", value=2, font=("Century Gothic", 12),fg="WHITE", bg="#3b3b3b")
    rbutton2.place(x=140, y=195)
    entrer4= Entry(window2, width="30")
    entrer4.place(x=355, y=200)
    entrer5= Entry(window2, width="30")
    entrer5.place(x=35, y=260)
    entrer6= Entry(window2, width="30")
    entrer6.place(x=355, y=260)
    entrer7= Entry(window2, width="30")
    entrer7.place(x=35, y=320)
    entrer8= Entry(window2, width="30")
    entrer8.place(x=355, y=320)

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
    button_quit = Button(window2, text="QUITTER", height="1", width="7", font=("Century Gothic Bold", 13), bg="WHITE", fg="#44749D", command=window2.destroy).place(x=600, y=380)
    button_effacer = Button(window2, text="EFFACER", height="1", width="8", font=("Century Gothic Bold", 13), bg="WHITE", fg="#44749D", command=delete_items).place(x=500, y=380)
    button_Rechercher = Button(window2, text="RECHERCHER", height="1", width="12", font=("Century Gothic Bold", 13), bg="WHITE", fg="#44749D").place(x=360, y=380)
    button_Enregistrer = Button(window2, text="ENREGISTRER", height="1", width="12", font=("Century Gothic Bold", 13), bg="WHITE", fg="#44749D").place(x=220, y=380)
    return

    window2.mainloop()   

    
# Personalisation of Main Window
window1 = Tk()

window1.title('Syteme de Gestion des employes')
window1.geometry("700x350")
window1.resizable(width=False, height=False)
window1.config(background='#3b3b3b')

# Create titles for Main Window
title = Label(window1, text="PROJET DE FIN DE SESSION", font=("Century Gothic bold", 22), bg="#3b3b3b", fg="#FFCD00").place(x=170, y=10)
title1 = Label(window1, text="MATIERE: ", font=("Century Gothic", 15), bg="#3b3b3b", fg="WHITE").place(x=30, y= 60)
title1 = Label(window1, text="Python ", font=("Century Gothic Bold", 14), bg="#3b3b3b", fg="WHITE").place(x=140, y= 60)
title2 = Label(window1, text="PROJET: ", font=("Century Gothic", 15), bg="#3b3b3b", fg="WHITE").place(x=30, y= 90)
title2 = Label(window1, text="Systeme de Gestion des employes", font=("Century Gothic Bold", 14), bg="#3b3b3b",fg="WHITE").place(x=140, y=90)
title3 = Label(window1, text="Etudiant:", font=("Century Gothic", 15), bg="#3b3b3b", fg="WHITE").place(x=30, y=120)
title3 = Label(window1, text="Johnny JOSEPH", font=("Century Gothic Bold", 14), bg="#3b3b3b", fg="WHITE").place(x=140, y=120)
title4 = Label(window1, text="Professeur:", font=("Century Gothic", 15), bg="#3b3b3b", fg="WHITE").place(x=30, y=150)
title4 = Label(window1, text="Rodely DOUILLY", font=("Century Gothic Bold", 14), bg="#3b3b3b", fg="WHITE").place(x=140, y=150)
title5 = Label(window1, text="Option:", font=("Century Gothic", 15), bg="#3b3b3b", fg="WHITE").place(x=30, y=180)
title5 = Label(window1, text="Full Stack Web Developer", font=("Century Gothic Bold", 14), bg="#3b3b3b", fg="WHITE").place(x=140, y=180)

# Create Button for Main Window
button_suivant = Button(window1, text="SUIVANT", height="1", width="10", font=("Century Gothic Bold", 14), bg="WHITE", fg="#44749D", command=open_window2).place(x=560, y=290)

window1.mainloop()