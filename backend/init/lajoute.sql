CREATE DATABASE lajoute CHARACTER SET 'utf8';
--
use lajoute;
--
CREATE TABLE accounts(
    id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    admin INT NOT NULL,
    present INT NOT NULL,
    nom VARCHAR(255) NOT NULL,
    prenom VARCHAR(255) NOT NULL,
    ecole VARCHAR(255) NOT NULL,
    annee VARCHAR(255) NOT NULL,
    phone VARCHAR(255) NOT NULL,
    theme VARCHAR(255) NOT NULL,
    specialite VARCHAR(255) NOT NULL,
    token VARCHAR(255) NOT NULL,
    PRIMARY	KEY (id));
--
CREATE TABLE cours(
    id INT NOT NULL AUTO_INCREMENT,
    titre VARCHAR(255) NOT NULL,
    datedb VARCHAR(255) NOT NULL,
    start VARCHAR(255) NOT NULL,
    end VARCHAR(255) NOT NULL,
    lien VARCHAR(255) NOT NULL,
    color VARCHAR(255) NOT NULL,
    PRIMARY	KEY (id));
--
CREATE TABLE infos(
    id INT NOT NULL AUTO_INCREMENT,
    datedb VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    PRIMARY	KEY (id));
--
CREATE TABLE sujets(
    id INT NOT NULL AUTO_INCREMENT,
    sujet TEXT NOT NULL,
    type VARCHAR(255) NOT NULL,
    PRIMARY	KEY (id));
--
CREATE TABLE config(
    id INT NOT NULL AUTO_INCREMENT,
    type VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    value VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    PRIMARY	KEY (id));
--
CREATE TABLE dbparlementaire(
    id INT NOT NULL AUTO_INCREMENT,
    datedb VARCHAR(255) NOT NULL,
    type VARCHAR(255) NOT NULL,
    sujet TEXT NOT NULL,
    gouvernement TEXT NOT NULL,
    opposition TEXT NOT NULL,
    meilorateur VARCHAR(255) NOT NULL,
    meilequipe VARCHAR(255) NOT NULL,
    jury TEXT NOT NULL,
    equipe TEXT NOT NULL,
    PRIMARY	KEY (id));
--
LOCK TABLES `config` WRITE;
INSERT INTO `config` VALUES
    ('unique','Admin','0','Utilisateur'),
    ('unique','Admin','1','Membre de pôle'),
    ('unique','Admin','2','Bureau ouvert');
    ('unique','Admin','3','Bureau fermé'),
    ('unique','Admin','4','Super admin'),
    ('unique','Admin','-1','Au Goulag'),

    ('unique','Année','A1','A1'),
    ('unique','Année','A2','A2'),
    ('unique','Année','A3','A3'),
    ('unique','Année','A4','A4'),
    ('unique','Année','A5','A5'),
    ('unique','Année','Autre','Autre'),

    ('unique','École','ESILV','ESILV'),
    ('unique','École','EMLV','EMLV'),
    ('unique','École','IIM','IIM'),
    ('unique','École','Autre','Autre'),

    ('unique','Sujet','Conférence de presse','Conférence de presse'),
    ('unique','Sujet','Débat parlementaire','Débat parlementaire'),
    ('unique','Sujet','Plaidoirie','Plaidoirie'),
    ('unique','Sujet','Sujet fun','Sujet fun'),

    ('unique','Débat parlementaire','Match Amical','Match Amical'),
    ('unique','Débat parlementaire','Compétition','Compétition'),
    ('unique','Débat parlementaire','Match Interne','Match Interne'),
    
    ('unique','Spécialité','Débat parlementaire','Débat parlementaire'),
    ('unique','Spécialité','Débat Libre','Débat Libre'),
    ('unique','Spécialité','Plaidoirie','Plaidoirie'),

    ('Pass','Mot de passe','hf_name','sha512'),
    ('Pass','Mot de passe','iterations','1'),
    ('Pass','Mot de passe','dksize','1'),

    ('Pass','Mot de passe','hf_name_pepper','sha512'),
    ('Pass','Mot de passe','iterations_pepper','1'),
    ('Pass','Mot de passe','dksize_pepper','1'),

    ('Pass','Mot de passe','defaultpass','lajoute'),
    ('Pass','Mot de passe','firstaccount','firstaccount'),

    ('Pass','Mot de passe','secret_key','secret_key'),
    ('Pass','Mot de passe','salt','salt'),

    ('Pass','Mot de passe','algorithm','HS512'),

    ('Pass','Mot de passe','BASE','/api'),
    ('Pass','Mot de passe','URL','http://0.0.0.0'),

    ('Pass','Mot de passe','TOKEN','token'),
UNLOCK TABLES;
