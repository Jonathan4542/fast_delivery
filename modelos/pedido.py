from .cliente import Cliente
from .entrega import EntregaComum, EntregaExpressa, EntregaPremium

class Pedido:
    def __init__(self, codigo: str, cliente: Cliente, peso: float, distancia: float, tipo_entrega: int):
        self.__codigo = codigo
        self.__cliente = cliente
        self.__peso = peso
        self.__distancia = distancia
        self.__status = "Em preparação"
        
        if tipo_entrega == 1:
            self.__estrategia_entrega = EntregaComum()
        elif tipo_entrega == 2:
            self.__estrategia_entrega = EntregaExpressa()
        else:
            self.__estrategia_entrega = EntregaPremium()
            
        self.__valor_frete = self.__estrategia_entrega.calcular_frete(self.__distancia)

    @property
    def codigo(self): return self.__codigo
    
    @property
    def cliente(self): return self.__cliente
    
    @property
    def status(self): return self.__status
    
    @status.setter
    def status(self, novo_status): self.__status = novo_status
    
    @property
    def valor_frete(self): return self.__valor_frete