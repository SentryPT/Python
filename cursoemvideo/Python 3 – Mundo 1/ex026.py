# programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str (input('Indique uma frase à sua escolha: ')).strip().upper()
print(f"A letra A, aparece {frase.count('A')} vezes na frase. ")
print(f"A primeira vez que a palavra A surge na frase  é na {frase.find('A') + 1}ª posição. ")
print(f"A última vez em que a palavra A surge na frase é na {frase.rfind('A')}ª posição. ")