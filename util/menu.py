class Menu:
    @staticmethod
    def exibir_menu_principal():
        print("\n--- FastDelivery Express ---")
        print("1. Cadastrar Cliente")
        print("2. Listar Clientes")
        print("3. Criar Pedido")
        print("4. Listar Pedidos")
        print("5. Atualizar Status do Pedido")
        print("0. Sair")
        return input("Escolha uma opção: ")