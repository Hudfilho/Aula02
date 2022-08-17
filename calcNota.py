def calculaNota():
  Ap1 = float(input('Informe a nota da Ap1 '))
  Ap2 = float(input('Informe a nota da Ap2 '))
  Ac = float(input('Informe a nota da Ac '))

  media = ((Ap1*4)+(Ap2*4)+(Ac*2))/10

  print('A media do aluno é ', media)
  if media>=7:
    print('Aluno aprovado!')
  else:
    print('Hora de estudar para a AS!')
    As = float(input('Informe a nota da As '))
    if Ap2>=Ap1:
      novamedia = (As*4+Ap2*4+Ac*2)/10
      print(novamedia)
    elif Ap1>=Ap2:
      novamedia =(Ap1*4+As*4+Ac*2)/10
      print(novamedia)
    else:
      print('As muito baixa')
    if novamedia>=7:
      print('Aprovado')
    else:
      print('Reprovado')