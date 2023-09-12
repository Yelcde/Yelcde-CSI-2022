-- 2. Crie um banco de dados no Postgres chamado “Projetos”. Em seguida, crie as tabelas conforme o esquema seguinte que deve estar compatível com o modelo conceitual e lógico anteriores. Observe que a chave primária da tabela Atuação é composta. Observe também que os tipos de codeng e codproj nas tabelas Engenheiro e Projeto são serial. 
create table engenheiro (
	codeng serial not null,
	nome varchar(30),
	salario numeric(15, 2),
	constraint engenheiroPK primary key (codeng)
);

create table projeto (
	codproj serial not null,
	titulo varchar(30),
	area varchar(30)
);

alter table projeto add constraint projetoPK primary key (codproj);

create table atuacao (
	codeng integer not null,
	codproj integer not null,
	função varchar(30),
	constraint atuacaoPK primary key (codeng, codproj),
	constraint atuacaoFK_codeng foreign key(codeng) references engenheiro(codeng),
	constraint atuacaofk_codproj foreign key(codproj) references projeto(codproj)
);

-- 5. Crie um check de validação em uma das tabelas. 

alter table engenheiro add constraint salario_notNull check(salario > 0);

-- 6. Insira 5 engenheiros.

insert into engenheiro values(default, 'João Silva', 5000);
insert into engenheiro values(default, 'Maria Joaquina', 5200);
insert into engenheiro values(default, 'Pedro Lucas', 4500);
insert into engenheiro values(default, 'Gusttavo Lima', 7000);
insert into engenheiro values(default, 'Jimin', 5000);

-- 7. Insira 5 projetos. 

insert into projeto values(default, 'Projeto A', 'Tecnologia');
insert into projeto values(default, 'Projeto B', 'Saúde');
insert into projeto values(default, 'Projeto C', 'Educação');
insert into projeto values(default, 'Projeto D', 'Meio Ambiente');
insert into projeto values(default, 'Projeto E', 'Artes');

-- 8. Insira relacionamentos entre os projetos e engenheiros.
insert into atuacao values (1, 1, 'Engenheiro de Software');
insert into atuacao values (2, 2, 'Engenheiro Civil');
insert into atuacao values (3, 3, 'Engenheiro Elétrico');
insert into atuacao values (4, 4, 'Engenheiro de Produção');
insert into atuacao values (5, 5, 'Engenheiro Mecânico');

-- 9. Elabore consultas conforme se pede a seguir:

-- a. Mostre os nomes dos engenheiros cujo salário seja menor que 15000.
select nome 
from engenheiro 
where salario > 15000;

-- b. Apresente os nomes dos engenheiros que possuem a função “Analista” em projetos ou uma outra existente em seu banco.
select e.nome 
from engenheiro e
join atuacao a on e.codeng = a.codeng 
where função = 'Engenheiro Mecânico';

-- c. Mostre a quantidade de engenheiros por área de projeto.
select count(e.codeng)
from engenheiro e
join atuacao a on e.codeng = a.codeng
join projeto p on a.codeng = p.codproj
group by p.area;

-- d. Verifique os nomes dos engenheiros que ganham acima da média salarial de todos os engenheiros.
select nome
from engenheiro
where salario >( select avg(salario)
				 from engenheiro
			   );

-- 10. Execute e analise o comando seguinte:
SELECT SUBSTR(e.nome, 1, 1) AS PrimeiraLetra, COUNT(*) AS Contagem
FROM engenheiro e
GROUP BY SUBSTR(e.nome, 1, 1);

-- 11. Verifique o seguinte comando:
select nome
from engenheiro
where codeng in (select codeng
				 from atuacao
				 where codproj in (select codproj
								   from projeto
								   where area like 'Tecnologia'));

-- Reescreva-o, desta vez, usando JOIN.
select e.nome
from engenheiro e
join atuacao a on e.codeng = a.codeng
join projeto p on a.codeng = p.codproj
where p.area like 'Tecnologia';