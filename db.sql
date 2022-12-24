DROP DATABASE IF EXISTS gestion_note;
CREATE DATABASE gestion_note;
USE gestion_note;
CREATE TABLE filiere(
    nom_filiere VARCHAR(100) PRIMARY KEY
);
CREATE TABLE class(
    niveau VARCHAR(50) PRIMARY KEY
);
CREATE TABLE semestre(
    numero_semestre INT PRIMARY KEY AUTO_INCREMENT
);
CREATE TABLE trimestre(
    id_trimestre INT PRIMARY KEY AUTO_INCREMENT,
    numero_semestre INT,
    niveau VARCHAR(50)
);
CREATE TABLE ue(
    id_ue INT PRIMARY KEY AUTO_INCREMENT,
    nom_ue VARCHAR(50),
    numero_semestre INT,
    CONSTRAINT numero_semestre_fk FOREIGN KEY(numero_semestre) REFERENCES semestre(numero_semestre)
);


CREATE TABLE ecu(
    id_ecu INT PRIMARY KEY AUTO_INCREMENT,
    nom_ecu VARCHAR(50),
    coeficiant INT,
    id_ue INT,
    CONSTRAINT id_ue_fk FOREIGN KEY(id_ue) REFERENCES ue(id_ue)
);


CREATE TABLE etudiant(
    matricule_etudiant INT PRIMARY KEY AUTO_INCREMENT,
    nom_etudiant VARCHAR(50),
    prenom_etudiant VARCHAR(1000),
    date_de_naissance VARCHAR(15),
    genre VARCHAR(15),
    niveau VARCHAR(50),
    nom_filiere VARCHAR(100),
    CONSTRAINT niveau_fk FOREIGN KEY(niveau) REFERENCES class(niveau),
    CONSTRAINT nom_filiere_fk FOREIGN KEY(nom_filiere) REFERENCES filiere(nom_filiere)
);


CREATE TABLE note(
    matricule_etudiant INT,
    id_ecu INT,
    valeur FLOAT,
    CONSTRAINT id_ecu_fk FOREIGN KEY(id_ecu) REFERENCES ecu(id_ecu),
    CONSTRAINT matricule_etudiant_fk FOREIGN KEY(matricule_etudiant) REFERENCES etudiant(matricule_etudiant)
);


INSERT INTO filiere("ABF");
INSERT INTO filiere("ADB");
INSERT INTO filiere("CCA");
INSERT INTO filiere("MIAGE");
INSERT INTO filiere("MID");
INSERT INTO class("Licence 1");
INSERT INTO class("Licence 2");
INSERT INTO class("Licence 3");
INSERT INTO 