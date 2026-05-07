import collections
import subprocess
import subprocess
lista_de_produtos = []
lista_de_precos = []
muito_caros = 0

while True:

    nome_produto = input('Digite o nome do produto: ')
    preco_produto = float(input('Digite o preço do produto: '))

    lista_de_produtos.append(nome_produto)
    lista_de_precos.append(preco_produto)
    
    continuar = input('Deseja adicionar outro produto? (se não digite: sair): ').lower()
    if continuar == 'sair':
        break


media_dos_precos = sum(lista_de_precos) / len(lista_de_precos)

caro = max(lista_de_precos)
posicao_caro = lista_de_precos.index(caro)
nome_caro = lista_de_produtos[posicao_caro]

for preco in lista_de_precos:
    if preco >= 100:
        muito_caros += 1





print(f'A média dos preços é: {media_dos_precos:.2f}')

for i in range(len(lista_de_produtos)):
    print(f'Produto: {lista_de_produtos[i]}, Preço: R$ {lista_de_precos[i]:.2f}')

print(lista_de_produtos)
print(lista_de_precos)
print(f'O produto {nome_caro} custa R${caro:.2f}') 
print(f'Foram encontrados {muito_caros} produtos muito caros')
