create or replace function cria_filme(f_titulo filme.titulo%type, f_ano filme.ano%type, f_duracao filme.duracao%type, f_categoria categoria.desccateg%type, f_estudio estudio.nomeest%type)
	returns void
	as $$
		declare codigocateg integer;
		declare codigoestudio integer;
		begin
-- 			Pegando o código da categoria
			select codcateg into codigocateg from categoria where desccateg = f_categoria;
			if not found then
				insert into categoria(desccateg) values(f_categoria) returning codcateg into codigocateg; -- retorna já adicionando em uma variavel
			end if;
			
-- 			Pegando o código do estúdio
			select codest into codigoestudio from estudio where nomeest = f_estudio;
			if not found then
				insert into estudio(nomeest) values(f_estudio) returning codest into codigoestudio; -- retorna já adicionando em uma variavel
			end if;
			insert into filme values(default, f_titulo, f_ano, f_duracao, codigocateg, codigoestudio);
		end;
	$$ language 'plpgsql';
	
drop function cria_filme2;
select cria_filme('Homem Aranha',2021,130,'Aventura','Universal');
select cria_filme('A História de Robin Hood',1993,104,'Musical','Brooksfilms');
	
select f.titulo, f.ano, f.duracao || ' min', c.desccateg, e.nomeest
from filme f join categoria c on f.codcateg = c.codcateg
join estudio e on f.codest = e.codest;

create or replace function cria_filme2(f_titulo filme.titulo%type, f_ano filme.ano%type, f_duracao filme.duracao%type, f_categoria categoria.desccateg%type, f_estudio estudio.nomeest%type)
	returns void
	as $$
		declare codigocateg integer;
		declare codigoestudio integer;
		declare msg varchar(25);
		begin
-- 			Pegando o código da categoria
			select codcateg into strict codigocateg from categoria where desccateg = f_categoria;
-- 			Pegando o código do estúdio
			select codest into strict codigoestudio from estudio where nomeest = f_estudio;
			insert into filme values(default, f_titulo, f_ano, f_duracao, codigocateg, codigoestudio);
			exception
				When No_data_found then
					msg = 'Nenhum produto encontrado';
					Return msg;
				When others then
					Return 'Erro desconhecido ';
		end;
	$$ language 'plpgsql';