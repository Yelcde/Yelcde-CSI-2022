# 1. Criar um banco de dados chamado BD.
CREATE DATABASE BD;

# 2. Abrir banco de dados BD para utilização.
USE BD;

# 3. Criar a tabela CIDADE, conforme a especificação abaixo.
CREATE TABLE Cidade (
	codigo 	INT NOT NULL,
    nome 	VARCHAR(30),
    uf 		CHAR(2),
    CONSTRAINT Cidade_pk PRIMARY KEY (codigo)
);

# 4. Criar a tabela SOCIO, conforme a especificação abaixo.
CREATE TABLE Socio (
	cpf 	CHAR(11) NOT NULL,
    nome 	VARCHAR(30) NOT NULL,
    sexo 	CHAR(1),
    email 	VARCHAR(30) NOT NULL,
    cidade 	INT NOT NULL,
    CONSTRAINT Socio_sexo CHECK (sexo IN ('M', 'F')),
	CONSTRAINT Socio_pk PRIMARY KEY (cpf),
    CONSTRAINT Socio_unique_email UNIQUE (email),
    CONSTRAINT Socio_fk (cidade) REFERENCES Cidade(codigo)
);

# 5. Criar a tabela DEPENDENTE, conforme a especificação abaixo.
CREATE TABLE Dependente (
	socio 	CHAR(11) NOT NULL,
    numero	INT NOT NULL,
    nome	VARCHAR(30) NOT NULL,
    CONSTRAINT Dependente_pk PRIMARY KEY (socio, numero),
    FOREIGN KEY (socio) REFERENCES Socio(cpf) 
);