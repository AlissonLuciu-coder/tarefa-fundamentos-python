lista_de_produtos = []
lista_de_precos = []

while True:

    nome_produto = input('Digite o nome do produto: ')
    preco_produto = float(input('Digite o preço do produto: '))

    lista_de_produtos.append(nome_produto)
    lista_de_precos.append(preco_produto)
    
    continuar = input('Deseja adicionar outro produto? (se não digite: sair): ').lower()
    if continuar == 'sair':
        break

print(lista_de_produtos)
print(lista_de_precos)
    
