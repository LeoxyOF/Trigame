# Trigame By LeoxyOF(https://github.com/LeoxyOF)

while True:
    from random import randint
    from time import sleep
    print('\033[1;31;40m-=\033[m'*14)
    print('\033[1;31;40m Seja Bem-vindo ao Trigame! \033[m')
    print('\033[1;31;40m-=\033[m'*14)
    sleep(2)
    print('\033[1;31;40m-\033[m'*31)
    print('\033[1;31;40mVocê tem três opções de jogo >>\033[m')
    print('\033[1;31;40m-\033[m'*31)
    sleep(2)
    print('\033[1;32m-=\033[m'*10)
    print('\033[1;32m    Tabuada = 1     \033[m')
    print('\033[1;32m-=\033[m'*10)
    sleep(1)
    print('\033[1;36m-=\033[m'*17)
    print('\033[1;36m     Jogo da Adivinhação = 2      \033[m')
    print('\033[1;36m-=\033[m'*17)
    sleep(1)
    print('\033[1;35m-=\033[m'*10)
    print('\033[1;35m      Quiz = 3      \033[m')
    print('\033[1;35m-=\033[m'*10)
    sleep(2)
    resp = str(input('\033[1;31;40mQual é sua escolha? >>\033[m')).strip()
    if resp == '1':
        print('\033[1;33mCarregando Jogo...')
        sleep(3)
        print('\033[1;31mX \033[1;36mVocê escolheu a Tabuada')
        print('\033[1;33mFunção >> Criar uma tabela automáticamente do valor que você colocar\033[m')
        A = int(input('\033[1;31mDigite Um Número: \033[m'))
        print('\033[1;34m-='*15)
        print(f'\033[1;34m        Tabuada de {A}\033[m')
        print('\033[1;34m-='*15)
        for c in range(1, 11):
            print(f'\033[1;3{c}m{A}x{c} = {A * c}')
            sleep(0.5)
    elif resp == '2':
        print('\033[1;33mCarregando Jogo...')
        sleep(3)
        print("\033[1;31mX \033[m\033[1;36mVocê escolheu o Jogo da Adivinhação\033[m")
        print('\033[1;31m----Jogo da Adivinhação----\033[m')
        print("\033[1;30mObjetivo >> Adivinhe o Número que o computador escolheu de 0 á 10!")
        pc = randint(0, 10)
        cont = 0
        while resp != pc:
            resp = int(input('\033[36mNúmero >> '))
            if resp > 10:
                print('\033[31mO Limite é \033[33m10\033[31m!')
            elif resp < pc:
                print('\033[31mResposta incorreta! Tente novamente \033[39m(Mais \033[32m+\033[39m)')
            elif resp > pc:
                print('\033[31mResposta incorreta! Tente novamente \033[39m(Menos \033[31m-\033[39m)')
            cont += 1
        if cont == 1:
            print(f'\033[1;32mVocê Acertou!\033[33m Foram Necessários Apenas {cont} Palpite!')
        if cont > 1:
            print(f'\033[1;32mVocê Acertou!\033[33m Foram Necessários {cont} Palpites!')
    elif resp == '3':
        cont = 10
        print('\033[1;33mCarregando Jogo...')
        sleep(3)
        print('\033[1;31mX \033[1;36mVocê escolheu o Quiz')
        print('\033[1;31m-='*9)
        print('\033[1;31m       Quiz')
        print('\033[1;31m-=' * 9)
        print('\033[1;35mObjetivo >> Acertar todas as Perguntas')
        sleep(3)
        print('\033[1;33mPrimeira pergunta em 5 segundos...')
        sleep(5)
        print('\033[1;34m(1) Qual é o maior país do mundo?')
        sleep(0.5)
        print('')
        print('\033[1;33m(A) Alemanha')
        sleep(0.5)
        print('')
        print('\033[1;33m(B) Japão')
        sleep(0.5)
        print('')
        print('\033[1;33m(C) Rússia')
        sleep(0.5)
        print('')
        print('\033[1;33m(D) Estados Unidos')
        sleep(0.5)
        print('')
        print('\033[1;33m(E) Brasil')
        sleep(1)
        print('')
        respq1 = str(input('\033[1;31mSua Resposta >> ')).strip().lower()
        print('\033[1;33mProcessando...')
        sleep(3)
        if respq1 == 'c':
            print('\033[1;32m✔ Resposta Correta! +1 ponto :)')
        else:
            print('\033[1;31mX Resposta Incorreta! 0 pontos :(')
            cont -= 1
        sleep(1)
        print('\033[1;36mA Rússia é de longe o maior país do mundo. Com mais de 17 milhões (17.000.000) de', end='')
        print('quilômetros quadrados, tem quase o dobro do tamanho do canadá! Uma grande parte', end='')
        print(' da Ásia e da Europa pertencem à Rússia.')
        sleep(5)
        print('\033[1;33mPróxima pergunta em 5 segundos...')
        sleep(5)
        print('\033[1;34m(2) Qual dessas aves não voa?')
        sleep(0.5)
        print('')
        print('\033[1;33m(A) Pinguim')
        sleep(0.5)
        print('')
        print('\033[1;33m(B) Galinha')
        sleep(0.5)
        print('')
        print('\033[1;33m(C) Cegonha')
        sleep(0.5)
        print('')
        print('\033[1;33m(D) Pato')
        sleep(0.5)
        print('')
        print('\033[1;33m(E) Peru')
        sleep(1)
        print('')
        respq2 = str(input('\033[1;31mSua Resposta >> ')).strip().lower()
        print('\033[1;33mProcessando...')
        sleep(3)
        if respq2 == 'a':
            print('\033[1;32m✔ Resposta Correta! +1 ponto :)')
        else:
            print('\033[1;31mX Resposta Incorreta! 0 pontos :(')
            cont -= 1
        sleep(1)
        print("""\033[1;36mO pinguim, apesar de ser uma ave, não voa. Isso deve-se ao fato da adaptação que esses 
        animais sofreram ao longo dos anos. Cientistas acreditam que eles
        foram aos poucos deixando de voar e se tornaram exímios nadadores.""")
        sleep(5)
        print('\033[1;33mPróxima pergunta em 5 segundos...')
        sleep(5)
        print('\033[1;34m(3) Qual a unidade que mede a intensidade do som?')
        sleep(0.5)
        print('')
        print('\033[1;33m(A) Compasso')
        sleep(0.5)
        print('')
        print('\033[1;33m(B) Frequência')
        sleep(0.5)
        print('')
        print('\033[1;33m(C) Hertz')
        sleep(0.5)
        print('')
        print('\033[1;33m(D) Decibel')
        sleep(0.5)
        print('')
        print('\033[1;33m(E) Ruído')
        sleep(1)
        print('')
        respq3 = str(input('\033[1;31mSua Resposta >> ')).strip().lower()
        print('\033[1;33mProcessando...')
        sleep(3)
        if respq3 == 'd':
            print('\033[1;32m✔ Resposta Correta! +1 ponto :)')
        else:
            print('\033[1;31mX Resposta Incorreta! 0 pontos :(')
            cont -= 1
        sleep(1)
        print("""\033[1;36mEm todo o mundo, os decibéis são usados para 
        medir o nível do som, o que é feito mediante uma escala logarítmica.""")
        sleep(5)
        print('\033[1;33mPróxima pergunta em 5 segundos...')
        sleep(5)
        print('\033[1;34m(4) De onde vem o chuveiro elétrico?')
        sleep(0.5)
        print('')
        print('\033[1;33m(A) França')
        sleep(0.5)
        print('')
        print('\033[1;33m(B) Inglaterra')
        sleep(0.5)
        print('')
        print('\033[1;33m(C) Brasil')
        sleep(0.5)
        print('')
        print('\033[1;33m(D) Austrália')
        sleep(0.5)
        print('')
        print('\033[1;33m(E) Itália')
        sleep(1)
        print('')
        respq4 = str(input('\033[1;31mSua Resposta >> ')).strip().lower()
        print('\033[1;33mProcessando...')
        sleep(3)
        if respq4 == 'c':
            print('\033[1;32m✔ Resposta Correta! +1 ponto :)')
        else:
            print('\033[1;31mX Resposta Incorreta! 0 pontos :(')
            cont -= 1
        sleep(1)
        print("""\033[1;36mVeio do Brasil! Francisco Canhos é o nome do homem 
        que, na década de 40 desenvolveu o primeiro chuveiro elétrico
        seguro em Jaú-SP. O aparelho vinha sendo desenvolvido desde os
        anos 30 mas apresentava riscos de curto-circuito.""")
        sleep(5)
        print('\033[1;33mPróxima pergunta em 5 segundos...')
        sleep(5)
        print('\033[1;34m(5) Em que período da pré-história o fogo foi descoberto?')
        sleep(0.5)
        print('')
        print('\033[1;33m(A) Neolítico')
        sleep(0.5)
        print('')
        print('\033[1;33m(B) Paleolítico')
        sleep(0.5)
        print('')
        print('\033[1;33m(C) Idade dos Metais')
        sleep(0.5)
        print('')
        print('\033[1;33m(D) Período da pedra polida')
        sleep(0.5)
        print('')
        print('\033[1;33m(E) Idade Média')
        sleep(1)
        print('')
        respq5 = str(input('\033[1;31mSua Resposta >> ')).strip().lower()
        print('\033[1;33mProcessando...')
        sleep(3)
        if respq5 == 'b':
            print('\033[1;32m✔ Resposta Correta! +1 ponto :)')
        else:
            print('\033[1;31mX Resposta Incorreta! 0 pontos :(')
            cont -= 1
        sleep(1)
        print("""\033[1;36mFoi no Paleolítico que o fogo começou a ser
        utilizado quando os homens aprenderam que era
        possível obter fogo por meio do atrito de pedaços de madeira e pedra.""")
        sleep(5)
        print('\033[1;33mPróxima pergunta em 5 segundos...')
        sleep(5)
        print('\033[1;34m(6) Qual foi o recurso utilizado inicialmente pelo homem para explicar a origem das coisas?')
        sleep(0.5)
        print('')
        print('\033[1;33m(A) Filosofia')
        sleep(0.5)
        print('')
        print('\033[1;33m(B) Biologia')
        sleep(0.5)
        print('')
        print('\033[1;33m(C) Matemática')
        sleep(0.5)
        print('')
        print('\033[1;33m(D) Astronomia')
        sleep(0.5)
        print('')
        print('\033[1;33m(E) Mitologia')
        sleep(1)
        print('')
        respq6 = str(input('\033[1;31mSua Resposta >> ')).strip().lower()
        print('\033[1;33mProcessando...')
        sleep(3)
        if respq6 == 'e':
            print('\033[1;32m✔ Resposta Correta! +1 ponto :)')
        else:
            print('\033[1;31mX Resposta Incorreta! 0 pontos :(')
            cont -= 1
        sleep(1)
        print("""\033[1;36mA mitologia é um sistema de crenças que inclui uma série de narrativas e lendas, as quais 
        fizeram parte do imaginário coletivo de diversas civilizações antigas. 
        Dessa forma, no começo do desenvolvimento da humanidade, diversos povos utilizaram a mitologia para explicar 
        alguns fenômenos e a origem das coisas.""")
        sleep(5)
        print('\033[1;33mPróxima pergunta em 5 segundos...')
        sleep(5)
        print('\033[1;34m(7) Quem foi o primeiro homem a pisar na Lua? Em que ano aconteceu?')
        sleep(0.5)
        print('')
        print('\033[1;33m(A) Yuri Gagarin, em 1961')
        sleep(0.5)
        print('')
        print('\033[1;33m(B) Buzz Aldrin, em 1969')
        sleep(0.5)
        print('')
        print('\033[1;33m(C) Charles Conrad, em 1969')
        sleep(0.5)
        print('')
        print('\033[1;33m(D) Neil Armstrong, em 1969')
        sleep(0.5)
        print('')
        print('\033[1;33m(E) Charles Duke, em 1971')
        sleep(1)
        print('')
        respq7 = str(input('\033[1;31mSua Resposta >> ')).strip().lower()
        print('\033[1;33mProcessando...')
        sleep(3)
        if respq7 == 'd':
            print('\033[1;32m✔ Resposta Correta! +1 ponto :)')
        else:
            print('\033[1;31mX Resposta Incorreta! 0 pontos :(')
            cont -= 1
        sleep(1)
        print("""\033[1;36mNeil Armstrong (1930-2012) foi um engenheiro e astronauta, sendo o primeiro homem a pisar
        na lua em 1969 na missão Apollo 11, ao lado dos astronautas: Michael Collins e Edwin "Buzz" Aldrian.""")
        sleep(5)
        print('\033[1;33mPróxima pergunta em 5 segundos...')
        sleep(5)
        print('\033[1;34m(8) Em que oceano fica Madagascar?')
        sleep(0.5)
        print('')
        print('\033[1;33m(A) Oceano Índico')
        sleep(0.5)
        print('')
        print('\033[1;33m(B) Oceano Antártico')
        sleep(0.5)
        print('')
        print('\033[1;33m(C) Oceano Atlântico')
        sleep(0.5)
        print('')
        print('\033[1;33m(D) Oceano Pacífico')
        sleep(0.5)
        print('')
        print('\033[1;33m(E) Oceano Ártico')
        sleep(1)
        print('')
        respq8 = str(input('\033[1;31mSua Resposta >> ')).strip().lower()
        print('\033[1;33mProcessando...')
        sleep(3)
        if respq8 == 'a':
            print('\033[1;32m✔ Resposta Correta! +1 ponto :)')
        else:
            print('\033[1;31mX Resposta Incorreta! 0 pontos :(')
            cont -= 1
        sleep(1)
        print("""\033[1;36mO Madagascar é um país insular banhado pelo Oceano Índico.
        Localizado no sudeste da África sua capital é Antananarivo.""")
        sleep(5)
        print('\033[1;33mPróxima pergunta em 5 segundos...')
        sleep(5)
        print('\033[1;34m(9) Qual o metal cujo símbolo químico é o Au?')
        sleep(0.5)
        print('')
        print('\033[1;33m(A) Cobre')
        sleep(0.5)
        print('')
        print('\033[1;33m(B) Prata')
        sleep(0.5)
        print('')
        print('\033[1;33m(C) Mercúrio')
        sleep(0.5)
        print('')
        print('\033[1;33m(D) Ouro')
        sleep(0.5)
        print('')
        print('\033[1;33m(E) Manganês')
        sleep(1)
        print('')
        respq9 = str(input('\033[1;31mSua Resposta >> ')).strip().lower()
        print('\033[1;33mProcessando...')
        sleep(3)
        if respq9 == 'd':
            print('\033[1;32m✔ Resposta Correta! +1 ponto :)')
        else:
            print('\033[1;31mX Resposta Incorreta! 0 pontos :(')
            cont -= 1
        sleep(1)
        print("""\033[1;36mO ouro é um metal de transição presente\nna 
        tabela periódica, sendo representado\npelo símbolo Au.""")
        sleep(5)
        print('\033[1;33mPróxima pergunta em 5 segundos...')
        sleep(5)
        print('\033[1;34m(10) (Última Pergunta) Em que século o continente europeu foi devastado pela peste bubônica?')
        sleep(0.5)
        print('')
        print('\033[1;33m(A) No século X')
        sleep(0.5)
        print('')
        print('\033[1;33m(B) No século XI')
        sleep(0.5)
        print('')
        print('\033[1;33m(C) No século XII')
        sleep(0.5)
        print('')
        print('\033[1;33m(D) No século XIII')
        sleep(0.5)
        print('')
        print('\033[1;33m(E) No século XIV')
        sleep(1)
        print('')
        respq10 = str(input('\033[1;31mSua Resposta >> ')).strip().lower()
        print('\033[1;33mProcessando...')
        sleep(3)
        if respq10 == 'e':
            print('\033[1;32m✔ Resposta Correta! +1 ponto :)')
        else:
            print('\033[1;31mX Resposta Incorreta! 0 pontos :(')
            cont -= 1
        sleep(1)
        print("""\033[1;36mA peste bubônica, também chamada de peste negra, atingiu a 
        população europeia no século XIV, sendo que o auge da epidemia ocorreu entre os anos de 1347 e 1353. Estima-se 
        que ⅓ da população morreu afetada por essa doença pulmonar, ou seja,cerca de 25 milhões de pessoas.""")
        sleep(5)
        print("\n\033[1;34mO seu Resultado foi:", end=' ')
        if cont <= 3:
            print('\033[1;31mDecepcionante :(')
        elif cont <= 6:
            print('\033[1;33mMeeeeh, Mais ou menos :0')
        elif cont <= 8:
            print('\033[1;35mMuito bem!, quase lá :>')
        elif cont <= 10:
            print('\033[1;32mPerfeito!!! :) :) :)')
    else:
        print('\033[1;33mResposta Inválida!')
    conti = str(input('\033[1;39mQuer Continuar? [\033[1;32mS\033[1;39m/\033[1;31mN\033[1;39m]: ')).strip().upper()[0]
    if conti == 'N':
        print('\033[1;31mFechando...')
        sleep(1)
        break
    else:
        print('\033[1;33mReiniciando...')
        sleep(3)
