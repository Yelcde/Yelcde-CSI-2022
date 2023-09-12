-- 1. 	Faça um select geral nas cinco tabelas e observe seus relacionamentos.
select * from artista;
select * from filme;
select * from categoria;
select * from estudio;
select * from personagem;

-- 2. 	Em seguida, realize a seguinte inserção e consulta:
insert into filme values(default,'Elvis',2022,120,null,3);
select * from filme;

-- 3. 	Verifique quais os títulos dos filmes que possuem duração maior que 120 min?
select titulo 
from filme 
where duracao > 120;

-- 4. 	Na tabela ARTISTA, quais artistas possuem cidade nula? Após a consulta realizada, atualize as cidades nulas encontradas para três artistas.
select codart as "Código", nomeart as "Artista", cidade as "Cidade"
from artista 
where cidade is null;

update artista
set cidade = 'Rio de Janeiro'
where codart in(11, 12);

update artista
set cidade = 'Coreia'
where codart = 8;

-- 5. 	Qual a descrição da categoria do filme ‘Coringa’?
select f.titulo as "Filme", c.desccateg as "Categoria"
from filme f join categoria c 
on f.codcateg = c.codcateg
where codfilme = 4;

-- 6. 	Mostre os títulos de filmes, com seus nomes de estúdios e nomes de suas categorias.
select f.titulo as "Filme", e.nomeest as "Estudio", c.desccateg as "Categoria"
from filme f join estudio e
on f.codest = e.codest
join categoria c 
on f.codcateg = c.codcateg;

-- 7. 	Qual o nome dos artistas que fizeram o filme ‘Encontro Explosivo’?
select 