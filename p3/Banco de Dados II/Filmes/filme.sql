CREATE TABLE Filme (
CodFILME Serial NOT NULL,
Titulo Varchar(25),
Ano integer,
Duracao integer,
CodCATEG integer,
CodEst integer);

CREATE TABLE Artista (
CodART Serial NOT NULL,
NomeART Varchar(25),
Cidade Varchar(20),
Pais Varchar(20),
DataNasc Date);

CREATE TABLE Estudio (
CodEst serial NOT NULL,
NomeEst Varchar(25));

CREATE TABLE Categoria (
CodCATEG serial NOT NULL,
DescCATEG VARCHAR(25));

CREATE TABLE Personagem (
CodART integer NOT NULL,
CodFILME integer NOT NULL,
NomePers VARCHAR(25),
Cache numeric(15,2));

ALTER TABLE Filme ADD CONSTRAINT PKFilme PRIMARY KEY(CodFILME);

ALTER TABLE Artista ADD CONSTRAINT PKArtista PRIMARY KEY(CodART);

ALTER TABLE Estudio ADD CONSTRAINT PKEst PRIMARY KEY(CodEst);

ALTER TABLE Categoria ADD CONSTRAINT PKCategoria PRIMARY KEY(CodCATEG);

ALTER TABLE Personagem ADD CONSTRAINT PKPersonagem PRIMARY KEY(CodART,CodFILME);

ALTER TABLE Filme ADD CONSTRAINT FKFilme1Categ FOREIGN KEY(CodCATEG) REFERENCES
Categoria;

ALTER TABLE Filme ADD CONSTRAINT FKFilme2Estud FOREIGN KEY(CodEst) REFERENCES
Estudio;

ALTER TABLE Personagem ADD CONSTRAINT FKPersonagem2Artis FOREIGN KEY(CodART)
REFERENCES Artista;

ALTER TABLE Personagem ADD CONSTRAINT FKPersonagem1Filme FOREIGN KEY(CodFILME)
REFERENCES Filme;

-- Inserindo os dados

insert into artista values(default,'Cameron Diaz',null,'USA','15/07/75');
insert into artista values(default,'Julia Roberts',null,'USA','20/08/67');
insert into artista values(default,'Brad Pitt',null,null,'05/03/70');
insert into artista values(default,'Joaquin Phoenix',null,null,'06/04/72');
insert into artista values(default,'Bradley Cooper',null,'USA','06/06/77');
insert into artista values(default,'Tom Cruise',null,'USA','10/09/64');
insert into artista values(default,'Rodrigo Santoro','Rio de Janeiro','Brasil','12/10/78');
insert into artista values(default,'JungKook',null,'USA','15/07/75');
insert into artista values(default,'V',null,'USA','20/08/67');
insert into artista values(default,'Jimin',null,null,'05/03/70');
insert into artista values(default, 'Caio Castro', null, 'BR', '15/07/75');
insert into artista values(default, 'Larissa Manoella', null, 'BR', '15/07/75');
insert into artista values(default, 'Maria Ximenes', null, 'BR', '27/11/78');

-- Atualizações
update artista
set cidade = 'Rio de Janeiro'
where codart in(11, 12);

update artista
set cidade = 'Coreia'
where codart = 8;

insert into categoria values(default,'Aventura');
insert into categoria values(default,'Romance');
insert into categoria values(default,'Comédia');
insert into categoria values(default,'Ação');
insert into categoria values(default,'Suspense');
insert into categoria values(default,'Drama');
insert into categoria values(default,'Tensão');
insert into categoria values(default,'Terror');
insert into categoria values(default,'Besteirol');

insert into estudio values(default,'Paramount');
insert into estudio values(default,'Disney');
insert into estudio values(default,'Universal');
insert into estudio values(default,'Marvel');
insert into estudio values(default,'DC');
insert into estudio values(default,'Pixar');

insert into filme values(default,'Encontro Explosivo',2010,134,4,1);
insert into filme values(default,'O Besouro Verde',2010,155,1,1);
insert into filme values(default,'Comer, Rezar, Amar',2010,177,2,1);
insert into filme values(default,'Coringa',2019,122,6,1);
insert into filme values(default,'Era uma vez em Hollywood',2020,119,4,2);
insert into filme values(default,'Nasce uma estrela',2018,100,6,1);
insert into filme values(default,'Uncharted',2010,134,4,1);
insert into filme values(default,'O Besouro Azul',2010,155,1,1);
insert into filme values(default,'Comer, Dormir, Viver',2010,177,2,1);
insert into filme values(default,'Elvis',2022,120,null,3);
update filme
set codfilme = 10
where codfilme = 14;
select * from personagem;

insert into personagem values(1,1,'Natalie',10000);
insert into personagem values(1,2,'Tom',10000);
insert into personagem values(5,3,'John',10000);
insert into personagem values(3,2,'Ana',6000);
insert into personagem values(6,5,'Tom',11000);
insert into personagem values(4,4,'John',12000);
insert into personagem values(1,3,'The Rock',10000);
insert into personagem values(3,3,'Tin Tin',10000);
insert into personagem values(5,4,'John Wick',10000);