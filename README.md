# FastDelivery Express

## 1. Descrição do Projeto
O FastDelivery Express é um sistema para gerenciamento de entregas urbanas via console. Ele permite o controle de clientes, entregadores, pedidos, além do cálculo dinâmico de fretes baseados em diferentes modalidades de entrega e atualização de status em tempo real.

## 2. Tecnologias Utilizadas
* Python 3
* Git
* GitHub

## 3. Estrutura de Pastas
* `/modelos`: Contém as classes de modelo que representam as entidades do sistema (Pessoa, Cliente, Entregador, Pedido, Entrega).
* `/interfaces`: Contém os contratos do sistema, como a interface de cálculo de frete.
* `/services`: Gerencia a regra de negócio do sistema (cadastro, listagem, atualização de status).
* `/util`: Contém funções auxiliares do sistema, como exibição de menus e validações.
* `main.py`: Arquivo principal que executa e une os componentes do sistema.

## 4. Explicação dos Conceitos de POO Utilizados
* **Herança:** Utilizada nas classes `Cliente` e `Entregador`, que herdam características e comportamentos da superclasse base `Pessoa`.
* **Interface:** A classe `CalculoFreteInterface` atua como um contrato, obrigando que todas as modalidades de entrega implementem o método `calcular_frete`.
* **Polimorfismo:** O método `calcular_frete` atua de maneiras diferentes dependendo de qual objeto de entrega é instanciado (Comum, Expressa ou Premium), aplicando taxas distintas sobre a distância.
* **Encapsulamento:** Utilizado em todas as classes de modelo através de atributos privados (como `__nome` e `__cpf`) e acessados/modificados seguramente utilizando propriedades (`@property`, setters).

## 5. Como Executar o Projeto
No terminal do seu sistema operacional, dentro da raiz do projeto, execute o seguinte comando:
```bash
python main.py