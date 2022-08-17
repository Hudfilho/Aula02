def calculaPista():
  larg = float(input('Informe a largura da pista '))
  compri = float(input('Informe o comprimento da pista '))
  area = larg * compri
  dist = float(input('Informe a distancia percorrida pelo veiculo '))

  voltas = dist//area
  print (voltas)