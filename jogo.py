import forca
import adivinhacao

def escolhe_jogo():
    print('='*30)
    print('Escolha seu Jogo !!')
    print('='*30)

    print('(1) Forca (2) Adivinhacao')

    jogo = int(input('Qual o jogo ? '))

    if(jogo == 1):
        print('Jogando Forca')
        forca.jogar()
    elif (jogo == 2):
        print('Jogando Adivinhacao')
        adivinhacao.jogar()

if(__name__=='__main__'):
    escolhe_jogo()
