

def morral(tamagno_morral, pesos, valores, n):
    if n == 0 or tamagno_morral == 0:
        return 0
    if pesos[n -1] > tamagno_morral:
        return (tamagno_morral, pesos, valores, n -1)
    return max(valores[n -1] + morral(tamagno_morral - pesos[n - 1], pesos, valores, n -1),
                morral(tamagno_morral, pesos, valores, n - 1))

if __name__ == "__main__":
    valores = [160, 100, 120]
    pesos = [10, 20, 30]
    tamagno_morral = 50
    n = len(valores)

    resultado = morral(tamagno_morral, pesos, valores, n)
    print(resultado)