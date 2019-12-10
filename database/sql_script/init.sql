CREATE DATABASE IF NOT EXISTS autochess;
CREATE TABLE IF NOT EXISTS autochess.board(id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(255), spot INT, bonus INT);
CREATE TABLE IF NOT EXISTS autochess.champions(id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(255), health INT, attack INT, price INT, description VARCHAR(255), rarity INT, level INT);
CREATE TABLE IF NOT EXISTS autochess.class(id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(255), number INT, bonus INT);
CREATE TABLE IF NOT EXISTS autochess.heroes(id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(255), health INT, money INT, level INT);
CREATE TABLE IF NOT EXISTS autochess.user(id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, bool_ia boolean);