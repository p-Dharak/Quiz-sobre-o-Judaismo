#importando bibliotecas

import time #biblioteca time, usaremos uma função dela, para manipular o tempo de execucao do console
import sys #biblioteca sys, usaremos uma funçao presente nela,para fechar o console
import os #biblioteca os, usaremos uma funçao presente nela,para limpar o console

#Introducao ao programa
nome=input("Qual o seu nome:")#solicita o nome do usuario 
print("\nQue nome bonito, AGUARDE, o sistema esta carregando....")
time.sleep ( 5 )
print("\n------------------------------------------------------------------")
print("\nSeja bem-vindo(a):", nome , "!")
print("\n------------------------------------------------------------------")
print("\nAGUARDE MAIS UM MOMENTO....")
time.sleep(15)
comando=input("\nPressione ENTER para continuar:")
os.system('cls')
print("\n\n------------------------------------------------------------------")

#Menu de opcoes
print("\n\nVoce esta no menu de opçoes, para prosseguir, escolha uma!")

print("\n(1). Regras do Quiz e Programa")
print("\n(2). Quiz sobre Judaismo")
print("\n(3). Sair")

print("\n------------------------------------------------------------------")

opcao=input("\nDigite aqui sua opção:")#solicita a opcao do usuario


print("\n------------------------------------------------------------------")

#Se o usuario digitou 1, o programa executa a opcao 1
if opcao =='1':
    os.system('cls')#limpa a tela do console
    print("\n\t\tRegras do Quiz e Programa")
    print("\n------------------------------------------------------------------")
    print("\n1. Nao pesquisar as respostas no Google")
    print("\n2.Não usar acentos e caractereres especiais, pois, o programa buga")
    print("\n3.Caso erre uma pergunta, o programa é fechado, caso queira jogar novamente, abra novamente o programa")
    comando2=input("\nPressione ENTER para continuar:")
    os.system('cls')
    print("\n\n FECHANDO O PROGRAMA, CASO QUEIRA USA-LO DE NOVO, ABRA-O NOVAMENTE")
    time.sleep(19)#faz com que o console espere 15 segundos antes de executar a proxima acao
    sys.exit(0)#fecha o console

    #Se o usuario digitou 2, o programa executa a opcao 2
elif opcao == '2':
    os.system('cls')
    print("\n------------------------------------------------------------------")
    print("\n\t\t Quiz sobre Judaismo")
    print("\nQuestao 1 - Assinale a alternativa correta....")
    print("\n1.Torá é uma festa cristã, onde se comemora o nascimento de Buda ")
    print("\n2.Torá é uma loja de artigos religiosos")
    print("\n3.Torá é a biblia hebraica, um conjunto de textos sagrados para os judeus, onde são narrados diversos eventos de acordo com a visão da religião judaica")
    print("\n4.Torá é uma comida Australiana")
    print("\n5.Torá é um templo religioso")
    print("\n6.Torá não é algo sagrado para os judeus.")
    resposta=input("\n\nDigite o numero da alternativa correta:")
    if (resposta=="3"):
        time.sleep ( 6 )
        print("\n\n------------------------------------------------------------------")
        print("\nParabens", nome , "voce acertou. Carregando a proxima pergunta!")
        time.sleep(15)
        os.system('cls')
        print("\n\n------------------------------------------------------------------")
        print("Questao 2 - Qual das opcoes abaixo,  esta correta")
        print("\n1.Uma Sinagoga é um local onde são realizados jogos de futebol")
        print("\n2.Uma Sinagoga é um local onde são realizados Torneios de Luta")
        print("\n3.Uma Sinagoga é um local onde Mulçumanos oram para Alá")
        print("\n4.Uma Sinagoga é um local onde Hinduistas fazem seus Ritos Religiosos")
        print("\n5.Uma Sinagoga é um parque religioso")
        print("\n6.Uma Sinagoga é um templo religioso, onde a comunidade judaica se reune, e é dirigida por um Rabino")

        resposta2=input("\n\nDigite o numero da opcao correta:")
        print("\n\n------------------------------------------------------------------")
        if resposta2== '6':
            print("\nParabens", nome , "voce acertou. Carregando a proxima pergunta!")
            time.sleep(15)
            os.system('cls')
            print("\n\n------------------------------------------------------------------")
            print("Questao 3 - Qual das alternativas abaixo se encontra incorreta")
            print("\n1.O monoteismo é a crença em um unico deus")
            print("\n2.Talmude é a coleção de leis, ensinamentos e contos do judaismo")
            print("\n3.´Tefilá é a prece e ligação com deus")
            print("\n4.Berit Mitá é um feriado religioso.Nele é comemorado o nascimento de Cristo")
            print("\n5.Teshuvá são os  arrependimentos e o retorno às origens quando são cometidos erros pelos adeptos")
            resposta3=input("\n\nDigite o numero da alternativa correta:")
            print("\n\n------------------------------------------------------------------")
        if resposta3== '4':
            print("\nParabens", nome , "voce acertou. Carregando a proxima pergunta!")
            time.sleep(15)
            os.system('cls')
            print("\n\n------------------------------------------------------------------")
            print("Questao 4 - Qual das alternativas abaixo se encontra incorreta")
            print("\n1.Tsedacá é a caridade com sentido de justiça")
            print("\n2.Bar Mitzvah é um processo pelo qual, as meninas realizam a leitura do Torá aos 14 anos, assim marcando a maturidade religiosa")
            print("\n3.O judaismo conta com mais de 15 milhões de fiéis")
            print("\n4.Religiões abraâmicas são aquelas que descendem de Abraão")
            resposta4=input("\n\nDigite o numero da alternativa correta:")
            print("\n\n------------------------------------------------------------------")
        if resposta4== '2':
            print("\nParabens", nome , "voce acertou. Carregando a proxima pergunta!")
            time.sleep(15)
            print("\n\n------------------------------------------------------------------")
            os.system('cls')
            print("Questao 5 - Qual das alternativas abaixo se encontra incorreta")
            print("\n1.Bat Mitzvah é um processo pelo qual, os meninos realizam a leitura do Torá aos 17 anos, assim marcando a maturidade religiosa ")
            print("\n2.Talmude é a coleção de leis, ensinamentos e contos do judaismo")
            print("\n3.Torá é a biblia hebraica, um conjunto de textos sagrados para os judeus, onde são narrados diversos eventos de acordo com a visão da religião judaica")
            print("\n4.Tefilá é a prece e ligação com deus")
            print("\n5.YHWH é também conhecido com Javé ou Jeová")
            resposta5=input("\n\nDigite o numero da alternativa correta:")
            print("\n\n------------------------------------------------------------------")
        if resposta5== '1':
            time.sleep(5)
            print("\nNossa voce eh incrivel", nome , "! Voce acertou todas as perguntas.")
            time.sleep(5)
            comando3=input("\nPressione ENTER para continuar:")
            time.sleep(5)
            os.system('cls')
            print("\nFIM DE JOGO, VOCE EH UM ESPECIALISTA EM RITOS RELIGIOSOS DO JUDAISMO!!!!!")
            comando3=input("\nPressione ENTER para continuar:")
            os.system('cls')
            print("Fechando o programa...Obrigado por jogar...")
            time.sleep(7)
            sys.exit(0)

        else:
             print("\n\n------------------------------------------------------------------")
             print("\nSinto muito", nome , ",voce errou, fechando o programa....")
             time.sleep(8)
             sys.exit(0)
    else:
        print("\n\n------------------------------------------------------------------")
        print("\nSinto muito", nome , ",voce errou, fechando o programa....")
        time.sleep(8)
        sys.exit(0)

elif opcao == '3':
    print("\n\nENCERRANDO O PROGRAMA, PARA JOGAR ABRA-O NOVAMENTE!!!!!")
    time.sleep(8)
    sys.exit(0)

