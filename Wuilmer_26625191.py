#!/usr/bin/env python3
"""
Proyecto Polinomio de Lagrange.

Cada participante debe completar su módulo y luego solicitar el Pull-Request.
"""

def polinomio_lagrange(X, Y):
    """
    Implementa y retorna el Polinomio de Lagrange para las listas X e Y.

    Parámetros:
    X: lista de valores de la variable independiente.
    Y: lista de valores de la variable dependiente.
    """

    if len(X) != len(Y): raise ValueError("Dimensiones diferentes en X e Y.")

    # Ordena el par (x, y) en forma ascendente por x.
    pares = list(zip(X, Y))
    pares.sort(key = lambda x: x[0])
    X, Y  = zip(*pares)
    def polinomio(x):
        L=[]    
        poli=0
        for i in range(len(X)):
            numerador=1
            denominador=1
            for j in range(len(X)):
                if j != i:
                    numerador=numerador*(x-X[j])
                    denominador=denominador*(X[i]-X[j])
            L.append(numerador/denominador)
        for index in range(len(X)):
            poli+=(Y[index]*L[index])
        return poli
    return polinomio


if __name__ == '__main__':
    # Pruebe aquí su Polinomio de Lagrange ...
    X=[-2,0,2,4]
    Y=[1,-1,3,-2]
    polinomio=polinomio_lagrange(X,Y)
    p=polinomio(4)
    print(p)
    pass