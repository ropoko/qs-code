import unittest
from factorial import factorial

class TestFactorial(unittest.TestCase):

  def test_factorial_0(self):
    return self.assertEqual(
      factorial(0),
      0
    )

  def test_factorial_1(self):
    return self.assertEqual(
      factorial(1),
      1
    )

  def test_factorial_2(self):
    return self.assertEqual(
      factorial(5),
      120
    )

  def test_factorial_3(self):
    return self.assertEqual(
      factorial(10),
      3628800
    )

  def test_factorial_string(self):
    return self.assertEqual(
      factorial('n'),
      None
    )

  def test_factorial_4(self):
    return self.assertEqual(
      factorial(6),
      720
    )

  def test_factorial_5(self):
    return self.assertEqual(
    factorial(7),
    5040
  )

  def test_factorial_6(self):
    return self.assertEqual(
      factorial(8),
      40320
    )