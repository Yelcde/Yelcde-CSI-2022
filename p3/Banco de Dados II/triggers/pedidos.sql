-- Exemplo 4

Create or replace view vPessoas as
	select nome as nome, 'c' as tipo
	from cliente
	Union
	Select nome, 'v' from vendedor;

select * from vPessoas;

CREATE or replace FUNCTION insere_view_vPessoas()
RETURNS trigger AS $$
	Declare
		v_cod_vend integer;
		v_cod_cli integer;
	Begin
		Select max(codvend)+1 into v_cod_vend from vendedor;
		Select max(codcli)+1 into v_cod_cli from cliente;
	If new.tipo = 'c' then
		Insert into cliente(codcli, nome) values (v_cod_cli,new.nome);
	Else
		Insert into vendedor(codvend,nome) values (v_cod_vend,new.nome);
	End if;
	Return null;
END;
$$ language plpgsql;

Create trigger insViewVPessoas
	Instead of insert on vPessoas
		for each row execute procedure insere_view_vPessoas();

select * from vendedor;
select * from cliente;
select * from vPessoas order by tipo;

insert into vPessoas values('Mercia','v');
insert into vPessoas values('Catarina','c');

-- Exemplo 5

create table tabClienteaudit(atualizacao integer, ultimadata date, quem varchar);

select * from tabClienteaudit;

CREATE OR REPLACE FUNCTION registra_upd_cliente() 
RETURNS TRIGGER AS $$
	declare
		qtd_linhas integer;
	Begin
		select count(*) into qtd_linhas from tabClienteaudit;
	if qtd_linhas = 0 then 
		insert into tabclienteAudit values(1,current_date,current_user);
	else 
		Update tabClienteAudit 
		Set atualizacao = atualizacao + 1, ultimadata = current_date , quem = current_user;
	end if;
return null;
End;
$$ language plpgsql;

CREATE TRIGGER cliente_audit
	AFTER UPDATE ON cliente
		FOR EACH ROW EXECUTE PROCEDURE registra_upd_cliente();

select * from cliente;
update cliente set cidade = 'João Pessoa' Where codcli = 1;
Select * from tabclienteAudit;

-- Exemplo 6

CREATE OR REPLACE FUNCTION impedeAlteração() RETURNS TRIGGER AS $$
Declare
  v_hoje integer;
  v_agora integer;
Begin
    v_hoje := to_number(to_char(current_timestamp,'d'),'99');
    v_agora := to_number(to_char(current_timestamp,'hh24mi'),'9999');
    If v_agora >  1330 then
       RAISE EXCEPTION '%', 'Hora proibida para atualizações' USING ERRCODE = 45000;
    End if;
    If v_hoje = 1 then
       RAISE EXCEPTION '%', 'Dia proibido para atualizações' USING ERRCODE = 45001;    
    End if;
    return new; 
End;
$$ language plpgsql; 

-- drop trigger empnotifTrig on empregado; 

CREATE TRIGGER empnotifTrig
  BEFORE INSERT OR UPDATE ON empregado
    FOR EACH ROW EXECUTE PROCEDURE impedeAlteração();

select * from empregado order by matricula; 
-- delete from empregado where matricula > 12; 

INSERT INTO empregado VALUES (13,'TESTE','Morais','12-03-2020',
							  'Gerente',10000,1,1); 							
select * from empregado order by matricula; 
select current_timestamp; 

select * from empregado order by primeironome; 


-- Exemplo 7

SELECT * FROM INFORMATION_SCHEMA.TRIGGERS