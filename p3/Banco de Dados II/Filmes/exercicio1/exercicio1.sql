-- 4. Verifique a estrutura das tabelas após sua criação: ARTISTA, FILME, CATEGORIA, ESTÚDIO e PERSONAGEM. Estão compatíveis com os modelos?

select * from artista;
select * from filme;
select * from categoria;
select * from estudio;
select * from personagem;

-- 5. Rode os scripts de inserção dos dados de cada tabela, conforme scripts passados.

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

insert into filme values(default,'Encontro Explosivo',2010,134,4,1);
insert into filme values(default,'O Besouro Verde',2010,155,1,1);
insert into filme values(default,'Comer, Rezar, Amar',2010,177,2,1);
insert into filme values(default,'Coringa',2019,122,6,1);
insert into filme values(default,'Era uma vez em Hollywood',2020,119,4,2);
insert into filme values(default,'Nasce uma estrela',2018,100,6,1);
insert into filme values(default,'Uncharted',2010,134,4,1);
insert into filme values(default,'O Besouro Azul',2010,155,1,1);
insert into filme values(default,'Comer, Dormir, Viver',2010,177,2,1);

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

insert into personagem values(1,1,'Natalie',10000);
insert into personagem values(1,2,'Tom',10000);
insert into personagem values(5,3,'John',10000);
insert into personagem values(3,2,'Ana',6000);
insert into personagem values(6,5,'Tom',11000);
insert into personagem values(4,4,'John',12000);
insert into personagem values(1,3,'The Rock',10000);
insert into personagem values(3,3,'Tin Tin',10000);
insert into personagem values(5,4,'John Wick',10000);

-- 6. Faça um select geral para verificar o conteúdo de cada uma das tabelas.

select * from artista;
select * from filme;
select * from categoria;
select * from estudio;
select * from personagem;

-- 7. Em seguida, insira mais três registros (de sua autoria) em cada tabela.

insert into artista values(default,'JungKook',null,'USA','15/07/75');
insert into artista values(default,'V',null,'USA','20/08/67');
insert into artista values(default,'Jimin',null,null,'05/03/70');

insert into filme values(default,'Uncharted',2010,134,4,1);
insert into filme values(default,'O Besouro Azul',2010,155,1,1);
insert into filme values(default,'Comer, Dormir, Viver',2010,177,2,1);

update filme set codfilme = 8
where codfilme = 11;
update filme set codfilme = 9
where codfilme = 12

insert into categoria values(default,'Tensão');
insert into categoria values(default,'Terror');
insert into categoria values(default,'Besteirol');

insert into estudio values(default,'Marvel');
insert into estudio values(default,'DC');
insert into estudio values(default,'Pixar');

insert into personagem values(1,3,'The Rock',10000);
insert into personagem values(3,3,'Tin Tin',10000);
insert into personagem values(5,4,'John Wick',10000);

-- 8. Verifique quais são os artistas cadastrados ordenados pelo nome.

select * from artista 
order by nomeart;

-- 9. Selecione os artistas que têm o nome iniciando com a letra ‘B’.
select nomeart as "Artista"
from artista
where nomeart like 'B%';

-- 10. Verifique os filmes que foram lançados em 2019.
select ano 
from filme 
where ano = 2019

-- 11. Atualize o cachê dos artistas em 15%.
update personagem
set cache = cache * 1.15

-- 12. Atualize o país de 3 artistas à sua escolha.
update artista 
set pais = 'USA'
where codart in(1, 2, 5);

-- 13. Insira 2 artistas brasileiros.
insert into artista values(default, 'Caio Castro', null, 'BR', '15/07/75');
insert into artista values(default, 'Larissa Manoella', null, 'BR', '15/07/75');

-- 14. Delete 1 artista recentemente incluído que não seja brasileiro.
delete from artista
where nomeart = 'Brad Pitt'