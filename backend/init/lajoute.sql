CREATE DATABASE lajoute CHARACTER SET 'utf8';
--
use lajoute;
--
CREATE TABLE accounts(
  id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(180) NOT NULL,
  password VARCHAR(180) NOT NULL,
  email VARCHAR(180) NOT NULL,
  admin INT NOT NULL,
  present INT NOT NULL,
  nom VARCHAR(180) NOT NULL,
  prenom VARCHAR(180) NOT NULL,
  ecole VARCHAR(180) NOT NULL,
  annee VARCHAR(180) NOT NULL,
  phone VARCHAR(180) NOT NULL,
  specialite VARCHAR(180) NOT NULL,
  token VARCHAR(180) NOT NULL,
  PRIMARY	KEY (id));
--
CREATE TABLE cours(
  id INT NOT NULL AUTO_INCREMENT,
  titre VARCHAR(180) NOT NULL,
  datedb VARCHAR(80) NOT NULL,
  start VARCHAR(80) NOT NULL,
  end VARCHAR(80) NOT NULL,
  lien VARCHAR(180) NOT NULL,
  color VARCHAR(180) NOT NULL,
  PRIMARY	KEY (id));
--
CREATE TABLE infos(
  id INT NOT NULL AUTO_INCREMENT,
  datedb VARCHAR(80) NOT NULL,
  description TEXT NOT NULL,
  PRIMARY	KEY (id));
--
CREATE TABLE sujets(
  id INT NOT NULL AUTO_INCREMENT,
  sujet TEXT NOT NULL,
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
CREATE TABLE dbparlementaire(
  id INT NOT NULL AUTO_INCREMENT,
  datedb VARCHAR(80) NOT NULL,
  type VARCHAR(80) NOT NULL,
  sujet TEXT NOT NULL,
  gouvernement TEXT NOT NULL,
  opposition TEXT NOT NULL,
  meilorateur VARCHAR(80) NOT NULL,
  meilequipe VARCHAR(80) NOT NULL,
  jury TEXT NOT NULL,
  equipe TEXT NOT NULL,
  PRIMARY	KEY (id));
--
