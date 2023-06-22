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