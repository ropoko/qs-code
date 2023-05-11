import unittest
from double import double

class TestDouble(unittest.TestCase):
  def test_double_1(self):
    return self.assertEqual(
      double(1),
      1
    )

  def test_double_2(self):
    return self.assertEqual(
      double(2),
      4
    )

  def test_double_3(self):
    return self.assertEqual(
      double(3),
      9
    )