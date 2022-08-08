class Pessoa:

    # Metodo Contrutor

    def __init__(self):
        self.nome = ""
        self.telefone = ""
        self.endereco = ""

    #Metodos de Acesso

    def getNome(self):
        return self .nome

    def getTelefone(self):
        return self .telefone

    def getEndereco(self):
        return self .endereco

    def setNome(self, nome):
        self .nome = nome

    def setTelefone(self, telefone):
        self .telefone = telefone

    def setEndereco(self, endereco):
        self .endereco = endereco


    #Metodo Cadastrar

    def cadastrar(self, nome, telefone, endereco):
        self.setNome(nome)
        self.setTelefone(telefone)
        self.setEndereco(endereco)


    #Metodo ConsultarTudo

    def consultarTudo(self):
        return "nome: {}\ntelefone: {}\nendereco: {}\n".format(self.getNome(), self.getTelefone(), self.getEndereco())

