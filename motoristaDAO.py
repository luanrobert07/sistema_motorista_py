from bson import ObjectId
from motoristas_classes import Corrida, Motorista, Passageiro


class MotoristaDAO:
    def __init__(self, database):
        self.database = database
    
    def create_motorista(self, motorista):
        try:
            dados_motorista = {
                "nome": motorista.nome,
                "corridas": []
            }

            for corrida in motorista.corridas:
                dados_corrida = {
                    "nota": corrida.nota,
                    "distancia": corrida.distancia,
                    "valor": corrida.valor,
                    "passageiro": {
                        "nome": corrida.passageiro.nome,
                        "documento": corrida.passageiro.documento
                    }
                }
                dados_motorista["corridas"].append(dados_corrida)

            self.database.collection.insert_one(dados_motorista)
            print("Motorista criado com sucesso!")
        except Exception as e:
            print(f"Erro ao criar motorista: {e}")

    def read_motorista(self, id: str):
        try:
            print(f"Procurando por motorista com ID: {id}")
            motorista_data = self.database.collection.find_one({"_id": ObjectId(id)})
            if motorista_data:
                nome = motorista_data["nome"]
                corridas = motorista_data["corridas"]
                motorista = Motorista(nome)
                for corrida_data in corridas:
                    nota = corrida_data["nota"]
                    distancia = corrida_data["distancia"]
                    valor = corrida_data["valor"]
                    passageiro_data = corrida_data["passageiro"]
                    passageiro = Passageiro(passageiro_data["nome"], passageiro_data["documento"])
                    corrida = Corrida(nota, distancia, valor, passageiro)
                    motorista.adicionar_corrida(corrida)
                return motorista_data
            else:
                print("Motorista não encontrado.")
                return None
        except Exception as e:
            print(f"Erro ao ler motorista: {e}")
            return None

    
    def update_motorista(self, id: str, nome: str):
        try:
            novo_motorista = self.database.collection.update_one({"_id": ObjectId(id)}, {"$set": {"nome": nome}})
            print("Motorista atualizado com sucesso!")
            return novo_motorista
        except Exception as e:
            print(f"Erro ao atualizar motorista: {e}")
            return None
    
    def delete_motorista(self, id: str):
        try:
            self.database.collection.delete_one({"_id": ObjectId(id)})
            print("Motorista deletado com sucesso!")
        except Exception as e:
            print(f"Erro ao deletar motorista: {e}")
