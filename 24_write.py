with open('./text.txt','w+') as file:
  for i in file:
    print(i)
  file.write('Hola\n')
  file.write('Nueva linea\n')