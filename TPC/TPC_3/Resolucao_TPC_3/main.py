import re


def main():
    f = open("processos.txt")

    all = re.compile(
        r'(?P<id>\d+)::(?P<ano>\d{4})-(?P<mes>\d{2})-(?P<dia>\d{2})::(?P<nome>[a-zA-Z ]+)::(?P<nomeP>[a-zA-Z ]+)::(?P<nomeM>[a-zA-Z ]+)::(?P<nomeEtc>[\w\.\, ]+)?::\n')
    pnome = re.compile(r'^[a-zA-Z]+')
    unome = re.compile(r'[a-zA-Z]+$')
    relacao = re.compile(r',(\w[a-zA-Z ]+)\.\s*Proc\.')

    PPA = {}  # processos por ano
    anos = []

    PrimeiroNomeSec = {}
    UltimoNomeSec = {}

    DR = {}  # Dicionario de relações

    for line in f:
        r = all.fullmatch(line)
        if r != None:
            _, ano, _, _, nome, _, _, extraRelacao = r.groups()
            if ano in PPA:
                PPA[ano] += 1
            else:
                PPA[ano] = 1
                anos.append(ano)

            seculo = (int(ano) - 1) // 100 + 1
            primeiroNome = pnome.search(nome)[0]
            ultimoNome = unome.search(nome)[0]

            if (extraRelacao != None):
                relacoes = relacao.findall(extraRelacao)
                if (relacoes):
                    for r in relacoes:
                        if r in DR:
                            DR[r] += 1
                        else:
                            DR[r] = 1

            if seculo not in PrimeiroNomeSec:
                PrimeiroNomeSec[seculo] = {}
                UltimoNomeSec[seculo] = {}

            if primeiroNome in PrimeiroNomeSec[seculo]:
                PrimeiroNomeSec[seculo][primeiroNome] += 1
            else:
                PrimeiroNomeSec[seculo][primeiroNome] = 1

            if ultimoNome in UltimoNomeSec[seculo]:
                UltimoNomeSec[seculo][ultimoNome] += 1
            else:
                UltimoNomeSec[seculo][ultimoNome] = 1

    saida = -1
    while saida != 0:
        print(" ")
        print("------------------------------ TPC 3 ------------------------------")
        print(" ")
        print("a) - Calcular a frequência de processos por ano")
        print("b) - Calcular a frequência de nomes próprios e apelidos por séculos")
        print("c) - Calcular a frequência dos vários tipos de relação")
        print("d) - Converter os 20 primeiros registos num novo ficheiro em formato Json")
        print("0  - Saír")
        print(" ")
        print("-------------------------------------------------------------------")
        print(" ")


        saida = input("---> ")

        if (saida == 'a'):
            anos.sort()
            print(' ')
            for a in anos:
                print(f"{a}: {PPA[a]}")

            print(' ')
            l = input("prima enter para continuar")

        elif (saida == 'b'):
            nomeSec = dict(sorted(PrimeiroNomeSec.items()))


            print(' ')

            for s in nomeSec:
                aux = reversed(dict(sorted(nomeSec[s].items(), key=lambda item: item[1])))
                i = 1
                print(' ')
                print(f' Primeiro nome mais usado no seculo {s} ')
                for n in aux:
                    print(f'    {i}º nome: {n}  {nomeSec[s][n]}')
                    i += 1
                    if i == 6:
                        break

            print(' ')
            print('-------------------------------------')
            print(' ')

            nomeSec = dict(sorted(UltimoNomeSec.items()))
            for s in nomeSec:
                aux = reversed(dict(sorted(nomeSec[s].items(), key=lambda item: item[1])))
                i = 1
                print(' ')
                print(f' Apelido nome mais usado no seculo {s} ')

                for n in aux:

                    print(f'    {i}º nome: {n}  {nomeSec[s][n]}')
                    i += 1
                    if i == 6:
                        break


            print(' ')

            l = input("prima enter para continuar")


        elif (saida == 'c'):
            DRaux = reversed(dict(sorted(DR.items(), key=lambda item: item[1])))
            print(' ')
            print(f' Numero de relações de tipo')
            for r in DRaux:
                print(f'   {r} : {DR[r]}')

            print(' ')
            l = input("prima enter para continuar")

        elif (saida == 'd'):
            print("")
            print("INDISPONIVEL")
            print("")

        elif (saida == '0'):
            print("")
            print("Saindo.......")
            print("")
            return 0

        else:
            print("Opção inválida...")
            l = input("prima enter para continuar")


if __name__ == "__main__":
    main()
