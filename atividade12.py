soma = 0

for i in range(5):
    salario = float(input(f"Digite o salário do funcionário {i+1}: "))
    soma += salario

media = soma / 5

print(f"A média dos salários é: R$ {media:.2f}")