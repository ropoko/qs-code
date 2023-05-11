class Calculadora:
  def somar(x: int, y: int):
    return x + y

  def subtrair(x: int, y: int):
    return x - y

  def multiplicar(x: int, y: int):
    return x * y
    
  def divisao(x: int, y: int):
    if y == 0:
      return 0

    return x / y
