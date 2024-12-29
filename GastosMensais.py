# Listas para armazenar os dados
gasto = []
valor_gasto = []
valor_entrada = []
entrada = []

# Função para adicionar elementos
def adicionar():
    elemento = input("Digite o item que deseja acrescentar à listagem: ")
    try:
        categoria = int(input("Digite a categoria: \n 1- Gastos  2- Entradas: "))
        if categoria == 1:
            valor = float(input("Digite o valor do gasto: "))
            gasto.append(elemento)
            valor_gasto.append(valor)
        elif categoria == 2:
            valor = float(input("Digite o valor da entrada: "))
            entrada.append(elemento)
            valor_entrada.append(valor)
        else:
            print("Você não digitou uma categoria válida.")
    except ValueError:
        print("Você não digitou um número válido.")

# Função para listar os dados e calcular saldo
def listar():
    total_gastos = sum(valor_gasto)
    total_entradas = sum(valor_entrada)
    saldo = total_entradas - total_gastos 
    print(f"\nOs itens dos gastos são: {gasto}, e o valor total é: {total_gastos:.2f}")
    print(f"Os itens das entradas são: {entrada}, e o valor total é: {total_entradas:.2f}")
    print(f"Saldo (Entradas - Gastos): {saldo:.2f}\n")  

# Menu principal
print("Cálculo de Gastos Mensais")
while True:
    try:
        opcao = int(input("Digite o número correspondente à opção que deseja: \n 1- Listar  2- Adicionar  3- Sair: "))
        if opcao == 1:
            listar()
        elif opcao == 2:
            adicionar()
        elif opcao == 3:
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Você não digitou um número válido.")






