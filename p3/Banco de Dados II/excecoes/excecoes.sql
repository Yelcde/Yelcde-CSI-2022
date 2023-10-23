select * from artista;

select verificaArt(11);

create or replace function verificaArt(codigo integer)
	returns varchar
	as $$
	declare nome varchar(25);
		begin
			select nomeart into nome from artista where codart = codigo;
			if not found then
				return 'Nenhum artista com esse código foi encontrado.';
			end if;
			return nome;
		end;
	$$ language 'plpgsql';
	

select verificaart2(111);
	
create or replace function verificaart2(integer)
	returns varchar
	As $$
		Declare r record;
		begin
			select into r * from artista where codart = $1;
			if not found then RAISE EXCEPTION 'Artista não existente--> %', $1 -- O dolar e um numero é usado para quando a função tem mais de um argumento e eu não tenho nomes ou acho mais comodo usar esse modo
				USING HINT = 'Por favor, verifique o código do artista';
			end if;
			return r.nomeart;
		End; 
	$$ LANGUAGE 'plpgsql';
	
select * from artista;

select verificaArt(11);

create or replace function verificaArt(codigo integer)
	returns varchar
	as $$
	declare nome varchar(25);
		begin
			select nomeart into nome from artista where codart = codigo;
			if not found then
				return 'Nenhum artista com esse código foi encontrado.';
			end if;
			return nome;
		end;
	$$ language 'plpgsql';
	

select verificaart2(111);
	
create or replace function verificaart2(integer)
	returns varchar
	As $$
		Declare r record;
		begin
			select into r * from artista where codart = $1;
			if not found then RAISE EXCEPTION 'Artista não existente--> %', $1 -- O dolar e um numero é usado para quando a função tem mais de um argumento e eu não tenho nomes ou acho mais comodo usar esse modo
				USING HINT = 'Por favor, verifique o código do artista';
			end if;
			return r.nomeart;
		End; 
	$$ LANGUAGE 'plpgsql';
	
select * from estudio;
select testains(4,'Teste');
select testains(5,'Teste');
	
CREATE OR REPLACE FUNCTION testains(cod integer,nome varchar(25))
	RETURNS integer 
	AS $$
		BEGIN
			Insert into estudio(codest,nomeest) values (cod,nome);
			Return 1;
			EXCEPTION
				WHEN unique_violation THEN
					raise notice 'Já existe esse registro';
					return -1;
				WHEN OTHERS THEN
					-- fazer algo
					RETURN -1;
		END;
	$$ LANGUAGE plpgsql;

