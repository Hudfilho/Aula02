def calculaIMC():
  peso = float(input('Informe o seu peso '))
  altura = float(input('Informe sua altura '))
  imc = peso/ (altura*altura)
  if imc>=30:
    print(imc, 'Obesidade')
  elif imc>=25:
    print(imc, 'Sobre Peso')
  elif imc>18.5:
    print(imc, 'Peso Ideal')
  else:
    print(imc, 'Abaixo do peso')