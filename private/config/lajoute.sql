CREATE DATABASE lajoute CHARACTER SET 'utf8';
--
use lajoute;
--
CREATE TABLE accounts(
id INT NOT NULL AUTO_INCREMENT,
username VARCHAR(80) NOT NULL,
password VARCHAR(80) NOT NULL,
email VARCHAR(80) NOT NULL,
admin INT NOT NULL,
present INT NOT NULL,
nom VARCHAR(80) NOT NULL,
prenom VARCHAR(80) NOT NULL,
ecole VARCHAR(80) NOT NULL,
annee VARCHAR(80) NOT NULL,
phone VARCHAR(80) NOT NULL,
specialite VARCHAR(80) NOT NULL,
role VARCHAR(80) NOT NULL,
PRIMARY	KEY (id));
--
CREATE TABLE cours(
id INT NOT NULL AUTO_INCREMENT,
titre VARCHAR(80) NOT NULL,
datedb VARCHAR(80) NOT NULL,
start VARCHAR(80) NOT NULL,
end VARCHAR(80) NOT NULL,
lien VARCHAR(80) NOT NULL,
color VARCHAR(80) NOT NULL,
PRIMARY	KEY (id));
--
CREATE TABLE infos(
id INT NOT NULL AUTO_INCREMENT,
datedb VARCHAR(80) NOT NULL,
description VARCHAR(80) NOT NULL,
PRIMARY	KEY (id));
--
CREATE TABLE sujets(
id INT NOT NULL AUTO_INCREMENT,
sujet VARCHAR(200) NOT NULL,
type VARCHAR(80) NOT NULL,
PRIMARY	KEY (id));
--
CREATE TABLE config(
id INT NOT NULL AUTO_INCREMENT,
type VARCHAR(80) NOT NULL,
name VARCHAR(80) NOT NULL,
value VARCHAR(80) NOT NULL,
description TEXT NOT NULL,
PRIMARY	KEY (id));
--