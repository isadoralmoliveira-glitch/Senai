print("=== Sistema de Cálculo de Fator de Risco ===\n")

pressao = float(input("Digite a pressão da caldeira: "))
temperatura = float(input("Digite a temperatura da caldeira: "))
ciclos = int(input("Digite a quantidade de ciclos de trabalho: "))

if ciclos < 200:
    reducao = 0
    nivel = "Operação Leve"
elif ciclos >= 200 and ciclos <= 999:
    reducao = 0.05
    nivel = "Operação Moderada"
elif ciclos >= 1000 and ciclos <= 1999:
    reducao = 0.10
    nivel = "Operação Intensiva"
else:
    reducao = 0.15
    nivel = "Operação Crítica"

fator_risco = pressao * temperatura
fator_final = fator_risco * (1 - reducao)

print("\n=== RESULTADO ===")
print(f"Nível de operação: {nivel}")
print(f"Fator de risco bruto: {fator_risco:.2f}")
print(f"Redução aplicada: {reducao * 100}%")
print(f"Fator de risco final: {fator_final:.2f}")