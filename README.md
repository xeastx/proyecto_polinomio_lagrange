# Proyecto Polinomio de Lagrange.

### Cada participante debe completar su módulo y luego solicitar el Pull-Request (PR).

A cada participante se le presenta un módulo en lenguaje *Python* con la siguiente estructura:

```python
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
        pass

    return polinomio


if __name__ == '__main__':
    # Pruebe aquí su Polinomio de Lagrange ...

    pass
```
## Requerimientos.

1. El participante deberá completar en su módulo la función `polinomio_lagrange(X, Y)`.
2. La función `polinomio_lagrange(X, Y)` **deberá retornar una función**, el *Polinomio de Lagrange* dadas las listas `X` e `Y` pasadas por parámetro.
3. El participante deberá probar su función `polinomio_lagrange(X, Y)` en la sección `main` del código.

## Notas.

**NOTA 1**: Cualquier duda o pregunta sobre este proyecto, por favor abra un [**issue**](https://github.com/ejdecena/proyecto_polinomio_lagrange/issues).

**NOTA 2**: Solo se recibirá UNA y solo una petición de PR por participante.

**NOTA 3**: Marque con **Watch** este repositorio para que reciba todas las notificaciones.

**NOTA 4**: Recuerde que hay un [**Tutorial Git**](https://github.com/ejdecena/tutorial_git) y un [**Tutorial Python**](https://github.com/ejdecena/tutorial_python) que pueden ser útiles en caso de cualquier duda.

**NOTA 5**: Se recibirán solicitudes de PR hasta el día **jueves 21 de noviembre de 2019, 11:59 pm**, SIN PRÓRROGA.