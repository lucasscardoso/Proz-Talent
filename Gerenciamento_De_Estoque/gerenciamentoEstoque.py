#Projeto MVP Lucas Da Silva Cardoso

# Função para apresentar o menu e obter a escolha do usuário
def menu():
    print("\n===== Cadastro de Produtos =====")
    print("1 - Cadastrar produto")
    print("2 - Consultar produto")
    print("3 - Remover todos os produtos")
    print("4 - Remover produto por código e quantidade")
    print("5 - Sair")
    return int(input("Escolha uma opção: "))

# Classe Produto para representar cada item
class Produto:
    def __init__(self, codigo, nome, preco, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

# Função para cadastrar um novo produto
def cadastrar_produto(produtos):
    print("\nCadastro de Produto")
    codigo = input("Digite o código do produto: ")

    # Verifica se o código já existe na lista de produtos
    for produto in produtos:
        if produto.codigo == codigo:
            print("Produto já cadastrado.")
            return

    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))

    novo_produto = Produto(codigo, nome, preco, quantidade)
    produtos.append(novo_produto)
    print("Produto cadastrado com sucesso.")

# Função para consultar um produto pelo código
def consultar_produto(produtos):
    codigo = input("Digite o código do produto a ser consultado: ")
    for produto in produtos:
        if produto.codigo == codigo:
            print("\nInformações do Produto")
            print(f"Código: {produto.codigo}")
            print(f"Nome: {produto.nome}")
            print(f"Preço: R${produto.preco:.2f}")
            print(f"Quantidade: {produto.quantidade}")
            return
    print("Produto não encontrado.")

# Função para remover todos os produtos
def remover_todos(produtos):
    confirmacao = input("Tem certeza que deseja remover todos os produtos? (s/n): ")
    if confirmacao.lower() == 's':
        produtos.clear()
        print("Todos os produtos foram removidos.")
    else:
        print("Operação cancelada.")

# Função para remover um produto pelo código e quantidade
def remover_produto(produtos):
    codigo = input("Digite o código do produto a ser removido: ")
    for produto in produtos:
        if produto.codigo == codigo:
            print(f"\nInformações do Produto: {produto.nome}")
            print(f"Quantidade disponível: {produto.quantidade}")

            quantidade_remover = int(input("Digite a quantidade a ser removida: "))

            if quantidade_remover > produto.quantidade or quantidade_remover < 1:
                print("Quantidade inválida. Operação cancelada.")
                return

            produto.quantidade -= quantidade_remover
            print(f"{quantidade_remover} unidades do produto removidas com sucesso.")

            if produto.quantidade == 0:
                produtos.remove(produto)
                print("Produto esgotado. Removido da lista.")
            return

    print("Produto não encontrado.")

# Função principal do programa
def main():
    produtos = []

    print("Bem-vindo ao sistema de cadastro de produtos!")

    while True:
        escolha = menu()

        if escolha == 1:
            cadastrar_produto(produtos)
        elif escolha == 2:
            consultar_produto(produtos)
        elif escolha == 3:
            remover_todos(produtos)
        elif escolha == 4:
            remover_produto(produtos)
        elif escolha == 5:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

# Iniciar o programa chamando a função principal
main()

