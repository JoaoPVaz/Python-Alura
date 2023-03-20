import random
def jogar():
    print('='*30)
    print('Bem Vindo ao jogo de adivinhacao !!')
    print('='*30)

    numero_secreto = random.randrange(1,101)
    tentativas = 0
    rodada = 1
    pontos = 1000

    print('Qual o nivel de Dificuldade ? ')
    print('(1)Facil|(2) Medio|(3) Dificil')
    print('='*30)

    nivel = int(input('Digite o nivel de Dificuldade: '))

    if(nivel == 1):
        tentativas = 20
    elif(nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range (1, tentativas + 1):
        print(f'Tentativa {rodada} de {tentativas}')
        chute = int(input("Digite um numero entre 1 e 100: "))
        print(f'Voce digitou o numero {chute}')
        rodada += 1

        if (chute < 1 or chute > 100):
            print('Valor invalido, tente novamente ! ')
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print('Voce adivinhou o numero secreto.', end=' ')
            print('Parabens !!!')
            print('=' * 30)
            break
        else:
            if (maior):
                print('Voce errou, o seu chute foi maior do que o numero secreto.', end=' ')
                print('Tente Novamente !!')
                print('=' * 30)
            elif (menor):
                print('Voce errou, o seu chute foi menor do que o numero secreto', end=' ')
                print('Tente Novamente !!')
                print('=' * 30)
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print(f'Voce fez {pontos} pontos no jogo !')
    print(f'O numero sorteado foi {numero_secreto} !')
    print('Fim de Jogo.')

if(__name__== '__main__'):
    jogar()
