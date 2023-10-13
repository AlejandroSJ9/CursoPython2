try:
  age = 10
  if age < 18:
    raise Exception('No se pemiten menores')
    #tipo de error que nos puede salir
# si no coge el error pues no se ejecuta lo siguiente
except Exception as error:
  print(error)

try:
  print(0/0)
  #exepcion es mas general
except Exception as error:
  print(error)
print('hola')