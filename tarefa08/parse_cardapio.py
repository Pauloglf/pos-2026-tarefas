from xml.dom.minidom import parse

dom = parse('tarefa08/cardapio.xml')

cardapio = dom.documentElement

pratos = cardapio.getElementsByTagName('prato')

for prato in pratos:
    id = prato.getAttribute('id')
    elemento_nome = prato.getElementsByTagName('nome')[0].firstChild.data
    elemento_preco = prato.getElementsByTagName('preco')[0].firstChild.data
    elemento_descricao = prato.getElementsByTagName('descricao')[0].firstChild.data

print('''
Menu:
    1 - Batata Frita
    2 - Hambúrguer
    3 - Lasanha
    4 - Salada
    5 - Risoto''')

escolha = input('Digite o ID do prato que deseja mais informações: ')

prato_encontrado = None
for p in pratos:
    if p.getAttribute('id') == escolha:
        prato_encontrado = p
        break

if prato_encontrado:
    nome = prato_encontrado.getElementsByTagName('nome')[0].firstChild.nodeValue
    descricao = prato_encontrado.getElementsByTagName('descricao')[0].firstChild.nodeValue
    preco = prato_encontrado.getElementsByTagName('preco')[0].firstChild.nodeValue
    calorias = prato_encontrado.getElementsByTagName('calorias')[0].firstChild.nodeValue
    tempo = prato_encontrado.getElementsByTagName('tempoPreparo')[0].firstChild.nodeValue
    
    nos_ingredientes = prato_encontrado.getElementsByTagName('ingrediente')
    
    print(f"\nNome: {nome}")
    print(f"Descrição: {descricao}")
    print("Ingredientes:")
    for ing in nos_ingredientes:
        print(f"    {ing.firstChild.nodeValue}")
    
    print(f"Preço: {preco}")
    print(f"Calorias: {calorias}kcal")
    print(f"Tempo de preparo: {tempo}.")
else:
    print("Prato não encontrado.")