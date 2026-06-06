from modelos.pedido import Pedido

class PedidoService:
    def __init__(self):
        self.__pedidos = []

    def criar_pedido(self, pedido: Pedido):
        self.__pedidos.append(pedido)

    def listar_pedidos(self):
        return self.__pedidos

    def atualizar_status(self, codigo: str, novo_status: str):
        for pedido in self.__pedidos:
            if pedido.codigo == codigo:
                pedido.status = novo_status
                return True
        return False