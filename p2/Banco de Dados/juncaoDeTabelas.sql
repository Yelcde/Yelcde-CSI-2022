use contpedido;

# 19. Obter todos os funcionários, mostrando código, nome, código da função, nome da função e gratificação da função.
select fu.idfuncionario as 'Id do Funcionário', 
	   fu.nome as 'Nome do Funcionário',
       fu.idfuncao as "Id da Função",
       fun.nome as 'Nome da Função',
       fun.gratific as "Gratificação da Função"
from funcionario fu
join funcao fun
on fu.idfuncao = fun.idfuncao
order by fu.nome; 

# 20. Obter o código e o nome dos clientes que moram na cidade de nome "London".
select c.idCliente as 'Id do Cliente',
	   c.nome as 'Nome do Cliente',
       cid.nome as 'Nome da Cidade'
from cliente c 
join cidade cid 
on c.idcidade = cid.idcidade
where cid.nome = 'London'
order by c.nome;

# 21. Obter a média salarial dos funcionários cujo nome da função inicie por “Diretor”.
select avg(fu.salario) as 'Média Salarial',
	   fun.nome as 'Função'
from funcionario fu
join funcao fun
on fu.idfuncao = fun.idfuncao
where fun.nome like 'Diretor%';