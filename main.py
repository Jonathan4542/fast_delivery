from modelos.cliente import Cliente
from modelos.pedido import Pedido
from services.cliente_service import ClienteService
from services.pedido_service import PedidoService
from util.menu import Menu

def main():
    cliente_service = ClienteService()
    pedido_service = PedidoService()

    while True:
        opcao = Menu.exibir_menu_principal()

        if opcao == '1':
            nome = input("Nome: ")
            cpf = input("CPF: ")
            telefone = input("Telefone: ")
            endereco = input("Endereço: ")
            cliente = Cliente(nome, cpf, telefone, endereco)
            cliente_service.cadastrar_cliente(cliente)
            print("Cliente cadastrado com sucesso!")

        elif opcao == '2':
            clientes = cliente_service.listar_clientes()
            for c in clientes:
                print(f"Nome: {c.nome} | CPF: {c.cpf} | Endereço: {c.endereco}")

        elif opcao == '3':
            cpf_cliente = input("CPF do Cliente: ")
            cliente = cliente_service.buscar_cliente(cpf_cliente)
            if cliente:
                codigo = input("Código do Pedido: ")
                peso = float(input("Peso (kg): "))
                distancia = float(input("Distância (km): "))
                print("1-Comum | 2-Expressa | 3-Premium")
                tipo = int(input("Tipo de entrega: "))
                
                pedido = Pedido(codigo, cliente, peso, distancia, tipo)
                pedido_service.criar_pedido(pedido)
                print(f"Pedido criado! Frete calculado: R$ {pedido.valor_frete:.2f}")
            else:
                print("Cliente não encontrado.")

        elif opcao == '4':
            pedidos = pedido_service.listar_pedidos()
            for p in pedidos:
                print(f"Código: {p.codigo} | Cliente: {p.cliente.nome} | Frete: R$ {p.valor_frete:.2f} | Status: {p.status}")

        elif opcao == '5':
            codigo = input("Código do Pedido: ")
            print("Status: Em preparação | Saiu para entrega | Entregue | Cancelado")
            novo_status = input("Novo status: ")
            if pedido_service.atualizar_status(codigo, novo_status):
                print("Status atualizado!")
            else:
                print("Pedido não encontrado.")

        elif opcao == '0':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()