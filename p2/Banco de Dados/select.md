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
order by idtipo 