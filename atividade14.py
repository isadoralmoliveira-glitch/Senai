import time

tempo = 10

print("Iniciando resfriamento\n")

for i in range(tempo, -1, -1):
    print(f"Tempo restante: {i} segundos")
    time.sleep(1)  

print("\nResfriamento concluído! Pode abrir a prensa.")