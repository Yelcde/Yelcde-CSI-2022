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

# 6. Adicionar, na tabela SÓCIO, o campo abaixo especificado.
ALTER TABLE Socio 
ADD datanasc DATETIME NULL;

# 7. Adicionar, na tabela CIDADE, o campo abaixo especificado.
ALTER TABLE Cidade
ADD CONSTRAINT Cidade_check CHECK(CHAR_LENGTH(UF)=2);

# 8. Adicionar um domínio (validação) para o campo NÚMERO da tabela DEPENDENTE, de modo que o valor seja maior que 0 (zero).
ALTER TABLE Dependente
ADD CONSTRAINT Dependente_validacao CHECK(numero > 0);

# 9. Alterar, na tabela SÓCIO, o tipo do campo NOME para varchar(40).
ALTER TABLE Socio 
MODIFY nome VARCHAR(40) NOT NULL;

# 10. Excluir, na tabela CIDADE, o domínio do campo UF.
ALTER TABLE Cidade
DROP COLUMN uf;

# 11. Excluir, na tabela SÓCIO, o campo cidade.
ALTER TABLE Socio
ADD CONSTRAINT Socio_fk FOREIGN KEY (cidade) REFERENCES Cidade(codigo); #Corrigindo erro ao não colocar fk na criação da tabela

ALTER TABLE Socio
DROP CONSTRAINT Socio_fk;

# 12. Excluir a tabela CIDADE.
DROP TABLE Cidade; 

ALTER TABLE Socio
DROP CONSTRAINT Socio_ibfk_1;

DROP TABLE Cidade; 

# 13. Excluir o banco de dados BD.
DROP DATABASE BD;