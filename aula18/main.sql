CREATE DATABASE locadora;
USE locadora;

CREATE TABLE filmes(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    genero VARCHAR(50),
    ano INT,
    preco FLOAT
);

DROP TABLE filmes;

CREATE TABLE clientes(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    endereco VARCHAR(50),
    idade INT
);

CREATE TABLE aluguel (
	id INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    id_filme INT,
    FOREIGN KEY (id_cliente) REFERENCES clientes (id),
	FOREIGN KEY (id_filme) REFERENCES filmes (id)
);

INSERT INTO clientes (nome, endereco, idade) VALUES 
	("João", "Rua logo ali, 10", 35),
	("Maria", "Rua logo ali, 11", 18),
	("José", "Rua logo ali, 12", 24),
	("Pedro", "Rua logo ali, 13", 10),
	("Ana", "Rua logo ali, 14", 51)
;

INSERT INTO filmes (nome, genero, ano, preco) VALUES 
	("Senhor dos aneis A sociedade do Anel", "Fantasia", 2001, 5.50),
	("Senhor dos aneis As duas torres", "Fantasia", 2002, 6),
	("Senhor dos aneis O retorno do rei", "Fantasia", 2003, 6.50),
	("Harry Potter E a Pedra Filosofal", "Aventura", 2004, 4),
	("Harry Potter e a Camara Secreta", "Aventura", 2005, 4.50)
;


SELECT * FROM filmes;

