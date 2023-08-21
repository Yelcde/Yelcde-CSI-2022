-- Criando as tabelas
CREATE TABLE Cliente (
CodCLI Serial PRIMARY KEY,
Nome Varchar(30),
Endereco Varchar(30),
Telefone Varchar(12),
InscE Varchar(10),
CNPJ Varchar(10),
Cidade Varchar(15),
UF Varchar(2)
);

CREATE TABLE Produto (
CodPROD Serial not null,
Descricao Varchar(20),
Valor Numeric(10,2),
Unidade Char(2),
constraint pk_prod primary key(CodPROD));

CREATE TABLE Pedido (
NumPED Serial PRIMARY KEY,
PrazoEntrega Integer,
Data Date,
CodCLI Integer,
CodVEND Integer,
FOREIGN KEY(CodCLI) REFERENCES Cliente (CodCLI)
);

CREATE TABLE Vendedor (
CodVEND Serial PRIMARY KEY,
Nome Varchar(30),
DataNasc Date,
SalarioFixo Numeric(12,2),
FaixaComissao Char(1)
);

CREATE TABLE ItensPedido (
NumPED Integer,
CodPROD Integer,
Quantidade Integer,
constraint pk_itens PRIMARY KEY(CodPROD,NumPED),
constraint fk_prod FOREIGN KEY(CodPROD) REFERENCES Produto (CodPROD),
constraint fk_ped FOREIGN KEY(NumPED) REFERENCES Pedido (NumPED)
);
 
ALTER TABLE Pedido ADD FOREIGN KEY(CodVEND) REFERENCES Vendedor (CodVEND);

-- Povoando a tabela cliente

insert into cliente values(default,'Claudia Dias',null,null, '564325','786534','Recife','PE');
insert into cliente values(default,'Joaquim Moraes','Epitacio Pessoa, 123','32425643', '500925','789004','Joao Pessoa','PB');
insert into cliente values(default,'Janaina Rodrigues','Rui Carneiro, 342',null, '764325','386534','Joao Pessoa','PB');
insert into cliente values(default,'Maria Portela','Boa Viagem, 345','76435678', null,null,'Recife','PE');
insert into cliente values(default,'Ana Moura','Nego, 321','32465432', '87325','780978','Joao Pessoa','PB');
insert into cliente values(default,'Cassandra Doura',null,null, '786525','79876','Recife','PE');
insert into cliente values(default,'Cicero Novaes',null,null, '123525','432534','Natal','RN');
insert into cliente values(default,'Marcos Araruna','Sergipe,267','43265432', '900325','800534','Joao Pessoa','PB');
select * from cliente;

-- Povoando a tabela vendedor

insert into vendedor values(default,'Juan Gomes', '28/07/1978', 2300.80,'C');
insert into vendedor values(default,'Joao Peregrino', '20/05/1970', 3300.80,'B');
insert into vendedor values(default,'Carla Gomes', '12/02/1984', 5300.80,'A');
insert into vendedor values(default,'Josefa Cirino', '23/08/1990', 2300.80,'C');
insert into vendedor values(default,'Ariane Dutra', '28/09/1993', 3300.80,'B');
select * from vendedor;

-- Povoando a tabela produto

insert into produto values(default,'Queijo', 22.00, 'KG');
insert into produto values(default,'Chocolate', 6.12, 'G');
insert into produto values(default,'Leite', 10.00, 'L');
insert into produto values(default,'Linho', 24.00, 'M');
insert into produto values(default,'Feijao', 12.00, 'KG');
insert into produto values(default,'Açucar', 9.00, 'KG');
select * from produto;

-- Povoando a tabela pedido

insert into pedido values(default,23, '12/09/2019', 1,1);
insert into pedido values(default,10, '21/09/2020', 2,1);
insert into pedido values(default,5, '25/08/2020', 3,4);
insert into pedido values(default,2, '28/07/2020', 4,2);
insert into pedido values(default,3, '28/09/2020', 5,3);
insert into pedido values(default,3, '26/10/2020', 5,2);
select * from pedido;

-- Povoando a tabela itenspedido

insert into itenspedido values(2,2, 35);
insert into itenspedido values(2,3, 30);
insert into itenspedido values(1,1, 10);
insert into itenspedido values(4,5, 35);
insert into itenspedido values(5,4, 10);
insert into itenspedido values(3,4, 35);
insert into itenspedido values(1,5, 10);
select * from itenspedido;

-- Consultas iniciais com pedidos  

Select numped, codprod, quantidade
    From itenspedido
    Where quantidade > 20;
		
Select descricao, unidade, valor
	From produto
	Where unidade = 'KG' and valor > 4.0
	
Select codprod, descricao, valor
	From produto
	Where valor between 5.00 and 15.50;

Select faixacomissao as identificador, nome as nome
	From vendedor
	Where faixacomissao IN ('A','B');
	
Select InscE, nome as nome
	From cliente
	Where InscE is null;
	
Select faixacomissao as identificador, (salariofixo * 1.15) + 120 as "Novo Salário", nome
From vendedor
Where faixacomissao = 'C'
Order by nome;

Select  *
From Cliente
Where nome like '________A';
 
Select  *
From Cliente
Where nome like '________a'

-- Aula 04 - Banco Pedidos 

Select nome
	From cliente
	Where cidade = 'Joao Pessoa';
	
	select * from cliente; 
	select * from pedido; 
	select * from vendedor; 
	
Select nome, UF 
from cliente JOIN pedido 
        on cliente.codcli = pedido.codcli
where UF in ('PB','PE') and prazoentrega > 15;

-- Operações de conjuntos 

(Select nome
    from cliente
    where cidade like 'Recife')
    UNION
(Select nome
 from vendedor);

select codcli
  from cliente
  where UF = 'PB'
  INTERSECT
select codcli
   from pedido;

select codcli
  from cliente
Except
select codcli
   from pedido;
   
select * from cliente order by codcli; 

select * from pedido order by numped; 

-- produto cartesiano

Select cliente.codcli, nome, numped, pedido.codcli
from cliente, pedido;

Select cliente.codcli, nome, numped, pedido.codcli
from cliente cross JOIN pedido;

-- Joins

Select cliente.codcli, pedido.codcli, nome, numped
from cliente, pedido
where cliente.codcli = pedido.codcli;

Select cliente.codcli, pedido.codcli, nome, numped
from cliente JOIN pedido on cliente.codcli = pedido.codcli;

Select v.nome 
From vendedor v join pedido p 
        on v.codvend =  p.codvend
     join itenspedido i on p.numped = i.numped 
     join produto pr on i.codprod = pr.codprod
Where i.quantidade > 5 and pr.descricao = 'Chocolate'; 

-- Group by 

Select cidade, count(*)
from cliente C join pedido P on C.codcli = P.codcli 
join vendedor V on P.codvend = V.codvend 
Group by cidade;

select cliente.uf, count(*) 
from cliente
group by uf
having count(*) > 2; 

select v.faixacomissao, avg(salariofixo)
from vendedor v
where v.faixacomissao <> 'B'
group by v.faixacomissao
having avg(salariofixo) > 3000; 

select v.faixacomissao, min(salariofixo), max(salariofixo)
from vendedor v
group by v.faixacomissao