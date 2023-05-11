import unittest
from emp import Empregado

class TestEmpregado(unittest.TestCase):

  def test_reajuste_salario_1(self):
    emp = Empregado('rodrigo', 'maganha', 'presidente', 1500)

    return self.assertEqual(
      emp.calcular_reajuste(),
      emp.salario + (emp.salario * 1.05)
    )

  def test_reajuste_salario_2(self):
    emp = Empregado('rodrigo', 'maganha', 'presidente', 2000)

    return self.assertEqual(
      emp.calcular_reajuste(),
      emp.salario + (emp.salario * 1.05)
    )
  
  def test_nome_completo_1(self):
    emp = Empregado('rodrigo', 'maganha', 'presidente', 2000)

    return self.assertEqual(
      emp.gerar_nome_completo(),
      'rodrigo maganha'
    )

  def test_nome_completo_2(self):
    emp = Empregado('felipe', 'gabriel', 'presidente', 2000)

    return self.assertEqual(
      emp.gerar_nome_completo(),
      'felipe gabriel'
    )

  def test_validar_cargo_1(self):
    emp = Empregado('rodrigo', 'maganha', 'presidente', 2000)

    return self.assertEqual(
      emp.validar_cargo(),
      True
    )

  def test_validar_cargo_2(self):
    emp = Empregado('rodrigo', 'maganha', 'faxineiro', 2000)

    return self.assertEqual(
      emp.validar_cargo(),
      False
    )

  def test_validar_cargo_3(self):
    emp = Empregado('rodrigo', 'maganha', 'PRESIDENTE', 2000)

    return self.assertEqual(
      emp.validar_cargo(),
      True
    )
