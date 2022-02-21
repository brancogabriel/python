digitadas = []
print()

palavra_secreta = input('Você está no Jogo da Forca. Digite qual será a palavra secreta: ')
vidas = input('Digite o número de vidas que o usuário terá: ')

vidas = int(vidas)
    
print('O desafio vai iniciar.')
print()

while True:
    if vidas < 0:
        print('Você perdeu.')
        break

    letra = input('Digite uma letra: ')
    
    if len(letra) > 1:
        print('Ah, isso não vale! Digite somente uma letra.')
        continue
    
    digitadas.append(letra) # adiciona letra à lista 'digitadas'
    
    if letra in palavra_secreta:
        print(f'Parabéns! A letra {letra} existe na palavra secreta!')
    else:
        print(f'Putz! Você errou.')
        digitadas.pop
        
    secreta_temporaria = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in digitadas:
            secreta_temporaria += letra_secreta
        else:
            secreta_temporaria += '*'
    
    if secreta_temporaria == palavra_secreta:
        print(f'Parabéns! Você ganhou! A palavra era {palavra_secreta}.')
        break
    else:
        print(f'A palavra secreta está assim: {secreta_temporaria}')
        
    if letra not in palavra_secreta:
        vidas -= 1
        print(f'Você perdeu uma vida. Restam {vidas} vidas.')

    
    
    