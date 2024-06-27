lista_produtos = [
    'máscaras faciais', 'batons', 'esmaltes', 'perfumes', 
    'loções', 'xampus', 'sabonetes', 'delineadores'
]

# Atualizações na lista de produtos
lista_produtos[1] = 'rímel' 
lista_produtos[4] = 'cremes hidratantes' 
lista_produtos.remove('delineadores')  


lista_produtos.append('creme dental')
lista_produtos.append('protetor solar')


print("### Nova Lista de Produtos ###")
for produto in lista_produtos:
    print(produto)