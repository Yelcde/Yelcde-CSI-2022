class Pessoa:
    
    def __init__(self, nome, idade):
        # Inicializando atributos sem proteção
        # self.nome = nome
        # self.idade = idade
        
        # Inicializando atributos com proteção
        self._nome = nome
        self._idade = idade
        
    # Protegendo os atributos
    
    # O get retorna o valor do atributo
    def get_idade(self):
        return self._idade
    
    # O set muda o valor do atributo
    def set_idade(self, nova_idade):
        # Protegendo idade de receber valores invalidos
        if nova_idade >= 0:
            self._idade = nova_idade
        # Agora a idade só vai ser alterada se o valor for válido

aluno = Pessoa('Carlos', 19)
print('Nome do Aluno:', aluno._nome)
#aluno.idade = -3  Isso não pode acontecer

# Acessando atributo idade por metodos
aluno.set_idade(-3)
print('Idade do Aluno:', aluno.get_idade())