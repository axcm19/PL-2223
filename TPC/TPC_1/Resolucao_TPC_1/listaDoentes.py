import math

from doente import Doente

class Lista_Doentes:

    def __init__(self):
        self.lista_doentes = []

    ####################################################################################################################

    def parse(self, filename):

        try:
            f = open(filename)
            lines = f.readlines()

            idade = 0
            sexo = ""
            tensao = 0
            colestrol = 0
            batimento = 0
            temDoenca = 0  # 0 se não 1 se sim

            for line in lines:
                list = line.split(",")

                idade = list[0]
                sexo = list[1]
                tensao = list[2]
                colestrol = list[3]
                batimento = list[4]
                temDoenca = list[5]

                # cria um novo doente com base na informação retirada
                doente = Doente()
                doente.cria_doente(idade, sexo, tensao, colestrol, batimento, temDoenca)

                # adiciona o doente à lista
                self.lista_doentes.append(doente)

        finally:

            #elimina a primeira linha do ficheiro que não é válida
            self.lista_doentes.pop(0)

            f.close()


    ####################################################################################################################


    def calcula_dist_sexo(self):
        mascu_com_doenca = 0
        mascu_sem_doenca = 0

        fem_com_doenca = 0
        fem_sem_doenca = 0

        for doente in self.lista_doentes:
            if doente.sexo == "M" and int(doente.temDoenca) == 1:
                    mascu_com_doenca += 1

            if doente.sexo == "M" and int(doente.temDoenca) == 0:
                    mascu_sem_doenca += 1

            if doente.sexo == "F" and int(doente.temDoenca) == 1:
                    fem_com_doenca += 1

            if doente.sexo == "F" and int(doente.temDoenca) == 0:
                    fem_sem_doenca += 1

        print(" ")
        print(f"Doentes masculinos com doença = {mascu_com_doenca}")
        print(f"Doentes masculinos sem doença = {mascu_sem_doenca}")
        print(f"Doentes femininos com doença = {fem_com_doenca}")
        print(f"Doentes femininos sem doença = {fem_sem_doenca}")
        print(" ")

    ####################################################################################################################

    def maior_idade(self):
        maior = 0

        for doente in self.lista_doentes:
            if int(doente.idade) >= int(maior):
                maior = doente.idade

        return maior

    ####################################################################################################################

    def menor_idade(self):
        menor = 100

        for doente in self.lista_doentes:
            if int(doente.idade) <= int(menor):
                menor = doente.idade

        return menor

    ####################################################################################################################

    # resolução javarda e feita à pressa
    def calcula_dist_etaria(self):
        lim_sup = self.maior_idade()   # o limite superior de faixa etaria é 77

        # criar os contadores para os grupos etarios
        faixa_25_29 = 0
        faixa_25_29_DOENCA = 0

        faixa_30_34 = 0
        faixa_30_34_DOENCA = 0

        faixa_35_39 = 0
        faixa_35_39_DOENCA = 0

        faixa_40_44 = 0
        faixa_40_44_DOENCA = 0

        faixa_45_49 = 0
        faixa_45_49_DOENCA = 0

        faixa_50_54 = 0
        faixa_50_54_DOENCA = 0

        faixa_55_59 = 0
        faixa_55_59_DOENCA = 0

        faixa_60_64 = 0
        faixa_60_64_DOENCA = 0

        faixa_65_69 = 0
        faixa_65_69_DOENCA = 0

        faixa_70_74 = 0
        faixa_70_74_DOENCA = 0

        faixa_75_79 = 0
        faixa_75_79_DOENCA = 0

        for doente in self.lista_doentes:
            idade = int(doente.idade)
            doenca = int(doente.temDoenca)

            if idade >= 25 and idade <= 29:
                if doenca == 0: faixa_25_29 += 1
                if doenca == 1: faixa_25_29_DOENCA += 1

            if idade >= 30 and idade <= 34:
                if doenca == 0: faixa_30_34 += 1
                if doenca == 1: faixa_30_34_DOENCA += 1

            if idade >= 35 and idade <= 39:
                if doenca == 0: faixa_35_39 += 1
                if doenca == 1: faixa_35_39_DOENCA += 1

            if idade >= 40 and idade <= 44:
                if doenca == 0: faixa_40_44 += 1
                if doenca == 1: faixa_40_44_DOENCA += 1

            if idade >= 45 and idade <= 49:
                if doenca == 0: faixa_45_49 += 1
                if doenca == 1: faixa_45_49_DOENCA += 1

            if idade >= 50 and idade <= 54:
                if doenca == 0: faixa_50_54 += 1
                if doenca == 1: faixa_50_54_DOENCA += 1

            if idade >= 55 and idade <= 59:
                if doenca == 0: faixa_55_59 += 1
                if doenca == 1: faixa_55_59_DOENCA += 1

            if idade >= 60 and idade <= 64:
                if doenca == 0: faixa_60_64 += 1
                if doenca == 1: faixa_60_64_DOENCA += 1

            if idade >= 65 and idade <= 69:
                if doenca == 0: faixa_65_69 += 1
                if doenca == 1: faixa_65_69_DOENCA += 1

            if idade >= 70 and idade <= 74:
                if doenca == 0: faixa_70_74 += 1
                if doenca == 1: faixa_70_74_DOENCA += 1

            if idade >= 75 and idade <= 79:
                if doenca == 0: faixa_75_79 += 1
                if doenca == 1: faixa_75_79_DOENCA += 1


        print(" ")
        print(f"Faixa etaria [25-29]: Sem Doença = {faixa_25_29}; Com Doença = {faixa_25_29_DOENCA}")
        print(f"Faixa etaria [30-34]: Sem Doença = {faixa_30_34}; Com Doença = {faixa_30_34_DOENCA}")
        print(f"Faixa etaria [35-39]: Sem Doença = {faixa_35_39}; Com Doença = {faixa_35_39_DOENCA}")
        print(f"Faixa etaria [40-44]: Sem Doença = {faixa_40_44}; Com Doença = {faixa_40_44_DOENCA}")
        print(f"Faixa etaria [45-49]: Sem Doença = {faixa_45_49}; Com Doença = {faixa_45_49_DOENCA}")
        print(f"Faixa etaria [50-54]: Sem Doença = {faixa_50_54}; Com Doença = {faixa_50_54_DOENCA}")
        print(f"Faixa etaria [55-59]: Sem Doença = {faixa_55_59}; Com Doença = {faixa_55_59_DOENCA}")
        print(f"Faixa etaria [60-64]: Sem Doença = {faixa_60_64}; Com Doença = {faixa_60_64_DOENCA}")
        print(f"Faixa etaria [65-69]: Sem Doença = {faixa_65_69}; Com Doença = {faixa_65_69_DOENCA}")
        print(f"Faixa etaria [70-74]: Sem Doença = {faixa_70_74}; Com Doença = {faixa_70_74_DOENCA}")
        print(f"Faixa etaria [75-79]: Sem Doença = {faixa_75_79}; Com Doença = {faixa_75_79_DOENCA}")
        print(" ")

    ####################################################################################################################

    def maior_colestrol(self):
        maior = 0

        for doente in self.lista_doentes:
            if int(doente.colestrol) >= int(maior):
                maior = doente.colestrol

        return maior

    ####################################################################################################################

    def menor_colestrol(self):
        menor = 100

        for doente in self.lista_doentes:
            if int(doente.colestrol) <= int(menor):
                menor = doente.colestrol

        return menor


    ####################################################################################################################

    def nivel_colestrol_ALT(self, colestrol):
        # avalia o nivel de colestrol passado como argumento

        nivel = int(colestrol / 10)

        return nivel


    ####################################################################################################################

    def total_doentes(self):
        # apenas devolve o total de doentes
        return len(self.lista_doentes)


    ####################################################################################################################

    def calcula_dist_colestrol(self):
        lim_sup = self.maior_colestrol()  # o limite superior de colestrol = 603
        nivel_sup = self.nivel_colestrol_ALT(int(lim_sup))

        # criar os os niveis de colestrol
        niveis = [0] * (nivel_sup + 1)

        for doente in self.lista_doentes:
            nivel = int(doente.nivel_colestrol())

            niveis[int(nivel)] += 1

        print(" ")
        print(f"NÍVEL DE COLESTROL ---> NÚMERO DE DOENTES")
        print(" ")
        for i in range(len(niveis)):
            if(niveis[i] != 0 ):
                print(f"Nível {i} ---> {niveis[i]}")

        print(" ")

    ####################################################################################################################


    # calcula na mesma a distribuição mas imprime o resultado de forma diferente
    def tabela_colestrol(self):
        lim_sup = self.maior_colestrol()  # o limite superior de colestrol = 603
        nivel_sup = self.nivel_colestrol_ALT(int(lim_sup))

        # criar os os niveis de colestrol
        niveis = [0] * (nivel_sup + 1)

        for doente in self.lista_doentes:
            nivel = int(doente.nivel_colestrol())

            niveis[int(nivel)] += 1


        
        # "+--------------------+-------------------+")
        # "| NÍVEL DE COLESTROL | NÚMERO DE DOENTES |")
        # "+--------------------+-------------------+")
        # "| 1                  | 0                 |")
        # "| 1                  | 00                |")
        # "| 1                  | 000               |")
        # "+--------------------+-------------------+")
        # "| 10                 | 0                 |")
        # "| 10                 | 00                |")
        # "| 10                 | 000               |")
        # "+--------------------+-------------------+")
        # "| 100                | 0                 |")
        # "| 100                | 00                |")
        # "| 100                | 000               |")
        # "+--------------------+-------------------+")



        print(" ")
        print("+--------------------+-------------------+")
        print("| NÍVEL DE COLESTROL | NÚMERO DE DOENTES |")
        print("+--------------------+-------------------+")

        for i in range(len(niveis)):
            digits1 = len(str(i))
            digits2 = len(str(niveis[i]))

            if digits1 == 1 and digits2 == 1 :
                print(f"| {i}                  | {niveis[i]}                 |")
                print("+--------------------+-------------------+")

            if digits1 == 1 and digits2 == 2:
                print(f"| {i}                  | {niveis[i]}                |")
                print("+--------------------+-------------------+")

            if digits1 == 1 and digits2 == 3:
                print(f"| {i}                  | {niveis[i]}               |")
                print("+--------------------+-------------------+")

            #-------------------------------------------------------------------------

            if digits1 == 2 and digits2 == 1:
                print(f"| {i}                 | {niveis[i]}                 |")
                print("+--------------------+-------------------+")

            if digits1 == 2 and digits2 == 2:
                print(f"| {i}                 | {niveis[i]}                |")
                print("+--------------------+-------------------+")

            if digits1 == 2 and digits2 == 3:
                print(f"| {i}                 | {niveis[i]}               |")
                print("+--------------------+-------------------+")

            #-------------------------------------------------------------------------

            if digits1 == 3 and digits2 == 1:
                print(f"| {i}                | {niveis[i]}                 |")
                print("+--------------------+-------------------+")

            if digits1 == 3 and digits2 == 2:
                print(f"| {i}                | {niveis[i]}                |")
                print("+--------------------+-------------------+")

            if digits1 == 3 and digits2 == 3:
                print(f"| {i}                | {niveis[i]}               |")
                print("+--------------------+-------------------+")

        print(" ")


    ####################################################################################################################

    # calcula na mesma a distribuição mas imprime o resultado de forma diferente
    def tabela_sexo(self):
        mascu_com_doenca = 0
        mascu_sem_doenca = 0

        fem_com_doenca = 0
        fem_sem_doenca = 0

        for doente in self.lista_doentes:
            if doente.sexo == "M" and int(doente.temDoenca) == 1:
                mascu_com_doenca += 1

            if doente.sexo == "M" and int(doente.temDoenca) == 0:
                mascu_sem_doenca += 1

            if doente.sexo == "F" and int(doente.temDoenca) == 1:
                fem_com_doenca += 1

            if doente.sexo == "F" and int(doente.temDoenca) == 0:
                fem_sem_doenca += 1

        # "                 +------------+------------+")
        # "                 | SEM DOENÇA | COM DOENÇA |")
        # "+----------------+------------+------------+")
        # "| MASCULINO      | 1          | 1          |")
        # "+----------------+------------+------------+")
        # "| FEMININO       | 1          | 00         |")
        # "+----------------+------------+------------+")


        print(" ")
        print("                 +------------+------------+")
        print("                 | SEM DOENÇA | COM DOENÇA |")
        print("+----------------+------------+------------+")
        print(f"| MASCULINO      | {mascu_sem_doenca}        | {mascu_com_doenca}        |")
        print("+----------------+------------+------------+")
        print(f"| FEMININO       | {fem_sem_doenca}        | {fem_com_doenca}         |")
        print("+----------------+------------+------------+")
        print(" ")

    ####################################################################################################################

    def tabela_etaria(self):
        lim_sup = self.maior_idade()  # o limite superior de faixa etaria é 77

        # criar os contadores para os grupos etarios
        faixa_25_29 = 0
        faixa_25_29_DOENCA = 0

        faixa_30_34 = 0
        faixa_30_34_DOENCA = 0

        faixa_35_39 = 0
        faixa_35_39_DOENCA = 0

        faixa_40_44 = 0
        faixa_40_44_DOENCA = 0

        faixa_45_49 = 0
        faixa_45_49_DOENCA = 0

        faixa_50_54 = 0
        faixa_50_54_DOENCA = 0

        faixa_55_59 = 0
        faixa_55_59_DOENCA = 0

        faixa_60_64 = 0
        faixa_60_64_DOENCA = 0

        faixa_65_69 = 0
        faixa_65_69_DOENCA = 0

        faixa_70_74 = 0
        faixa_70_74_DOENCA = 0

        faixa_75_79 = 0
        faixa_75_79_DOENCA = 0

        for doente in self.lista_doentes:
            idade = int(doente.idade)
            doenca = int(doente.temDoenca)

            if idade >= 25 and idade <= 29:
                if doenca == 0: faixa_25_29 += 1
                if doenca == 1: faixa_25_29_DOENCA += 1

            if idade >= 30 and idade <= 34:
                if doenca == 0: faixa_30_34 += 1
                if doenca == 1: faixa_30_34_DOENCA += 1

            if idade >= 35 and idade <= 39:
                if doenca == 0: faixa_35_39 += 1
                if doenca == 1: faixa_35_39_DOENCA += 1

            if idade >= 40 and idade <= 44:
                if doenca == 0: faixa_40_44 += 1
                if doenca == 1: faixa_40_44_DOENCA += 1

            if idade >= 45 and idade <= 49:
                if doenca == 0: faixa_45_49 += 1
                if doenca == 1: faixa_45_49_DOENCA += 1

            if idade >= 50 and idade <= 54:
                if doenca == 0: faixa_50_54 += 1
                if doenca == 1: faixa_50_54_DOENCA += 1

            if idade >= 55 and idade <= 59:
                if doenca == 0: faixa_55_59 += 1
                if doenca == 1: faixa_55_59_DOENCA += 1

            if idade >= 60 and idade <= 64:
                if doenca == 0: faixa_60_64 += 1
                if doenca == 1: faixa_60_64_DOENCA += 1

            if idade >= 65 and idade <= 69:
                if doenca == 0: faixa_65_69 += 1
                if doenca == 1: faixa_65_69_DOENCA += 1

            if idade >= 70 and idade <= 74:
                if doenca == 0: faixa_70_74 += 1
                if doenca == 1: faixa_70_74_DOENCA += 1

            if idade >= 75 and idade <= 79:
                if doenca == 0: faixa_75_79 += 1
                if doenca == 1: faixa_75_79_DOENCA += 1

        print(" ")
        print("+----------------------+-----------------+------------------+")
        print(f"| Faixa etaria [25-29] | Sem Doença = {faixa_25_29}  | Com Doença = {faixa_25_29_DOENCA}   |")
        print("+----------------------+-----------------+------------------+")
        print(f"| Faixa etaria [30-34] | Sem Doença = {faixa_30_34} | Com Doença = {faixa_30_34_DOENCA}   |")
        print("+----------------------+-----------------+------------------+")
        print(f"| Faixa etaria [35-39] | Sem Doença = {faixa_35_39} | Com Doença = {faixa_35_39_DOENCA}  |")
        print("+----------------------+-----------------+------------------+")
        print(f"| Faixa etaria [40-44] | Sem Doença = {faixa_40_44} | Com Doença = {faixa_40_44_DOENCA}  |")
        print("+----------------------+-----------------+------------------+")
        print(f"| Faixa etaria [45-49] | Sem Doença = {faixa_45_49} | Com Doença = {faixa_45_49_DOENCA}  |")
        print("+----------------------+-----------------+------------------+")
        print(f"| Faixa etaria [50-54] | Sem Doença = {faixa_50_54} | Com Doença = {faixa_50_54_DOENCA}  |")
        print("+----------------------+-----------------+------------------+")
        print(f"| Faixa etaria [55-59] | Sem Doença = {faixa_55_59} | Com Doença = {faixa_55_59_DOENCA} |")
        print("+----------------------+-----------------+------------------+")
        print(f"| Faixa etaria [60-64] | Sem Doença = {faixa_60_64} | Com Doença = {faixa_60_64_DOENCA} |")
        print("+----------------------+-----------------+------------------+")
        print(f"| Faixa etaria [65-69] | Sem Doença = {faixa_65_69} | Com Doença = {faixa_65_69_DOENCA}  |")
        print("+----------------------+-----------------+------------------+")
        print(f"| Faixa etaria [70-74] | Sem Doença = {faixa_70_74}  | Com Doença = {faixa_70_74_DOENCA}  |")
        print("+----------------------+-----------------+------------------+")
        print(f"| Faixa etaria [75-79] | Sem Doença = {faixa_75_79}  | Com Doença = {faixa_75_79_DOENCA}   |")
        print("+----------------------+-----------------+------------------+")
        print(" ")