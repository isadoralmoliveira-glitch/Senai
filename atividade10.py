soma = 0
acima_15 = 0
acima_20 = 0
acima_200 = 0
sobrecarga = False
alerta = False
for i in range (8):
    corrente = float(input(f"digite a {i+1}medição de corrente(A):"))
    soma += corrente 

    if corrente > 15:
       acima_15 += 1
    if corrente > 20:
      sobrecarga = True
      acima_20 += 1
    if corrente > 200:
      alerta = True
      acima_200 += 1
media = soma/8
print("medições acima de 15 (A)", acima_15)
print ("media da corrente:", media)
if sobrecarga:
   print (f"houve sobre carga no motor{acima_20} vezes")
if alerta:
   print (f"alerta:medição ultrapassou 200 (A){acima_200}")

