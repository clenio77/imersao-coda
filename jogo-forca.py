import random
import streamlit as st 


def get_word():
    lista_palavras = ['gata', 'cão', 'lagarto', 'centopéia', 'boi']
    word = random.choice(lista_palavras)
    return word.upper()


def play(word):
    word_completion = "_" * len(word) 
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    st.title('Jogo da Forca!')
    st.write('JOGO DA FORCA! \n Dica: {} letras!'.format(len(word)))
    #print(f"JOGO DA FORCA!\nDica: {len(word)} letras!")
    st.write(display_hangman(tries))
    #print(display_hangman(tries))
    st.write(word_completion)
    #print(word_completion)
    #st.write('\n')
    print("\n")
    
    while not guessed and tries > 0:
        guess = st.text_input('Adivinhe uma letra ou palavra: ').upper()
        #guess = input("Adivinhe uma letra ou palavra: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                st.write('Voce já tentou ', guess)
                #print("Você já tentou ", guess)
            elif guess not in word:
                st.write(guess, 'Não.')
                #print(guess, "Não.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                st.write(guess, 'está na palavra!')
                #print(guess, "está na palavra!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                st.write('Você já tentou a palavra', guess)
                #print("Você já tentou a palavra", guess)
            elif guess != word:
                st.write(guess, 'não é a palavra.')
                print(guess, "não é a palavra.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Inválido.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Parabéns, você adivinhou a palavra! Você venceu!")
    else:
        print("Você perdeu!. A palavra era " + word + ".")
        
        

def display_hangman(tries):
    stages = [  # cabeça, tronco e braços e pernas: morte.
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \
                   -
                """,
                # cabeça, tronco e braços, perna
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                """,
                # cabeça, tronco e braços
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                """,
                # cabeça, tronco e braço
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                """,
                # cabeça e tronco
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # cabeça
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # vazio
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]        


#@st.cache
def main():
    word = get_word()
    play(word)
    while input("Jogar de novo? (S/N) ").upper() == "S":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()