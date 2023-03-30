# Atividade Prática 02
# Parte 2 - Pedra, Papel, Tesoura

import random
import time

print('Seja muito bem vindo(a) à nossa plataforma de jogos, e você escolheu jogar hoje: Pedra, Papel, Tesoura')
continuar = True 
while continuar: 
    time.sleep(1.5)

    jogada = input('Escolha entre: Pedra, Papel ou Tesoura (0: Pedra, 1: Papel, 2: Tesoura)')
    
    perguntas = [
        'Será que temos um(a) vencedor(a)?',
        'Será que você ganhou da máquina?',
        'Será que você foi páreo(a) para vencer?',
        'Será que teremos um rei ou rainha desse jogo?',
        'Que jogada! Veja se você ganhou...',
        'Será que essa foi uma jogada de mestre?',
    ]
    
    pergunta_qualquer = random.choice(perguntas)
    time.sleep(2.5)
    print(f'\n{pergunta_qualquer}\n')
    time.sleep(2.5)
    
    jogada = int(jogada)
    resultado = random.randint(0,2)
    
    print(f'Você jogou: {jogada}')
    print(f'Seu oponente jogou: {resultado}')
    
    if jogada == resultado:
        print('Uii, empate! :/')
    elif jogada == 0 and resultado == 1:
        print("Puxa, você perdeu! :(")
    elif jogada == 0 and resultado == 2: 
        print('Uhull, você ganhou! :)')
    elif jogada == 1 and resultado == 0:
        print('Uhull, você ganhou! :)')
    elif jogada == 1 and resultado == 2:
        print('Puxa, você perdeu! :(')
    elif jogada == 2 and resultado == 0:
        print('Puxa, você perdeu! :(')
    elif jogada == 2 and resultado == 1:
        print('Uhull, você ganhou! :)')
    
    time.sleep(4.0)

    continuar = input('\nDeseja continuar? (1: Sim ; 0: Não)\n')
    continuar = bool(int(continuar))
    if not continuar:
        print('\nObrigado por jogar e volte sempre!\n')
    else:
        print('\nE lá vamos nós!\n')

# Atividade Prática 02
# Parte 1: Cara ou Coroa 

time.sleep(2.0)

print('Seja bem vindo à nossa plataforma de jogos, e hoje você escolhleu jogar: Cara ou Coroa!')

continuar = True
while continuar:
    time.sleep(1.5)

    jogada = input('Escolha entre Cara ou Coroa. (0: Cara ; 1: Cora)')

    perguntas = [
        "Um(a) gênio(a) da jogada?",
        "Será que você é bom em prever as jogadas?",
        "Um(a) Ás dos jogos?",
        "Sabia que você tem 50% de chance de ganhar ou de perder?",
        "Será que a Coroa da moeda lhe faz tornar-se um rei ou rainha?",
        "Fiquei sem criatividade, vamos para o resultado.",
    ]

    pergunta_qualquer = random.choice(perguntas)
    time.sleep(2.5)
    print(f'\n{pergunta_qualquer}\n')
    time.sleep(2.5)

    jogada = int(jogada)
    resultado = random.randint(0,1)
   
    print(f'Você jogou: {jogada}')
    print(f'O reultado foi: {resultado}')
    if jogada == resultado:
        print("\nUhuul, você ganhou essa!\n")
    else:
        print("\nPuxa vida! você perdeu.\n")
    
    time.sleep(3.0)

    continuar = input('\nDeseja continuar? (1: Sim ; 0: Não)\n')
    continuar = bool(int(continuar))
    if not continuar:
        print('\nObrigado por jogar e volte sempre quando quiser!\n')
    else:
        print('\nVamos nessa!\n')