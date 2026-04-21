# Funcio que elija palabras aleatoriamente
import random

def get_word(file_name):
    words = []
    with open(file_name, "r") as file:
        for line in file:
            words.append(line.strip())

    length = len(words)
    index = random.randint(0, length -1)
    return words[index]


# Funcion que dibuja al ahorcado
def draw_hangman(errors):
    match(errors):
        case 1:
            hangman =  '''
            |- - - - - - - - -
            |
            |
            |
            |
            |
            |
            |
            |__________________
            '''
        case 2:
            hangman =  '''
            |- - - - - - - - -
            |         |
            |              
            |
            |
            |
            |
            |
            |__________________
            '''
        case 3:
            hangman =  '''
            |- - - - - - - - -
            |         |
            |         O      
            |
            |
            |
            |
            |
            |__________________
            '''
        case 4:
            hangman =  '''
            |- - - - - - - - -
            |         |
            |         O
            |         |
            |
            |
            |
            |
            |__________________
            '''
        case 5:
            hangman =  '''
            |- - - - - - - - -
            |         |
            |         O
            |        /|
            |
            |
            |
            |
            |__________________
            '''
        case 6:
            hangman =  '''
            |- - - - - - - - -
            |         |
            |         O
            |        /|\\
            |
            |
            |
            |
            |__________________
            '''
        case 7:
            hangman =  '''
            |- - - - - - - - -
            |         |
            |         O
            |        /|\\
            |         |
            |
            |
            |
            |__________________
            '''
        case 8:
            hangman =  '''
            |- - - - - - - - -
            |         |
            |         O
            |        /|\\
            |         |
            |        /
            |
            |
            |__________________
            '''
        case 9:
            hangman =  '''
            |- - - - - - - - -
            |         |
            |         O
            |        /|\\
            |         |
            |        / \\
            |
            |
            |__________________
            '''
        case _:
            pass 
    print(hangman)
#funcion game 

#Funcion que regresa guiones en lugar de la plabara 
def get_dashed_word(word,chars=''):
    dashed_word = '-' * len(word)
    for char in chars:
        new_word = ''
        for i in range(len(word)):
            if word[i] == char:
                new_word += char
            else:
                new_word += dashed_word[i]
        dashed_word = new_word 
        
    return dashed_word

def select_category():
    choices_menu = "Elige la categoria para jugar: "
    choices_menu += "\n.1 Comidas: \n.2 Animales: \n.3 Equipos: "
    choice = int(input(choices_menu))
    if choice == 1 :
        word = get_word('comidas.txt')
    elif choice == 2:
        word = get_word('animales.txt')
    elif choice == 3:
        word = get_word('equipos.txt')
    else:
        print('Opción Incorrecta')
        return None
    return word
    
def game():

    
    print('Bienvenido al Juego Ahocado')
    word = select_category()
    if word != None:
        print(get_dashed_word(word))

    chars = ''
    errors = 0
    while True:
        char = input('Ingresa unaletra o una palabra completa: ')
        if (len(char) == 1 and char in word) or char == word:
            chars += char
            dashed_word = get_dashed_word(word, chars)
            print(dashed_word)   
            if dashed_word == word:
                print('Ganaste!')
                break

        else:
            errors += 1
            draw_hangman(errors)
            if errors == 9:
                print('Perdiste!')
                print('La palabra era:', word)
                break

if __name__ == "__main__":
    game()

