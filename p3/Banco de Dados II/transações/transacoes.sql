-- Aula 08 Transações 

-- Parte 01
-- desabilite o autocommit; 

-- Iniciando transação
select * from vendedor;
insert into vendedor values(default,'Melissa Gonçalves', '28/07/1988', 3300.80,'B');
insert into vendedor values(default,'Debora Maciel', '20/04/1990', 3300.80,'B');
insert into vendedor values(default,'Alicia Silva', '28/06/1998', 2300.80,'C');
select * from vendedor;
commit; 

-- novo teste de transação

-- Início da nova transação

select * from vendedor;
insert into vendedor values(default,'Moacir Ribeiro', '27/07/1988', 3300.80,'B');
insert into vendedor values(default,'Daniel Moura', '20/03/1990', 3300.80,'B');
insert into vendedor values(default,'Alvaro Soares', '28/04/1998', 2300.80,'C');
select * from vendedor;

-- supondo uma exceção - if exception ... then 
rollback; 
-- final da transação

select * from vendedor;

-- Parte 02
-- User 1:postgres
-- Criação de outro usuário caso ainda não tenha 
CREATE ROLE jycc LOGIN
  PASSWORD 'bd2' SUPERUSER CREATEDB CREATEROLE ;
-- crie conexão com novo usuário e deixe-a aberta em outra query tool 

-- delete from vendedor where codvend > 11; 

Grant all on vendedor to jycc;

--Iniciando a transação 
select * from vendedor; 
insert into vendedor values(12,'Clovis Paulo', '12/01/1994', 5300.80,'A');
Select * from vendedor;
commit;
select * from vendedor;

-- novo teste de transação
insert into vendedor values(40,'Augusto Paulo', '12/03/1996', 5300.80,'A');
commit; 

-- Parte 03
-- Nova transação

Begin;
UPDATE vendedor
 SET salariofixo = 6000
 WHERE codvend = 1;
SAVEPOINT a_v1;
UPDATE vendedor
 SET salariofixo = 5000
 WHERE codvend = 2;
SAVEPOINT a_v2;
Select * from vendedor; 
SELECT sum(salariofixo) FROM vendedor;
ROLLBACK TO SAVEPOINT a_v1;
SELECT SUM(salariofixo) FROM vendedor;
Select * from vendedor; 
UPDATE vendedor
 SET salariofixo = 5000
 WHERE codvend = 2;
Select * from vendedor; 
COMMIT;