"""Crie um programa que leia 2 números inteiros positivos, A e B, e que calcule a soma
de todos os números compreendidos entre eles. Os valores A e B não devem ser
considerados no somatório. Caso A seja maior do que B deve ser enviada uma
mensagem para o usuário informando que a soma não será realizada."""

valorA = int(input("Digite o valor do número inicial de intervalo: "))
valorB = int(input("Digite o valor do número final de intervalo: "))
soma = 0

for num in range(valorA + 1, valorB):  # 1 e 5

    if (num % 4) == 0:
        print(f"Número selecionado: {num}")
        soma += num

print(soma)
