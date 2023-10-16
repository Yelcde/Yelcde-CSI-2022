Explain select * from empregado
where salario > 4000;

--  Qual o custo dessa consulta? 0.00..14.25
-- Quantos registros serão obtidos? 113
-- Execute efetivamente a consulta e informe seu tempo de resposta. 129 ms

Explain select * from empregado
where salario > 4000;

--  Qual o custo dessa consulta? 0.00..14.25
-- Quantos registros serão obtidos? 113
-- Execute efetivamente a consulta e informe seu tempo de resposta. 129 ms

create table testaEMP as select * from empregado;
select * from testaEMP;

-- Quando o planejador de consultas monta o plano de execução da consulta, ele pode fazer uso de índices, caso existam. Efetue os testes seguintes.

-- execute o bloco anônimo seguinte completo (do DO até o $$;) e não linha a linha. Tempo: 3 min 41 secs
DO $$
DECLARE i int:= 0;
BEGIN
	WHILE I <= 10000000 LOOP
		INSERT INTO testaEMP select * from empregado;
		I := I + 1;
	END LOOP;
END$$;

Select primeironome from testaEmp where gerente = 2; -- Tempo: 39 secs 780 ms
EXPLAIN Select primeironome from testaEmp where gerente = 2; 

-- Criando indice
create index testaEmpindex on testaEmp(gerente); -- Tempo: 51 secs 112 msec

-- Testando com Indice
Select primeironome from testaEmp where gerente = 2;
EXPLAIN Select primeironome from testaEmp where gerente = 2;

-- Compare os resultados e explique o que aconteceu. Houve melhora no tempo de resposta da consulta com o índice? Houve melhora, com o uso de indices foi possivel se criar uma btree o que facilita e turbina muito a busca

--  Verifique os seguintes comandos e informe a quantidade de páginas de disco ocupadas pelas tabelas EMPREGADO e TESTAEMP:
select relpages from pg_class where relname = 'empregado'; -- 0
select relpages from pg_class where relname = 'testaemp'; -- 689656

-- Quais índices existem para a tabela EMPREGADO? Qual outro índice poderia ser criado para essa tabela? Qual a justificativa para sua criação?
-- Existe o indice testaEmpidex. Por matricula já que a matricula é única.

-- Crie um índice indCargo para o campo “cargo” da tabela Empregado. Em que situações este índice é indicado? Explique.
create index indCargo on testaEmp(cargo); -- Tempo: 1 min 40 secs
-- É usado quando a coluna (ou colunas) é (são) usada(s) frequentemente em cláusulas WHERE, order by (e order by com Limit), group by ou em joins

-- Explique a frase: “os índices são estruturas que organizam referências à localização dos dados reais das tabelas”.
-- Os Indices ajudam na criação de estruturas de dados Btrees para a rapida localização de dados