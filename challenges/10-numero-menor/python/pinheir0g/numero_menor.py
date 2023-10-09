def numero_menor(numero):
    numeros = [int(d) for d in str(numero)]

    if numero > 1:
        reverse = -1
        
        for i in range(len(numeros) - 1):
            if numeros[i] > numeros[i + 1]:
                reverse = i
                break
        if reverse == -1:
            return -1
    
        numeros[reverse + 1:] = reversed(numeros[reverse + 1:])
        numeros[reverse + 1:] = sorted(numeros[reverse + 1:])
        
        numero_novo = int(''.join(map(str, numeros)))

        return numero_novo
    else:
        return None
    

numero = int(input('Digite um número: '))
print(numero_menor(numero))