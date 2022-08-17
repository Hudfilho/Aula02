import math
def calculaRaiz():
  print ('Vamos calcular os coeficientes de uma funcao de segundo grau! ')
  a = float(input('Informe o valor de a = '))
  b = float(input('Informe o valor de b = '))
  c = float(input('Informe o valor de c = '))
  print(a, 'x^2+',b, 'x+', c )
  delta = (b*b -4*a*c)
  x1 = (-b+math.sqrt(delta))/2*a
  x2 = (-b-math.sqrt(delta))/2*a
  print('Raizes: ', x1, x2)