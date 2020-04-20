"""
"abacabad" c
"abacabaabacaba" _
"abcdefghijklmnopqrstuvwxyziflskecznslkjfabe" d
"bcccccccccccccyb" y
"""

def first_not_repeating_char(char_sequence):
    seen_letters = {}

    for idx, letter in enumerate(char_sequence):
        if letter not in seen_letters: # si el caracter aparece una sola vez
            seen_letters[letter] = (idx, 1)
        else:
            seen_letters[letter] = (seen_letters[letter][0], seen_letters[letter][1] + 1) # almacena en un a tubla el indice donde la vio por primera vez y las veces que aparece
    
    # Obetener las letras que no se repiten junto a su idice y gardarlos en un alista como tuplas
    final_letters = []
    for key, value in seen_letters.items():
        if value[1] == 1:
            final_letters.append((key, value[0]))

    # Ordenar la lista de letras sin repetir
    not_repeated_letters = sorted(final_letters, key =lambda value: value [1])

    if not_repeated_letters:
        return not_repeated_letters [0][0]
    else:
        return '_'

if __name__ == '__main__':
    char_sequence = str(input('Escribe una secuencia de caracteres: '))

    result = first_not_repeating_char(char_sequence)

    if result == '_':
        print('Todos los caracteres se repiten.')
    else:
        print('El primer caracter no repetido es: {}'.format(result))