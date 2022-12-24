
from model import*

class enregistrement():
    def __init__(self):
        self.etudiant_enregistre = etudiant()
        self.semestre_enregistre = semestre()
        self.ue_enregistre = ue()
        self.note_enregistre = note()
        self.ecu_enregistre = ecu()
    
    def enregistrer_etudiant(self, a, b, c, d, e, f):
        self.etudiant_enregistre.enregistrement_etudiant(a,b,c,d,e,f)

    def enregistrer_semestre(self, a, b):
        self.semestre_enregistre.enregistrement_semestre(a,b)

    def enregistrer_ue(self, a, b):
        self.ue_enregistre.enregistrement_ue(a,b)

    def enregistrer_note(self, a, b, c):
        self.note_enregistre.enregistrement_note(a,b,c)

    def enregistrer_ecu(self, a, b, c):
        self.ecu_enregistre.enregistrement_ecu(a,b,c)

class suppression():
    def __init__(self):
        self.etudiant_supprime = etudiant()
        self.semestre_supprime = semestre()
        self.ue_supprime = ue()
        self.note_supprime = note()
        self.ecu_supprime = ecu()
    
    def suppression_etudiant(self, c):
        self.etudiant_supprime.supprimer_etudiant(c)

    def suppression_semestre(self, b):
        self.semestre_supprime.supprimer_semestre(b)

    def suppression_ue(self, a):
        self.ue_supprime.supprimer_ue(a)

    def suppression_note(self, c):
        self.note_supprime.supprimer_note(c)

    def suppression_ecu(self, c):
        self.ecu_supprime.supprimer_ecu(c)

class liste():
    def __init__(self):
        self.etudiant_liste = etudiant()
        self.semestre_liste = semestre()
        self.ue_liste = ue()
        self.note_liste = note()
        self.ecu_liste = ecu()
        self.resultatDeLaListeEtudiant = list()
    
    def getresultat(self):
        return self.resultatDeLaListeEtudiant
    
    def liste_etudiant(self):
        self.resultatDeLaListeEtudiant = self.etudiant_liste.lister_etudiant()

    def liste_semestre(self, a, b):
        self.semestre_liste.lister_semestre()

    def liste_ue(self):
        self.ue_liste.lister_ue()

    def liste_note(self):
        self.note_liste.lister_note()

    def liste_ecu(self):
        self.ecu_liste.lister_ecu()

class modification():
    def __init__(self):
        self.etudiant_modifier = etudiant()
        self.semestre_modifier = semestre()
        self.ue_modifier = ue()
        self.note_modifier = note()
        self.ecu_modifier = ecu()
    
    def modification_etudiant(self, a, b, c):
        self.etudiant_modifier.modifier_etudiant(a,b,c)

    def modification_semestre(self, a, b):
        self.semestre_modifier.modifier_semestre(a,b)

    def modification_ue(self, a, b):
        self.ue_modifier.modifier_ue(a,b)

    def modification_note(self, a, b):
        self.note_modifier.modifier_note(a,b)

    def modification_ecu(self, a, b, c):
        self.ecu_modifier.modifier_ecu(a,b,c)

