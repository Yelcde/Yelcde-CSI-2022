-- 1. Verifique o seguinte código:

DO $$
	Declare
		nomeCli varchar(40);
		qtdelinhas integer;
	BEGIN
		select nome into nomeCli from cliente where codcli = 2;
		GET DIAGNOSTICS qtdelinhas := ROW_COUNT;
		raise notice 'Nome cliente = %', nomeCli;
		raise notice 'Quantidade de registros retornados = %',qtdelinhas;
END$$;

-- a) Explique o que ele faz. Quantos registros são retornados?? Ele seleciona o nome do cliente cujo o código é 2 e conta os registros daquele cliente através da quantidade de linhas.

-- 2. Verifique o seguinte código, explique o que ele faz e mostra. Depois, explique para que serve o ROWTYPE. O código seleciona todos as colunas da tabela cliente e seus tipos, após isso ele verifica cada campo da variável de registro e vai adicionando valor por valor. O rowtype não pega o tipo de apenas uma coluna, mas de todas as colunas e cria campos com seus respectivos tipos.

DO $$
	DECLARE
		clireg cliente%ROWTYPE;
		info varchar(50);
	BEGIN
		clireg.codcli := 13;
		clireg.nome := 'Ariane Botelho';
		clireg.cidade := 'Campina Grande';
		Select clireg.nome || ' trabalha em ' || clireg.cidade into info;
		raise notice 'Informação = %', info;
END$$;

-- Questao 3

-- Criando tabela testa_bloco
create table testa_bloco (coluna1 integer primary key, coluna2 date);

-- Fazendo teste
do $$
	declare 
		i integer = 0;
	begin 
		while i < 10 loop
			if mod(i, 3) = 0 then 
				insert into testa_bloco values(i, current_date);
			end if;
			i := i + 1;
		end loop;
end $$;

select * from testa_bloco;







