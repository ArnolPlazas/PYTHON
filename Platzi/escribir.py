

def run():
    with open('numeros.txt', 'w') as f: # manejador de contexto (context manager) cierra el archivo
        for i in range(10):
            f.write(str(i))


if __name__ == "__main__":
    run()