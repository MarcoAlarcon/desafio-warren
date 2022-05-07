def reverso(n):
    numReverso = 0

    while n != 0:
        digito = n % 10
        numReverso = numReverso * 10 + digito
        n //= 10

    return numReverso
    
def tratativaVetor(v):
    try:
        while True:
            v.remove(',')
    except ValueError:
        pass