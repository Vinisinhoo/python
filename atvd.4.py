import os

numero = []
nomes = []


def cadastro(num, nome):
    numero.append(num)
    nomes.append(nome)
    return "A chapa foi cadastrada com sucesso"

def pesquisar():
    limpar()
    cont = 0
    while cont< len(nomes):
        print(numero[cont])
        print(nome[cont])
        cont+=1
def atualizar ():
    novonumero = int(input("Digite o novo número"))
    novonome = "Israel"
    if num in numero:
        posicao = numero.index(num)
        numero[posicao] = novonumero
        nomes[posicao] = novonome
        return "Chapa atualizada com sucesso"

    return "0"
def deletar(num):
    if num in numero:
        posicao= numero.index(num)
        numero.pop(posicao)
        nomes.pop(posicao)
        return "A chapa de número", num,"","foi removida com sucesso"
    else:
        return("Não existe chapa com esse número", num)
        
    return "0"
def msn():
    print("opção inválida")
    
def limpar():
    os.system('cls')      

op = 10
while op != 0:
    op = int(input("digte sua opção" +
             "\n1 cadastrar uma chapa"+
             "\n2 pesquisar uma chapa"+
             "\n3 atualize uma chapa"+
             "\n4 delete uma chapa"+
             "\n0 feche o sistema"))
    if op == 1:
        limpar()
        num = int(input("Digite o numero da chapa"))
        nome = input("Digite o nome da chapa")
        print(cadastro(num , nome)) 
    elif op==2:
        pesquisar()
    elif op==3:
        valor=int(input("digite o número da chapa para atualizar"))
        retorno = atualizar(valor)
        print (retorno)
    
    elif op==4:
        op= int(input("digite o número da chapa para deletar"))
        retorno = deletar(valor)
        print(retorno)