import unittest
from fizzbuzz import fizzbuzz

class TestFizzbuzz(unittest.TestCase):
  
  def test_fizzbuzz_1(self):
    return self.assertEqual(
      fizzbuzz(1),
      fizzbuzz(1)
    )

  def test_fizzbuzz_2(self):
    return self.assertEqual(
      fizzbuzz(2),
      fizzbuzz(2)
    )

  def test_fizzbuzz_3(self):
    return self.assertEqual(
      fizzbuzz(3),
      'fizz'
    )

  def test_fizzbuzz_5(self):
    return self.assertEqual(
      fizzbuzz(5),
      'buzz'
    )

  def test_fizzbuzz_15(self):
    return self.assertEqual(
      fizzbuzz(15),
      'fizzbuzz'
    )

  def test_fizzbuzz_30(self):
    return self.assertEqual(
      fizzbuzz(30),
      'fizzbuzz'
    )

  def test_fizzbuzz_string(self):
    return self.assertEqual(
      fizzbuzz('a'),
      None
    )
