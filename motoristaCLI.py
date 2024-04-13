from motoristas_classes import Corrida, Motorista, Passageiro

class MotoristaCLI:
    def __init__(self, motorista_model):
        self.commands = {}
        self.motorista_model = motorista_model

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        self.add_command("create", self.create_motorista)
        self.add_command("read", self.read_motorista)
        self.add_command("update", self.update_motorista)
        self.add_command("delete", self.delete_motorista)
        self.add_command("quit", self.quit_program)
        
        while True:
            command = input("Enter a command (create, read, update, delete, quit): ")
            if command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")

    def create_motorista(self):
        print("Creating motorista...")
        nome_motorista = input("Enter the driver's name: ")
        passageiro = self.create_passageiro()
        corridas = self.create_corridas(passageiro)
        motorista = Motorista(nome_motorista)
        for corrida in corridas:
            motorista.adicionar_corrida(corrida)
        self.motorista_model.create_motorista(motorista)
        print("Motorista created successfully!")

    def create_passageiro(self):
        nome = input("Enter the passenger's name: ")
        documento = input("Enter the passenger's document: ")
        return Passageiro(nome, documento)

    def create_corridas(self, passageiro):
        corridas = []
        while True:
            add_corrida = input("Would you like to add a race? (yes/no): ").lower()
            if add_corrida == "yes":
                nota = float(input("Enter the race's rating: "))
                distancia = float(input("Enter the race's distance: "))
                valor = float(input("Enter the race's value: "))
                corridas.append(Corrida(nota, distancia, valor, passageiro))
            elif add_corrida == "no":
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        return corridas

    def read_motorista(self):
        id = input("Enter the motorist's ID: ")
        motorista = self.motorista_model.read_motorista(id)
        if motorista:
            print("Motorista found:")
            print(motorista)
        else:
            print("Motorista not found.")

    def update_motorista(self):
        motorista_id = input("Enter the motorist's ID: ")
        motorista = self.motorista_model.read_motorista(motorista_id)
        if motorista:
            print("Updating motorista...")
            nome = input("Entre com um novo nome:")

            motorista = self.motorista_model.update_motorista(motorista_id, nome)
        else:
            print("Motorista not found.")

    def delete_motorista(self):
        motorista_id = input("Enter the motorist's ID: ")
        motorista = self.motorista_model.read_motorista(motorista_id)
        if motorista:
            self.motorista_model.delete_motorista(motorista_id)
            print("Motorista deleted successfully.")
        else:
            print("Motorista not found.")

    def quit_program(self):
        print("Goodbye!")
        exit()
