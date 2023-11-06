-- 1

select 123.456::decimal;
select 123::smallint;
Select coalesce(null,'Nada');

-- 2

select matricula, salario from empregado order by salario;
insert into empregado values (13,'João', 'Guedes',current_date,'Analista de Sistemas Junior',940.00,null,1);
insert into empregado values (14,'José', 'Batista',current_date,'Analista de Sistemas Pleno',1200.00,1,1);

Do $$
	Declare
  		cursor_emp cursor for select salario from empregado;
  		total_emp_recebe_menos integer default 0;
  		total_emp integer default 0;
  		percentual decimal;
	Begin
  		select count(*) into total_emp from empregado;
  		for i in cursor_emp loop
  			If i.salario < 1350.00 then 
				total_emp_recebe_menos = total_emp_recebe_menos + 1;
  	  		end if;
 		end loop;
  		raise notice 'Empregados que recebem menos que o salário: %',total_emp_recebe_menos;
  		raise notice 'Total de Empregados: %',total_emp;
  		percentual = round((total_emp_recebe_menos::decimal /total_emp::decimal) *100);
  		raise notice 'Percentual de empregados que recebem menos que o salário: % %%',percentual;
end; $$;

-- a) O que ele faz? Explique. A função cria um cursor pegando todos os salarios existente na tabela empregado, após isso o código verifica se a quantidade de empregados com o salario menor que 1350 e adiciona ele em uma variavel para fazer a conta e mostrar uma porcentagem
-- b) Transforme-o em uma procedure armazenada.
create or replace procedure percent_emp()
	language plpgsql
	as $$
		Declare
  		cursor_emp cursor for select salario from empregado;
  		total_emp_recebe_menos integer default 0;
  		total_emp integer default 0;
  		percentual decimal;
		Begin
  			select count(*) into total_emp from empregado;
  			for i in cursor_emp loop
  				If i.salario < 1350.00 then 
					total_emp_recebe_menos = total_emp_recebe_menos + 1;
  	  			end if;
 			end loop;
  			raise notice 'Empregados que recebem menos que o salário: %',total_emp_recebe_menos;
  			raise notice 'Total de Empregados: %',total_emp;
  			percentual = round((total_emp_recebe_menos::decimal /total_emp::decimal) *100);
  			raise notice 'Percentual de empregados que recebem menos que o salário: % %%',percentual;
	end$$
-- c) Execute a procedure recém-criada (use o comando Call). Os resultados obtidos foram iguais aos obtidos com o bloco anterior?
call percent_emp();

-- 3 Desabilite os triggers existentes para a tabela Empregado.
alter table empregado disable trigger all;

-- 4 Teste o trigger seguinte. Explique o que ele faz.
CREATE OR REPLACE function testa_salario() returns trigger
	as $$
		Begin
			If new.salario > 20000 then
    			raise exception 'salario alto';
			end if;
			return new;
			exception
   				when raise_exception then
       				Raise notice 'Tentativa de aumento exagerada!!! %', new.salario;
       				return null;
 		end;
	$$ LANGUAGE plpgsql; 
 
create trigger verSalario
 	BEFORE INSERT OR UPDATE OF salario ON empregado
 		FOR EACH ROW Execute procedure testa_salario();

insert into empregado(matricula,primeironome,salario,gerente,coddepto) values (15,'Poliana15',7000,2,2);
insert into empregado(matricula,primeironome,salario,gerente,coddepto) values (16,'Poliana16',27000,2,2);
select * from empregado where primeironome like 'Poliana%';

-- O código está inserindo valores na tabela empregado, mas antes de adicionar o valor na tabela o trigger vai verificar se o salario for maior que 20000, se for não vai ser inserido e vai mostrar uma mensagem informando isso.

-- 5 Crie a tabela seguinte (vale 0,3):
CREATE TABLE testeINC (
	id integer NOT NULL,
    Descricao VARCHAR(50) NOT NULL
);
ALTER TABLE testeINC ADD CONSTRAINT testepk PRIMARY KEY (id);

create or replace function add_pk() returns trigger
	as $$
		declare
			novoId integer;
		begin
			select coalesce(max(id), 0) + 1 into novoId from testeINC; 
			new.id = novoId;
			return new;
		end;
	$$ language plpgsql;
	
create trigger autoInc
	before insert or update of id on testeINC
		for each row execute procedure add_pk();


insert into testeINC (Descricao) values('oioioi');
insert into testeINC (Descricao) values('eieiei');
insert into testeINC (Descricao) values('uiuiui');
insert into testeINC (Descricao) values('dadada');
select * from testeINC;