class Doente:

    def __init__(self):
        self.idade = 0
        self.sexo = ""  # M ou F
        self.tensao = 0
        self.colestrol = 0
        self.batimento = 0
        self.temDoenca = 0 # 0 se não 1 se sim

    ####################################################################################################################

    def cria_doente(self, idade, sexo, tensao, colestrol, batimento, temDoenca):
        self.idade = idade
        self.sexo = sexo
        self.tensao = tensao
        self.colestrol = colestrol
        self.batimento = batimento
        self.temDoenca = temDoenca

    ####################################################################################################################

    def __str__(self):
        # representa o doente numa string
        out = "Idade = " +self.idade+ "; Sexo = " +self.sexo+ "; Tensão = " +self.tensao+ "; Colestrol = " +self.colestrol+ "; Batimento = " +self.batimento+ "; Tem Doença (1-sim, 0-não) = " +self.temDoenca
        return out

    ####################################################################################################################

    def imprime(self):
        # imprime o doente como uma string
        print(f"Idade = {self.idade} ; Sexo =  {self.sexo} ;  Tensão =  {self.tensao} ; Colestrol =  {self.colestrol} ; Batimento = {self.batimento} ; Tem Doença (1-sim, 0-não) =  {self.temDoenca}")

    ####################################################################################################################

    def nivel_colestrol(self):
        # avalia o nivel de colestrol de um doente

        colestrol = int(self.colestrol)

        nivel = int(colestrol / 10)

        return nivel


    ####################################################################################################################
