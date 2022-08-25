hodometro = float(input('Qual o valor atual do seu hodômetro? ')) # 700
kmviagem = float(input('Qual a quilometragem da viagem? ')) # 150
litrosgastos = float(input('Quantos litros foram gastos? ')) # 80
precolitro = float(input('Qual o preço do litro? ')) # 5
capacidadetanque= float(input('Qual a capacidade do tanque do seu veículo? ')) # 70

# CONTAS

kmrodados = hodometro + kmviagem
kmporlitro = kmrodados / litrosgastos
autonomia = kmrodados / capacidadetanque
litrosgastosnaviagem = kmviagem/kmporlitro
precodaviagem = litrosgastosnaviagem*precolitro

# SAÍDAS

print(f'Você andou {kmrodados} km')
print(f'Seu veículo faz {kmporlitro} km por litro')
print(f'Seu veículo tem que andar {autonomia} km para precisar reabastecer')
print(f'O custo da sua viagem vai ser {precodaviagem} R$')

# kmrodados = 850
# kmporlitro = 10
# autonomia = 70
# precodaviagem = 