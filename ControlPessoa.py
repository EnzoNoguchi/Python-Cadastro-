from Pessoa import Pessoa

class ControlPessoa:

    #Metodo Construtor

    def __init__(self):
        self.person = Pessoa()#Instanciando a classe pesso
        self.opcao = -1



     #Metodo Menu

    def menu(self):
        print("Escolha uma das opções abaixo:\n\n" +
              "1. Cadastrar\n" +
              "2. Consultar\n" +
              "0. Sair\n")
        self.opcao = int(input())#Converte a opção texto para numero



    #Metodo Operacao

    def operacao(self):
        while(self.opcao != 0):
            self.menu()#Chamando Menu
            if self.opcao == 0:
                print("Obrigado!")
            elif self.opcao == 1:
                print("Informe seu nome: ")
                nome = input()
                print("\nInforme seu telefone: ")
                telefone = input()
                print("\nInforme seu endereço: ")
                endereco = input()
                self.person.cadastrar(nome, telefone, endereco)

            elif self.opcao == 2:
                print(self.person.consultarTudo())
            else:
                print("Opção Inválida")

