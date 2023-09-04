-- 1.   Para a tabela artista, crie uma view artistaV com os seguintes campos: codart, nomeart, datanasc. Renomeie “codart” para “Código” e “nomeart” para “Nome” na view. Liste o conteúdo da view criada.
create or replace view artistaV(codigo, nome, datanasc)
as select codart, nomeart, datanasc
	from artista;
select * from artistaV;

-- 2.    Crie uma view filmeV com os seguintes campos: titulo,duração, ano, estúdio (nome do estúdio). Liste, em seguida, seu conteúdo.
create or replace view filmeV(titulo, duração, ano, estudio)
as select f.titulo, f.duracao, f.ano, e.nomeest
	from filme f join estudio e
	on f.codest = e.codest;
	
select * from filmeV;

-- 3.   Faça a inserção da artista “Mariana Ximenes” com a data de nascimento ‘27/11/78’ através da view artistaV. Como foi possível inserir por meio da view? Explique.
insert into artistaV
values(default, 'Maria Ximenes', '27/11/78'); 