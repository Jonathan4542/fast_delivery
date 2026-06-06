from modelos.cliente import Cliente

class ClienteService:
    def __init__(self):
        self.__clientes = []

    def cadastrar_cliente(self, cliente: Cliente):
        self.__clientes.append(cliente)

    def listar_clientes(self):
        return self.__clientes
        
    def buscar_cliente(self, cpf: str):
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                return cliente
        return None