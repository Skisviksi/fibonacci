def pertence_a_fibonacci(numero):
    # Inicializando os dois primeiros termos da sequência
    a, b = 0, 1
    
    # Verificando se o número pertence à sequência
    while b <= numero:
        if b == numero:
            return True
        a, b = b, a + b
    
    # Se o número não for encontrado na sequência
    return False

# Número a ser verificado na sequência de Fibonacci
numero_verificar = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

# Verificando e exibindo a mensagem
if pertence_a_fibonacci(numero_verificar):
    print(f"{numero_verificar} pertence à sequência de Fibonacci.")
else:
    print(f"{numero_verificar} não pertence à sequência de Fibonacci.")
