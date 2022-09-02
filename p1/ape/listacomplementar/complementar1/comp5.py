entrada = int(input('Me dê um horário em segundos: '))
horas = entrada // 3600
minutos = (entrada % 3600) // 60
segundos = entrada % 60

print(f'Seu horário {entrada}, que está em segundo é {horas}:{minutos}:{segundos}')