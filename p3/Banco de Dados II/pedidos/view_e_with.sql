CREATE or replace VIEW Prquilo(codigo, descricao,unidade)
AS Select codprod,descricao,unidade
	From produto
	Where unidade = ‘KG’;
	
CREATE OR REPLACE VIEW VendSal(codigo,nome,salario)
AS Select codvend,nome,salariofixo
	From vendedor;
	
Insert into Prquilo
values (110,’Arroz’,’KG’);

select * from Prquilo;

Update Prquilo
Set descricao = ‘Arroz XX’
Where codigo = 110;

create or replace view ProdutodescA 
as select codprod,descricao
	from produto
	where descricao like 'A%'
	with check option; 
	
select * from ProdutodescA;

insert into ProdutodescA
values(40, 'Manteiga');

insert into ProdutodescA
values(41, 'Azeite');

With ClientesAtivos 
AS(SELECT codcli 
   from Cliente 
   WHERE endereco is not null),
ClientesInativos 
AS(SELECT codcli 
   from Cliente 
   WHERE endereco is null )
SELECT * FROM ClientesAtivos
UNION
SELECT * FROM ClientesInativos
