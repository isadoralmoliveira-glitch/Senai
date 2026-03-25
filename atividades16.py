print("=== Bem-vindo ao Sistema de Qualidade ===")
nome = input("Digite o nome do aluno: ")
print(f"\nOlá, {nome}! Vamos analisar os sensores.\n")

soma_calibrada = 0


for i in range(1, 6):
    print(f"\n--- Sensor {i} ---")
    
    leitura = float(input("Digite o valor da leitura: "))
    horas = int(input("Digite as horas de uso: "))
    
    if horas < 200:
        ajuste = 0
        nivel = "Sem ajuste"
    elif horas >= 200 and horas <= 999:
        ajuste = 0.05
        nivel = "Ajuste leve (5%)"
    elif horas >= 1000 and horas <= 1999:
        ajuste = 0.10
        nivel = "Ajuste médio (10%)"
    else:
        ajuste = 0.15
        nivel = "Ajuste alto (15%)"
    
    leitura_calibrada = leitura * (1 - ajuste)
    
   
    soma_calibrada += leitura_calibrada
    
    # Exibição
    print(f"Leitura bruta: {leitura:.2f}")
    print(f"Tipo de ajuste: {nivel}")
    print(f"Leitura calibrada: {leitura_calibrada:.2f}")

media = soma_calibrada / 5

print("\n=== RESULTADO FINAL ===")
print(f"Média das leituras calibradas: {media:.2f}")