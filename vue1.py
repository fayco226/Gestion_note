import os
import sys
from tkinter import*
from tkinter import messagebox
from controleur import*
#import vue
"""
def show_modal_window():
    messagebox.askokcancel("Quitter", "Voulez vous vraiment quitter?")


"""       

######################################
#         Fonction pour la vue       #
######################################


def run():
    acceuil.mainloop()

def verifierConnection(a, b):
    if a == "FEUBLE" and b =="1905":
        c = TRUE
    else :
        c = FALSE
    return(c)


def connexion():
    c = entrerNom.get()
    print(c)
        
    d = entrerMdp.get()
    print(d)
    
    
    w = verifierConnection(c,d)
        
    if w:
           
        labelNomUtilisateur.destroy()
        labelMdp.destroy()
        label.destroy()
        entrerMdp.destroy()
        entrerNom.destroy()
        boutonConnecter.destroy()
        bouttonContinuer.config( text="Continuer")
        # bouttonContinuer.grid_forget()
        bouttonContinuer.grid(row=0, column=0, sticky="sw" )
        signe.config(text="connection reussi", font=("",10), fg="green")
        menu1()
            
    else:
        signe.config(text="Nom d'utilisateur ou mot de passe invalide", font=("",10), fg= "red")
        entrerNom.delete(0, END)
        entrerMdp.delete(0, END)
   


def menu():
    #label.grid_forget()
    bouttonContinuer.grid_forget()
    signe.grid_forget()
    labelAjouterEtudiant.grid_forget()
    labelNomEtudiant.grid_forget()
    entrerNomEtudiant.grid_forget()
    labelPrenomEtudiant.grid_forget()
    entrerPrenomEtudiant.grid_forget()
    labelDateNaissance.grid_forget()
    EntrerDateNaissance.grid_forget()
    labelSex.grid_forget()
    genreMasculin.grid_forget()
    genreFeminin.grid_forget()
    bouttonRetour.grid_forget()
    bouttonAjouterEtudiant.grid_forget()
    NiveauLicence1.grid_forget()
    NiveauLicence2.grid_forget()
    NiveauLicence3.grid_forget()
    labelNiveau.grid_forget()
    labelFiliere.grid_forget()
    filiereABF.grid_forget()
    filiereADB.grid_forget()
    filiereCCA.grid_forget()
    filiereMIAGE.grid_forget()
    filiereMID.grid_forget()
    bienvenu.grid(row=0, column=1)
    bouttonEtudiant.grid(row=1, column=0)
    bouttonSemestre.grid(row=1, column=2)
    bouttonEcu.grid(row=2, column=1)
    bouttonNotes.grid(row=3, column=0)
    bouttonUe.grid(row=3, column=2)
    
def menu1():
    #label.grid_forget()
    bouttonContinuer.grid_forget()
    #signe.grid_forget()
    labelAjouterEtudiant.grid_forget()
    labelNomEtudiant.grid_forget()
    entrerNomEtudiant.grid_forget()
    labelPrenomEtudiant.grid_forget()
    entrerPrenomEtudiant.grid_forget()
    labelDateNaissance.grid_forget()
    EntrerDateNaissance.grid_forget()
    labelSex.grid_forget()
    genreMasculin.grid_forget()
    genreFeminin.grid_forget()
    bouttonRetour.grid_forget()
    bouttonAjouterEtudiant.grid_forget()
    NiveauLicence1.grid_forget()
    NiveauLicence2.grid_forget()
    NiveauLicence3.grid_forget()
    bienvenu.grid(row=0, column=1 )
    bouttonEtudiant.grid(row=1, column=0)
    bouttonSemestre.grid(row=1, column=2)
    bouttonEcu.grid(row=2, column=1)
    bouttonNotes.grid(row=3, column=0)
    bouttonUe.grid(row=3, column=2)
    
    
def etudiantFenetre():
    bienvenu.grid_forget()
    bouttonEcu.grid_forget()
    bouttonEtudiant.grid_forget()
    bouttonNotes.grid_forget()
    bouttonSemestre.grid_forget()
    bouttonUe.grid_forget()
    #****************************
    #Enregistrer etudiant
    #*************************
    labelAjouterEtudiant.grid(row=0, column=1)
    labelNomEtudiant.grid(row=1, column=0)
    entrerNomEtudiant.grid(row=1, column=1)
    labelPrenomEtudiant.grid(row=2, column=0)
    entrerPrenomEtudiant.grid(row=2, column=1)
    labelDateNaissance.grid(row=3,column=0 )
    EntrerDateNaissance.grid(row=3, column=1)
    labelSex.grid(row=4, column=0)
    genreMasculin.grid(row=4, column=1 )
    genreFeminin.grid(row=4, column=2)
    labelNiveau.grid(row=5, column= 0)
    NiveauLicence1.grid(row=5, column=1)
    NiveauLicence2.grid(row=5, column=2)
    NiveauLicence3.grid(row=5, column=3)
    labelFiliere.grid(row=6, column=0)
    filiereABF.grid(row=6, column=1)
    filiereADB.grid(row=6, column=2)
    filiereCCA.grid(row=7, column=1)
    filiereMIAGE.grid(row=7, column=2)
    filiereMID.grid(row=7, column=3)
    
    bouttonAjouterEtudiant.grid(row=9, column=1)
    
    
    #********************************
    #Liste des etudiant
    #*****************************
    
    
    
    
    #****************************
    #SEED
    #***************************
    
    bouttonRetour.grid(row=10, column=0)
    bouttonQuitter.grid_forget()
    bouttonQuitter.grid(row=10, column=15)
    

def enregistrerEtudiant():
    a = entrerNomEtudiant.get()
    b = entrerPrenomEtudiant.get()
    c = EntrerDateNaissance.get()
    
    if variableDegenre.get() == 1:
        d = "Masculin"
    else:
        d = "Feminin"
    if variableNiveau.get() == 0:
        e = "Licence 1"
    elif variableNiveau.get()== 1:
        e = "Licence 2"
    elif variableNiveau.get() == 2:
        e = "Licence 3"
    
    if variableFiliere.get()==0:
        f = "ABF"
    elif variableFiliere.get()==1:
        f = "ADB"
    elif variableFiliere.get()==2:
        f = "CCA"
    elif variableFiliere.get()==3:
        f = "MIAGE"
    elif variableFiliere.get()==4:
        f = "MID"
    
    enregistrer.enregistrer_etudiant(a,b,c,d,e,f)
    entrerNomEtudiant.delete(0, END)
    entrerPrenomEtudiant.delete(0, END)
    EntrerDateNaissance.delete(0, END)

    labelAlert.grid(row=0, column=3)
   
   



enregistrer = enregistrement()  


################################################################################
#                            PRINCIPALE                                        #       
#                    definition de la fenetre                                  #
################################################################################


acceuil = Tk() 
acceuil.title("Gestion de note")
#acceuil.iconbitmap("C:\\Users\FAYCAL\Documents\Python\Projet\ima.ico")
#acceuil.minsize(500, 250)
acceuil.resizable(width=TRUE, height=FALSE)
#acceuil.maxsize()
#acceuil.geometry("600x450+250+200")
##
variableDegenre = IntVar()
variableNiveau = IntVar()
variableFiliere = IntVar()

                        ###############################
                        #Pour l'acceuil et le loggin  #
                        ###############################


label = Label(acceuil, text="Se connecter", font=("", 20))
labelNomUtilisateur = Label(acceuil, text="Nom d'utilisteur", font=("",16))
labelMdp = Label(acceuil, text="Mot de passe",font=("",16))
entrerNom = Entry(acceuil, font=("",15))
entrerMdp = Entry(acceuil, show="*", exportselection = 0, font=("",15), )
bouttonQuitter = Button(acceuil, text="Quitter", command=acceuil.quit, font=("",17), fg="red")
bouttonQuitter.quit()
boutonConnecter = Button(acceuil, text="Se connecter", command=connexion, font=("",16), fg="green")
bouttonContinuer = Button(acceuil, command=menu, fg="green", font=("",17))

signe = Label(acceuil, text="")
signe.grid(row=4, column=0)
     
label.grid(row=1, column=1)
labelNomUtilisateur.grid(row=2, column=0)
entrerNom.grid(row=2, column=1)
labelMdp.grid(row=3, column=0)
entrerMdp.grid(row=3, column=1)
boutonConnecter.grid(row=4, column=1)
bouttonQuitter.grid(row=6, column=4, sticky="s")
                        #########################################
                        #         fin acceuil login             #
                        #########################################

                            ####################################
                            #         Menu Barre               #
                            ####################################

menuBarr = Menu(acceuil) 

                                 #######################################
                                #           Menu                      #
                                #######################################

bienvenu = Label(acceuil, text="Bienvenu dans Gestion de notes ", font=("",20), fg="blue")
bouttonSemestre = Button(acceuil, text="Semestre", font=("",15), fg="green")
bouttonEtudiant = Button(acceuil, text="Liste des etudiants", font=("",15), fg="green", command=etudiantFenetre)
bouttonUe = Button(acceuil, text= "Unité d'enseignement", font=("",15), fg="green")
bouttonEcu =  Button(acceuil, text="Liste des matieres", font=("",15), fg="green")
bouttonNotes = Button(acceuil, text="Liste des notes", font=("",15), fg="green")

                                #####################################
                                #          etudiant                 #
                                #####################################
                                
                                #Ajouter etudiant
                                
labelAjouterEtudiant = Label(acceuil, text="Ajouter un etudiant")
labelNomEtudiant = Label(acceuil, text="Nom")
entrerNomEtudiant = Entry(acceuil)
labelPrenomEtudiant = Label(acceuil, text="Prenom")
entrerPrenomEtudiant = Entry(acceuil)
labelDateNaissance = Label(acceuil, text="Date de naissance")
EntrerDateNaissance = Entry(acceuil)
labelSex = Label(acceuil, text="Genre")
genreMasculin = Radiobutton(acceuil, text="Masculin", variable=variableDegenre, value=1)
genreFeminin = Radiobutton(acceuil, text="Feminin",variable=variableDegenre, value=0)
bouttonAjouterEtudiant = Button(acceuil, text="Enregistrer", command=enregistrerEtudiant)
bouttonRetour = Button(acceuil, text="Retour au Menu", command=menu)
labelAlert = Label(acceuil, text="REUSSI", font=("",10), fg="green")
labelNiveau = Label(acceuil, text="Classe")
NiveauLicence1 = Radiobutton(acceuil, text="Licence 1",variable=variableNiveau, value=0)
NiveauLicence2 = Radiobutton(acceuil, text="Licence 2", variable=variableNiveau, value=1)
NiveauLicence3 = Radiobutton(acceuil, text="Licence 3", variable=variableNiveau, value=2)
labelFiliere = Label(acceuil, text="Filiere")
filiereABF = Radiobutton(acceuil, text="ABF", value=0, variable=variableFiliere)
filiereADB = Radiobutton(acceuil, text="ADB", value=1, variable=variableFiliere)
filiereCCA = Radiobutton(acceuil, text="CCA", value=2, variable=variableFiliere)
filiereMIAGE = Radiobutton(acceuil, text="MIAGE", value=3, variable=variableFiliere)
filiereMID = Radiobutton(acceuil, text="MID", value=4, variable=variableFiliere)
                                            #liste
Niveau = Menu(acceuil,)
labelEnteteNom = Label(acceuil, text="Nom")
labelEntetePrenomNom = Label(acceuil, text="Premom")
labelEnteteDateDeNaissance = Label(acceuil, text="Date de Naissance")
labelEnteteGenre = Label(acceuil, text="Genre")
labelEnteteNiveau = Label(acceuil, text="Niveau")







def menuBarre():
    pass