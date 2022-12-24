import mysql.connector

#class for database connection

class connectdb:
    def __init__(self):
        pass
    def connectdatabase(self):
        try :
            self.db = mysql.connector.connect(host="localhost", user="root", password="", database="gestion_note")
            print("Reussi")
            return self.db
        except :
            print("erreur de connexion a la base de donnee")




#student class
class etudiant():
    def __init__(self) :
        self.bd = connectdb()
        self.nombreDeLigne = int(0)

    def enregistrement_etudiant(self,nom_e, prenom_e,dateDeNaissance_e, genre, niveau, nom_filiere):
        e = self.bd.connectdatabase()
        curseur = e.cursor()

        try:
            
            curseur.execute(" INSERT INTO etudiant(nom_etudiant, prenom_etudiant,date_de_naissance,genre, niveau, nom_filiere) VALUES (%s,%s,%s,%s,%s,%s)",(nom_e, prenom_e,dateDeNaissance_e,genre,niveau,nom_filiere))
        
            e.commit()
        except mysql.connector.errors.ProgrammingError:
            print("ERROR")
        e.close()
        
    def supprimer_etudiant(self,id_e):
        e = self.bd.connectdatabase()
        curseur = e.cursor()

        try:
            
            curseur.execute(" DELETE FROM etudiant WHERE `etudiant`.`matricule_etudiant` = {}".format(id_e))
        
            e.commit()
        except mysql.connector.errors.ProgrammingError:
            print("ERROR")
        e.close()
    
    
    def modifier_etudiant(self, matricule_etudiant, n, mis_a_jour):
        e = self.bd.connectdatabase()
        curseur = e.cursor()

        try:
            if n == 0:
                curseur.execute(" UPDATE `etudiant` SET `nom_etudiant` = {} WHERE `etudiant`.`matricule_etudiant` = {}".format(mis_a_jour, matricule_etudiant))
            if n == 1:
                curseur.execute(" UPDATE `etudiant` SET `prenom_etudiant` = {} WHERE `etudiant`.`matricule_etudiant` = {}".format(mis_a_jour, matricule_etudiant))
            if n == 2:
                curseur.execute(" UPDATE `etudiant` SET `date_de_naissance` = {} WHERE `etudiant`.`matricule_etudiant` = {}".format(mis_a_jour, matricule_etudiant))
            e.commit()
        except mysql.connector.errors.ProgrammingError:
            print("ERROR")
        e.close()
    
    
    def lister_etudiant(self, filiere):
        e = self.bd.connectdatabase()
        curseur = e.cursor()
        nombre = e.cursor()

        try:
            if filiere == "toutes les filieres":
                
                self.nombreDeLigne = nombre.execute("SELECT COUNT * FROM etudiant")
                curseur.execute(" SELECT * FROM etudiant")
        
                return curseur.fetchall()
            elif filiere == "ABF":
                
                self.nombreDeLigne = nombre.execute("SELECT COUNT * FROM etudiant WHERE filiere = `ABF`")
                curseur.execute(" SELECT * FROM etudiant WHERE filiere = `ABF`")
        
                return curseur.fetchall()
            elif filiere == "ADB":
                
                self.nombreDeLigne = nombre.execute("SELECT COUNT * FROM etudiant WHERE filiere = `ADB`")
                curseur.execute(" SELECT * FROM etudiant WHERE filiere = `ADB`")
        
                return curseur.fetchall()
            elif filiere == "CCA":
                
                self.nombreDeLigne = nombre.execute("SELECT COUNT * FROM etudiant WHERE filiere = `CCA`")
                curseur.execute(" SELECT * FROM etudiant WHERE filiere = `CCA`")
        
                return curseur.fetchall()
            elif filiere == "MIAGE":
                
                self.nombreDeLigne = nombre.execute("SELECT COUNT * FROM etudiant WHERE filiere = `MIAGE`")
                curseur.execute(" SELECT * FROM etudiant WHERE filiere = `MIAGE`")
        
                return curseur.fetchall()
            elif filiere == "MID":
                
                self.nombreDeLigne = nombre.execute("SELECT COUNT * FROM etudiant WHERE filiere = `MID`")
                curseur.execute(" SELECT * FROM etudiant WHERE filiere = `MID`")
        
                return curseur.fetchall()
    
        except mysql.connector.errors.ProgrammingError:
            print("ERROR")
        e.close()
    def getnombreDeLigne(self):
        return self.nombreDeLigne
            
        
    
        

#note class

class note():
    def __init__(self):
        self.bd = connectdb()
    
    
    def enregistrement_note(self, matricule_etudiant, id_ecu, valeur):
        e = self.bd.connectdatabase()
        curseur = e.cursor()

        try:
            
            curseur.execute(" INSERT INTO note(matricule_etudiant, id_ecu, valeur) VALUES (%s,%s,%s)",(matricule_etudiant, id_ecu, valeur))
        
            e.commit()
        except mysql.connector.errors.ProgrammingError:
            print("ERROR")
        e.close()
        
        
    def supprimer_note(self, valeur):
        e = self.bd.connectdatabase()
        curseur = e.cursor()

        try:
            
            curseur.execute(" DELETE FROM `note` WHERE `note`.`valeur`= {}".format(valeur))
        
            e.commit()
        except mysql.connector.errors.ProgrammingError:
            print("ERROR")
        e.close()
        
    def modifier_note(self, mis_a_jour, matricule_etudiant, id_ecu):
        e = self.bd.connectdatabase()
        curseur = e.cursor()

        try:
            curseur.execute(" UPDATE `note` SET `valeur` = {} WHERE `note`.`matricule_etudiant` = {} AND `note`.`id_ecu` = {}".format(mis_a_jour, matricule_etudiant, id_ecu))
            e.commit()
        except mysql.connector.errors.ProgrammingError:
            print("ERROR")
        e.close()
        
    def lister_note(self):
        e = self.bd.connectdatabase()
        curseur = e.cursor()
        try:
            curseur.execute(" SELECT * FROM note ")
            for c in curseur.fetchall():
                print(c)
        except :
                print("ERROR")
        e.close()
        
        
#semestre class

class semestre():
    def __init__(self):
        self.bd = connectdb()
        
        
    def enregistrement_semestre(self, numero_semestre, niveau ):
        e = self.bd.connectdatabase()
        curseur = e.cursor()
        try:
            curseur.execute(" INSERT INTO semestre(numero_semestre, niveau) VALUES (%s,%s)",(numero_semestre, niveau))
        
            e.commit()
        except mysql.connector.errors.ProgrammingError:
            print("ERROR")
        e.close()
        
        
    def supprimer_semestre(self,numero):
        e = self.bd.connectdatabase()
        curseur = e.cursor()

        try:
            
            curseur.execute(" DELETE FROM `semestre` WHERE `semestre`.`numero_semetre`= {}".format(numero))
        
            e.commit()
        except mysql.connector.errors.ProgrammingError:
            print("ERROR")
        e.close()
    
    def modifier_semestre(self, mis_a_jour, id_semestre):
        e = self.bd.connectdatabase()
        curseur = e.cursor()

        try:
            
            curseur.execute(" UPDATE `semestre` SET `niveau` = {} WHERE `semestre`.`id_semestre` = {}".format(mis_a_jour, id_semestre))
            e.commit()
        except mysql.connector.errors.ProgrammingError:
            print("ERROR")
        e.close()
    
    
    def lister_semestre(self):
        e = self.bd.connectdatabase()
        curseur = e.cursor()

        try:
            
            curseur.execute(" SELECT * FROM semestre")
        
            e.commit()
        except mysql.connector.errors.ProgrammingError:
            print("ERROR")
        e.close()
             
#ue class

class ue():
    
    def __init__(self):
        self.bd = connectdb()
        
        
    def enregistrement_ue(self, nom_ue, id_semestre ):
        e = self.bd.connectdatabase()
        curseur = e.cursor()

        try:
            
            curseur.execute(" INSERT INTO ue(nom_ue, id_semestre) VALUES (%s,%s)",(nom_ue, id_semestre))
        
            e.commit()
        except mysql.connector.errors.ProgrammingError:
            print("ERROR")
        e.close()
        
    def supprimer_ue(self,id_ue):
        e = self.bd.connectdatabase()
        curseur = e.cursor()

        try:
            
            curseur.execute(" DELETE FROM `ue` WHERE `ue`.`id_ue`= {}".format(id_ue))
        
            e.commit()
        except mysql.connector.errors.ProgrammingError:
            print("ERROR")
        e.close()
        
    def modifier_ue(self, mis_a_jour, id_ue, id_semestre):
        e = self.bd.connectdatabase()
        curseur = e.cursor()

        try:
            
            curseur.execute(" UPDATE `ue` SET `nom_ue` = {} WHERE `ue`.`id_ue` = {} AND `ue`.`id_semestre` = {}".format(mis_a_jour, id_ue, id_semestre))
            e.commit()
        except mysql.connector.errors.ProgrammingError:
            print("ERROR")
        e.close()
        
    def lister_ue(self):
        e = self.bd.connectdatabase()
        curseur = e.cursor()

        try:
            
            curseur.execute(" SELECT * FROM `ue`")
        
            e.commit()
        except mysql.connector.errors.ProgrammingError:
            print("ERROR")
        e.close()
        
#ecu class
class ecu():
    def __init__(self):
        self.bd = connectdb()
    
    
    
    def enregistrement_ecu(self, nom, coeficiant, id_ue ):
        e = self.bd.connectdatabase()
        curseur = e.cursor()

        try:
            
            curseur.execute(" INSERT INTO ecu(nom_ecu, coeficiant, id_ue) VALUES (%s,%s,%s)",(nom, coeficiant, id_ue))
        
            e.commit()
        except mysql.connector.errors.ProgrammingError:
            print("ERROR")
        e.close()
        
        
    def supprimer_ecu(self,id_ecu):
        e = self.bd.connectdatabase()
        curseur = e.cursor()

        try:
            
            curseur.execute(" DELETE FROM `ecu` WHERE `ecu`.`id_ecu`= {}".format(id_ecu))
        
            e.commit()
        except mysql.connector.errors.ProgrammingError:
            print("ERROR")
        e.close()
    
    
    def modifier_ecu(self, n, mis_a_jour, id_ecu, id_ue):
        e = self.bd.connectdatabase()
        curseur = e.cursor()

        try:
            if n == 0:
                curseur.execute(" UPDATE `ecu` SET `nom_ecu` = {} WHERE `ecu`.`id_ecu` = {} AND `ecu`.`id_ue` = {}".format(mis_a_jour, id_ecu, id_ue))
            if n == 1:
                curseur.execute(" UPDATE `ecu` SET `prenom_ecu` = {} WHERE `ecu`.`id_ecu` = {} AND `ecu`.`id_ue` = {}".format(mis_a_jour, id_ecu, id_ue))
            e.commit()
        except mysql.connector.errors.ProgrammingError:
            print("ERROR")
        e.close()
    
    
    def lister_ecu(self):
        e = self.bd.connectdatabase()
        curseur = e.cursor()
        try:
            curseur.execute(" SELECT * FROM ecu ")
            for c in curseur.fetchall():
                print(c)
        except :
            print("ERROR")
        self.bd.close()

