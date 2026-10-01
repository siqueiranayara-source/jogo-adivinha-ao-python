numero_secreto = 27

print("Tente adivinhar o número secreto! Você tem 5 tentativas.")

for tentativa in range(1, 6):
    palpite = int(input(f"Tentativa {tentativa}/5 - Digite seu palpite: "))

    if palpite == numero_secreto:
        print("Parabéns! Você acertou!")
        break
    elif palpite > numero_secreto:
        print("Dica: O número secreto é MENOR.")
    else:
        print("Dica: O número secreto é MAIOR.")

    if tentativa == 5:
        print(f"Você perdeu! O número correto era {numero_secreto}.")
