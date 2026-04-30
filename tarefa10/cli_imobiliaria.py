import json
import os

def carregar_dados():
    caminho_arquivo = 'tarefa10/imobiliaria.json' 
    
    if not os.path.exists(caminho_arquivo):
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return None
    
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        return json.load(f)

def exibir_menu(imoveis):
    print("\n" + "="*40)
    print("      SISTEMA DE CONSULTA IMOBILIÁRIA")
    print("="*40)
    for i, imovel in enumerate(imoveis, start=1):
        print(f"{i} - {imovel['descricao']}")
    print("="*40)

def detalhar_imovel(imovel):
    print("\n" + "-"*50)
    print(f"DETALHES DO IMÓVEL")
    print("-"*50)
    print(f"Descrição: {imovel['descricao']}")
    print(f"Valor:     {imovel['valor']}")
    
    print("\nPROPRIETÁRIO:")
    print(f"  Nome:     {imovel['proprietario']['nome']}")
    print(f"  E-mails:  {', '.join(imovel['proprietario']['emails']) if imovel['proprietario']['emails'] else 'Nenhum'}")
    print(f"  Telefones: {', '.join(imovel['proprietario']['telefones']) if imovel['proprietario']['telefones'] else 'Nenhum'}")
    
    print("\nENDEREÇO:")
    end = imovel['endereco']
    numero = end['numero'] if end['numero'] else "S/N"
    print(f"  Rua:      {end['rua']}, Nº {numero}")
    print(f"  Bairro:   {end['bairro']}")
    print(f"  Cidade:   {end['cidade']}")
    
    print("\nCARACTERÍSTICAS:")
    carac = imovel['caracteristicas']
    print(f"  Área:        {carac['tamanho']}m²")
    print(f"  Quartos:     {carac['numQuartos']}")
    print(f"  Banheiros:   {carac['numBanheiros']}")
    print("-"*50)

def main():
    dados = carregar_dados()
    if not dados:
        return

    imoveis = dados['imobiliaria']

    while True:
        exibir_menu(imoveis)
        opcao = input("Digite o ID do imóvel para saber mais (ou 'sair'): ").strip().lower()

        if opcao == 'sair':
            print("Encerrando sistema... Até logo!")
            break
        
        try:
            indice = int(opcao) - 1
            if 0 <= indice < len(imoveis):
                detalhar_imovel(imoveis[indice])
                input("\nPressione ENTER para voltar ao menu...")
            else:
                print("\n[!] Erro: ID fora do intervalo. Tente novamente.")
        except ValueError:
            print("\n[!] Erro: Digite um número válido ou 'sair'.")

if __name__ == "__main__":
    main()