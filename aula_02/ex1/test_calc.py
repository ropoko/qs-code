import unittest
from calc import Calculadora

class TestCalculadora(unittest.TestCase):

  # Somar ---------------
  def test_somar_1(self):
    return self.assertEqual(
      Calculadora.somar(2,2),
      4
    )

  def test_somar_3(self):
    return self.assertEqual(
      Calculadora.somar(3,3),
      6
    )

  def test_somar_3(self):
    return self.assertEqual(
      Calculadora.somar(25,30),
      55
    )

  # Subtrair ---------------

  def test_subtrair_1(self):
    return self.assertEqual(
      Calculadora.subtrair(1,1),
      0
    )

  def test_subtrair_2(self):
    return self.assertEqual(
      Calculadora.subtrair(10,5),
      5
  )

  def test_subtrair_3(self):
    return self.assertEqual(
      Calculadora.subtrair(5,6),
      -1
  )

  # Multiplicar ---------------

  def test_multiplicar_1(self):
    return self.assertEqual(
      Calculadora.multiplicar(5,10),
      50
    )

  def test_multiplicar_2(self):
    return self.assertEqual(
      Calculadora.multiplicar(6,6),
      36
    )

  def test_multiplicar_3(self):
    return self.assertEqual(
      Calculadora.multiplicar(2,55),
      110
    )

  # Divisao ---------------

  def test_divisao_1(self):
    return self.assertEqual(
      Calculadora.divisao(5,5),
      1
    )

  def test_divisao_2(self):
    return self.assertEqual(
      Calculadora.divisao(36,6),
      6
    )

  def test_divisao_3(self):
    return self.assertEqual(
      Calculadora.divisao(50,25),
      2
    )  

  def test_divisao_zero(self):
    return self.assertEqual(
      Calculadora.divisao(50,0),
      0
    )
