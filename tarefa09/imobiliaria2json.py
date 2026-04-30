import json
from xml.dom.minidom import parse

def get_data(element, tag):
    """Auxiliar para pegar o texto de uma tag simples"""
    nodes = element.getElementsByTagName(tag)
    if nodes and nodes[0].firstChild:
        return nodes[0].firstChild.nodeValue
    return None

def xml_to_dict():
    try:
        dom = parse('tarefa09/imobiliaria.xml')
        root = dom.documentElement
        imoveis_xml = root.getElementsByTagName('imovel')
        
        lista_imoveis = []

        for imovel in imoveis_xml:
            prop_node = imovel.getElementsByTagName('proprietario')[0]
            prop_nome = get_data(prop_node, 'nome')
            emails = [e.firstChild.nodeValue for e in prop_node.getElementsByTagName('email')]
            telefones = [t.firstChild.nodeValue for t in prop_node.getElementsByTagName('telefone')]

            end_node = imovel.getElementsByTagName('endereco')[0]
            num = get_data(end_node, 'número')

            carac_node = imovel.getElementsByTagName('caracteristicas')[0]
            
            dados_imovel = {
                "descricao": get_data(imovel, 'descricao'),
                "proprietario": {
                    "nome": prop_nome,
                    "emails": emails,
                    "telefones": telefones
                },
                "endereco": {
                    "rua": get_data(end_node, 'rua'),
                    "bairro": get_data(end_node, 'bairro'),
                    "cidade": get_data(end_node, 'cidade'),
                    "numero": int(num) if num else None
                },
                "caracteristicas": {
                    "tamanho": get_data(carac_node, 'tamanho'),
                    "numQuartos": int(get_data(carac_node, 'numQuartos')),
                    "numBanheiros": int(get_data(carac_node, 'numBanheiros'))
                },
                "valor": get_data(imovel, 'valor')
            }
            lista_imoveis.append(dados_imovel)

        estrutura_final = {"imobiliaria": lista_imoveis}

        with open('tarefa09/imobiliaria.json', 'w', encoding='utf-8') as f:
            json.dump(estrutura_final, f, indent=4, ensure_ascii=False)
            
        print("Sucesso! O arquivo 'imobiliaria.json' foi criado.")

    except FileNotFoundError:
        print("Erro: O arquivo 'imobiliaria.xml' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro na conversão: {e}")

if __name__ == "__main__":
    xml_to_dict()