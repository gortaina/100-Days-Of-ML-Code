# -*- condig: utf-8 -*-

# Jogo da Forca
# Programação Orientada a Objetos

import random

# tabuleiro
tabuleiro = ['''

"***************** JOGO DA FORCA "*****************

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Forca:

    # Método Construtor
    def __init__(self, word):
        self.max_tentativas = len(tabuleiro)
        self.word = word
        self.word_guess = []
        self.right_letter = []
        self.wrong_letter = []

    # Método para adivinhar a letra
    def guess(self, letter):
        self.word_guess = list(map(lambda x: x if (x in letter) else "-", self.word))
        # Faz a verificação se a letra eEvita a adição de letras repetidas
        if(letter in self.word and letter not in self.right_letter):
            self.right_letter.append(letter)
            return True
        elif(letter not in self.word and letter not in self.wrong_letter):
            self.wrong_letter.append(letter)
            return False
        else:
            return False

    # Método para verificar se o jogo terminou
    # Se o jogador repetir uma letra correta, o nº de tentativas permanece
    def hangman_over(self):
        if(len(self.wrong_letter) > 5):
            return False
        elif(self.hangman_won()):
            return False
        else:
            return True

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        if(self.word == self.word_guess):
            return True
        else:
            return False

    # Método para não mostrar a letra no board
    def hide_word(self):
        self.word_guess = list(map(lambda x: x if( x in self.right_letter) else "-", self.word))
        self.word_guess = ''.join(self.word_guess)
        return self.word_guess

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        print(tabuleiro[len(self.wrong_letter)])
        print("\nPalavra: ", self.hide_word())
        # O join retira as chaves e separa as letras por vírgula
        print("\nLetras erradas:  ", ', '.join(self.wrong_letter))
        print("\nLetras corretas: ", ', '.join(self.right_letter))


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
        with open("palavras.txt", "rt") as f:
                bank = f.readlines()
        return bank[random.randint(0,len(bank))].strip()


# Função Main - Execução do Programa
def main():
    # Objeto
    game = Forca(rand_word())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    game.print_game_status()
    while(game.hangman_over()):
        letra = input("\nDigite uma letra: ")
        game.guess(letra)

        # Verifica o status do jogo
        game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()
