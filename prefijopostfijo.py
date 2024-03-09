def precedencia_de_operadores(operador):
    if operador == '+' or operador == '-':
        return 1
    elif operador == '*' or operador == '/':
        return 2
    else:
        return 0

def infijo_a_prefijo(expresion):
    operadores = []
    prefijo = []

    for token in reversed(expresion):
        if token.isdigit():
            prefijo.append(token)
        elif token == ')':
            operadores.append(token)
        elif token == '(':
            while operadores[-1] != ')':
                prefijo.append(operadores.pop())
            operadores.pop()
        else:
            while operadores and precedencia_de_operadores(operadores[-1]) > precedencia_de_operadores(token):
                prefijo.append(operadores.pop())
            operadores.append(token)

    while operadores:
        prefijo.append(operadores.pop())

    return ''.join(reversed(prefijo))

def infijo_a_postfijo(expresion):
    operadores = []
    postfijo = []

    for token in expresion:
        if token.isdigit():
            postfijo.append(token)
        elif token == '(':
            operadores.append(token)
        elif token == ')':
            while operadores[-1] != '(':
                postfijo.append(operadores.pop())
            operadores.pop()
        else:
            while operadores and precedencia_de_operadores(operadores[-1]) >= precedencia_de_operadores(token):
                postfijo.append(operadores.pop())
            operadores.append(token)

    while operadores:
        postfijo.append(operadores.pop())
    return ''.join(postfijo)

def main():
    expresion = input("Introduce la expresión aritmética: ")
    print("Expresión en notación prefija:", infijo_a_prefijo(expresion))
    print("Expresión en notación postfija:", infijo_a_postfijo(expresion))

if __name__ == "__main__":
    main()
