-- 1
Create or Replace Function trocaNome()
	Returns trigger as $$
		declare msg varchar(40);
		Begin
			msg = 'Nome ' || old.nomeart || ' mudou para ' || new.nomeart;
			raise notice 'Foi feito: %',msg;
			return null;
		End;
	$$ LANGUAGE plpgsql;
	
CREATE TRIGGER veNome 
	AFTER UPDATE of nomeart ON Artista
		FOR EACH ROW EXECUTE PROCEDURE trocaNome();
		
select * from artista;
update artista
set nomeart = 'Brad Pitt'
where nomeart = 'TROCA';

-- a) O que o trigger faz? Ele é uma função que é acionada antes ou após uma ação
-- b) Como você realizou o teste do trigger? Como ele foi “disparado”? Após algum registro ser atualizado na tabela artista ele ativa o trigger que chama a função
-- c) O que são os objetos “old” e “new”? O objeto old é a versão atual do campo e a new é a versão que será

-- 2
create table filmeLog (
	usuario varchar(20),
	operacao char(1),
	dataHora timestamp
);

create or replace function logFilme()
	returns trigger as $$
		begin
			insert into filmeLog values(user, SUBSTR(tg_op,1,1), now());
			return null;
		end;
	$$ language plpgsql;
	
create trigger opeFilme
	after insert or delete or update on filme
		for each row execute procedure logFilme();

insert into filme values(default,'Didi: O Fantasma Bundão',2007,134,4,1);

select * from filmeLog