import turtle

def main():
    window = turtle.Screen() # Abrir un aventana
    dave = turtle.Turtle() #intanciar Turtle

    make_squere(dave)

    turtle.mainloop() # No cerrar la ventana

def make_squere(dave):
    length = int(input('Tamaño del cuadrado: '))
    
    for i in range(4):
        make_line_and_turn(dave, length)


def make_line_and_turn(dave, length):
    dave.forward(50)
    dave.left(90)

if __name__ == '__main__': # Indicar en donde inicia el programa
    main()
