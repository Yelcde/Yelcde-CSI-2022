-- Adicionando dois campos na tabela produto
Alter table produto add status varchar(40);
Alter table produto add quantest integer;
Update produto
Set quantest = 45
Where codprod = 1;
Select * from produto;

-- Bloco Anônimo
Do $$
	Declare qtd_atual produto.quantest%type;
	Begin
		select quantest into qtd_atual from produto
		where codprod = 1;
		if qtd_atual > 30 then
			update produto
			set status = 'Estoque dentro do esperado'
			where codprod = 1;
		else
			update produto
			set status = 'Estoque fora do limite minimo'
			where codprod = 1;
		end if;
End$$;

select * from produto;
update produto set status = null where codprod = 10;
select atualizaStatus(6);
-- Altere o código do produto conforme seus dados.

-- Crie a função pedida e execute-a seguindo os comandos:
create or replace function atualizaStatus (codigo integer)
	returns void
	as $$
		begin
			if codigo > 30 then 
				update produto
				set status = 'Estoque dentro do esperado'
				where codprod = codigo;
			else
				update produto
				set status = 'Estoque fora do limite minimo'
				where codprod = codigo;
			end if;
		end;
	$$ language 'plpgsql';
	
-- Analise e execute a função seguinte. Explique o que ela faz.
create or replace function getSumSalario()
	returns numeric
	as $$
		Declare
		salcomp numeric;
		v record;
		Begin
			Salcomp = 0;
			for v in (select salariofixo from vendedor where salariofixo is not null) loop
				salcomp = salcomp + v.salariofixo;
			end loop;
			return salcomp;
		end;
	$$ LANGUAGE 'plpgsql';
select getSumsalario();
-- A função esta pegando todos os registros de funcionários onde o salário fixo não é nulo e vai somando numa variável interna e depois retorna essa soma

-- Crie uma tabela Fornecedor
create table fornecedor (
	cod serial not null,
	nome varchar(30),
	cnpj varchar(15),
	email varchar(15),
	constraint pk_fornecedor primary key (cod)
);

create or replace function inserirDados(nome varchar(30), cnpj varchar(15), email varchar(15))
	returns void
	as $$
		begin
			insert into fornecedor values(default, nome, cnpj, email);
		end;
	$$ language 'plpgsql';

select inserirDados('João', '1234', 'xxx@gmail.com');
select inserirDados('Luana', '5678', 'xxx@gmail.com');
select inserirDados('Joaquim', '9101112', 'xxx@gmail.com');
select inserirDados('Ludmilla', '131415', 'xxx@gmail.com');
select * from fornecedor;


-- Desenvolva uma função armazenada (showFornecedor)
create or replace function showFornecedor()
	returns void
	as $$
		declare
-- 			v record; Não é necessário declarar essa variável já que estou declarando o cursor fora do for
			f_fornecedor cursor for select * from fornecedor;
		begin
			for v in f_fornecedor loop -- A variável v é automaticamente declarado com o tipo de f_fornecedor
				raise notice '%--%--%', v.cod, v.nome, v.email;
			end loop;
		end;
	$$ language 'plpgsql';

select showFornecedor();