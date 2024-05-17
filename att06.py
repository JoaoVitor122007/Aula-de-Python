ano = int(input("Digite o ano: "))

if ano % 4 == 0 and ano % 100:
  print("O ano é bissexto")
else:
  print("O ano não é bissexto")
