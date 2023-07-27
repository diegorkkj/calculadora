
import os

x = "n"
while x != "y":

    #Variavel para verificação se quer ou não sair do algoritimo

    op = [1, 2 , 3, 4, 5]

    #Variaveis das operações

    op1 = int(input("Bem vindo a calculadora.py \n 1-Adição \n 2-Subtração \n 3-Divisão \n 4-Multiplicação \n 5-Sair \n Digite o numero equivalente a opção que deseja: "))

    #Input para a seleção de operação

    os.system("cls")

    if op1 == op [0]:
        ad1 = int(input("Você selecionou adição. Digite o primeiro numero da soma: "))
        ad2 = int(input("Digite o segundo numero da operação: "))
        print(ad1 + ad2)

    #Input para operação de adição

        os.system("pause")

    elif op1 == op [1]:
        sub1 = int(input("Você selecionou subtração. Digite o primeiro numero da operação: "))
        sub2 = int(input("Digite o segundo numero da operação: "))
        print(sub1 - sub2)

    #Input para Operação de subtração

        os.system("pause")

    elif op1 == op [2]:
        div1 = int(input("Você selecionou divisão. Digite o primeiro numero da operação: "))
        div2 = int(input("Digite o segundo numero da operação: "))

        os.system("pause")
        
    #Input para Operação de divisão
        
        if div1 == 0 or div2 == 0:
            print("ERROKKJ")
        #Código erro para o caso de divisão por 0
 
            os.system("pause")

        else:
            print(div1 / div2)

            os.system("pause")

    elif op1 == op [3]:
        mul1 = float(input("Você selecionou multiplicação. Digite o primeiro numero da operação: "))
        mul2 = float(input("Digite o segundo numero da operação: "))
        print(mul1 * mul2)

        os.system("pause")

    elif op1 == op[4]:
        x = "y"
    
    else:
        print("Essa opção não existe.")

        os.system("pause")

    #Código caso a seleção de numero não conste na lista

os.system("pause")