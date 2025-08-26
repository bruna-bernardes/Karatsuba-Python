def karatsuba(x: int, y: int) -> int:
    """
    Implementação do algoritmo de Karatsuba para multiplicação de dois inteiros.
    """

    if x == 0 or y == 0:
        return 0
    sinal = -1 if (x < 0) ^ (y < 0) else 1
    x_abs, y_abs = abs(x), abs(y)

    if x_abs < 10 or y_abs < 10:
        return sinal * (x_abs * y_abs)

    num_digitos = max(len(str(x_abs)), len(str(y_abs)))
    metade = num_digitos // 2

    x_alta, x_baixa = divmod(x_abs, 10 ** metade)
    y_alta, y_baixa = divmod(y_abs, 10 ** metade)

    produto_baixas = karatsuba(x_baixa, y_baixa)                           
    produto_somas  = karatsuba((x_baixa + x_alta), (y_baixa + y_alta))     
    produto_altas  = karatsuba(x_alta, y_alta)                             

    resultado_abs = (
        (produto_altas * (10 ** (2 * metade))) +
        ((produto_somas - produto_altas - produto_baixas) * (10 ** metade)) +
        produto_baixas
    )
    return sinal * resultado_abs


if __name__ == "__main__":
    try:
        a = int(input("\nDigite o primeiro número inteiro: ").strip())
        b = int(input("\nDigite o segundo número inteiro: ").strip())
    except ValueError:
        print("Entrada inválida. Por favor, digite apenas inteiros (ex.: 123456).")
        raise SystemExit(1)

    resultado = karatsuba(a, b)
    print(f"\nResultado da multiplicação (Karatsuba):\n{a} * {b} = {resultado}")