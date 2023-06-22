use contpedido;

# 11. Obter quantos clientes fizeram pedido na empresa.
select count(distinct idcliente) as "Quantidade"
from pedido;

# 12. Obter a soma do valor do frete de todos os pedidos atendidos por via marítima.
select sum(frete) as "Total"
from pedido
where via = "M";

# 13. Obter a média de salário dos vendedores (funções 10 e 11) que não sejam casados.
select avg(salario) as "Média Salarial"
from funcionario
where idfuncao in (10, 11) and estcivil != "C";

# 14. Obter a data de nascimento da funcionária mais velha.
select min(datanasc) as "Data de Nascimento"
from funcionario;

# 15. Obter qual a quantidade mais vendida de um produto para cada pedido.
select idpedido, max(quant) as "Quantidade"
from itens
group by idpedido;

# 16. Obter quantos homens e quantas mulheres funcionários nasceram em cada cidade.
select idnatural, count(idfuncionario) as 'Funcionario'
from funcionario
group by idnatural;

# 17. Obter o total de salários de cada setor da empresa que tenha este total maior que R$ 5.000,00.
select idsetor as 'Setor', sum(salario) as 'Salario Total'
from funcionario
group by idsetor 
having sum(salario) > 5000;

# 18. Obter o código do cliente e a quantidade de pedidos realizados por cada um em cada ano, apenas para os anos em que foram realizados mais de 5 pedidos.
select idcliente as 'Cliente', year(datapedid) as 'Ano', count(idpedido) as 'Pedido'
from pedido
group by idcliente, year(datapedid)
having count(idpedido) > 5
order by idcliente, year(datapedid)