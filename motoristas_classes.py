class Passageiro:
    def __init__(self, nome, documento):
        self.nome = nome
        self.documento = documento

class Corrida:
    def __init__(self, nota, distancia, valor, passageiro):
        self.nota = nota
        self.distancia = distancia
        self.valor = valor
        self.passageiro = passageiro

class Motorista:
    def __init__(self, nome):
        self.nome = nome
        self.corridas = []
    
    def adicionar_corrida(self, corrida):
        self.corridas.append(corrida)