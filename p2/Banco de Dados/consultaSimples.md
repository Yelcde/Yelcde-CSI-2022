use contpedido;

# 1. Obter, para todos os produtos, código, nome com o cabeçalho "Produto", quantidade em estoque com o cabeçalho "Estoque Real" e estoque mínimo com o cabeçalho "Estoque Mínimo".
select idproduto, nome as 'Produto', quantest as 'Estoque Real', estmin as 'Estoque Minimo'
from produto;

# 2. Obter, para todos os produtos, o código, o nome, o preço de venda e uma coluna adicional informando um aumento de 25% sobre o preço de venda. Dê um nome a esta coluna.
select idproduto, nome, venda, venda * 1.25 as 'Venda com Bônus'
from produto;

# 3. Obter as cidades onde residem os funcionários. Elimine a repetição de linhas.
select distinct idreside
from funcionario;

# 4. Obter código, nome, tipo, preço de custo e preço de venda de todos os produtos ordenados pelo tipo em ordem descendente e pelo nome em ordem ascendente.
select idproduto, nome, idtipo, custo, venda
from produto
order by idtipo; 

# 5. Obter o nome e o setor dos funcionários que nasceram nas cidades com código 7, 8 e 15, ordenados pelo setor e nome do funcionário.
select nome, idnatural
from funcionario
where (idnatural = 7) or
	  (idnatural = 8) or
      (idnatural = 15)
order by idsetor, nome; 

# 6. Obter os produtos cujo tipo seja 1, 2 ou 3 e o preço de venda esteja entre R$ 10,00 e R$ 50,00.
select nome, idtipo, venda
from produto
where (idtipo = 1 or idtipo = 2 or idtipo = 3) and (venda >= 10 and venda <= 50);

# 7. Obter todos os dados dos funcionários que não têm e-mail, mas possuam celular.
select nome
from funcionario
where (email is null and celular is not null);

# 8. Obter o nome e o salário dos funcionários homens, casados e com salário menor ou igual a R$ 3.000,00, ordenados pelo salário em ordem descendente.
select nome, salario
from funcionario
where (sexo = 'M' and estcivil = "C" and salario <= 3000)
order by salario desc; 

# 9. Obter o nome e o preço de venda dos produtos cuja descrição contenha a palavra "chocolate" com preço de venda maior ou igual a R$ 15,00, ordenados pelo preço de venda em ordem descendente.
select nome, venda
from produto
where descricao like '%chocolate%' and venda >= 15
order by venda desc;

# 10. Obter o código e o nome dos funcionários homens, exceto aqueles cujos nomes iniciam pela letra "A", ordenados pelo nome em ordem ascendente.
select idfuncionario, nome
from funcionario
where sexo = "M" and nome not like "a%"
order by nome