# Listas para armazenar os dados

lista_de_gastos = list()
lista_de_receitas = list()

def listar_gastos():
    if (len(lista_de_gastos) == 0):
        print("Nenhum gasto cadastrado.")
        return

    valor_total_gastos = 0.00

    print()
    print("*** RELATÓRIO DE GASTOS ***")
    for i, item_de_gasto in enumerate(lista_de_gastos):
        print(f"({i}) {item_de_gasto['discriminacao']}: R$ {item_de_gasto['valor']}")
        valor_total_gastos += item_de_gasto['valor']
    
    print("-" * 30)
    print(f"VALOR TOTAL DE GASTOS: R$ {valor_total_gastos}")


def adicionar_item_de_gasto():
    try:
        discriminacao_gasto = input("Discrimine o Gasto: ")
        valor_gasto = float(input("Valor do Gasto: "))

        item_de_gasto = {
            "discriminacao": discriminacao_gasto,
            "valor": valor_gasto
        }

        lista_de_gastos.append(item_de_gasto)

    except ValueError:
        print("Você não digitou um número válido.")


def remover_item_de_gasto():
    id_item_de_gasto = int(input("Informe o nr. do item de gasto a ser removido: "))
    del lista_de_gastos[id_item_de_gasto]
    print(f"Item {id_item_de_gasto} removido com sucesso.")


def listar_receitas():
    if (len(lista_de_receitas) == 0):
        print("Nenhuma receita cadastrada.")
        return
    
    valor_total_receitas = 0.00

    print()
    print("*** RELATÓRIO DE RECEITAS ***")
    for i, item_de_receita in enumerate(lista_de_receitas):
        print(f"({i}) {item_de_receita['discriminacao']}: R$ {item_de_receita['valor']}")
        valor_total_receitas += item_de_receita['valor']
    
    print("-" * 30)
    print(f"VALOR TOTAL DAS RECEITAS: R$ {valor_total_receitas}")


def adicionar_item_de_receita():
    try:
        discriminacao_receita = input("Discrimine a Receita: ")
        valor_receita = float(input("Valor da Receita: "))

        item_de_receita = {
            "discriminacao": discriminacao_receita,
            "valor": valor_receita
        }

        lista_de_receitas.append(item_de_receita)

    except ValueError:
        print("Você não digitou um número válido.")


def remover_item_de_receita():
    pass


def mostrar_msg_inicial():
    print("*****************************************")
    print("********** CONTROLE FINANCEIRO **********")
    print("*****************************************")


def mostrar_opcoes():
    print()
    print("Opções: ")

    # Gastos
    print("1 - Listar Gastos;")
    print("2 - Adicionar Item de Gasto;")
    print("3 - Remover Item de Gasto;")

    # Receitas
    print("4 - Listar Receitas;")
    print("5 - Adicionar Item de Receita;")
    print("6 - Remover Item de Receita;")

    print("7 - Sair.")

    try:
        opcao = int(input(": "))

        match opcao:
            case 1:
                listar_gastos()
            case 2:
                adicionar_item_de_gasto()
            case 3:
                remover_item_de_gasto()
            case 4:
                listar_receitas()
            case 5:
                adicionar_item_de_receita()
            case 6:
                remover_item_de_receita()
            case 7:
                exit()
            case _:
                print("Opção inválida. Tente novamente.")

    except ValueError:
        print("Você não digitou um número válido.")


mostrar_msg_inicial()

while True:
    mostrar_opcoes()







