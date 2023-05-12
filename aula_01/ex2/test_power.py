import unittest
from power import power

class TestPower(unittest.TestCase):
  def test_power_1(self):
    return self.assertEqual(
      power(1, 1),
      1
    )

  def test_power_2(self):
    return self.assertEqual(
      power(2, 4),
      16
    )

  def test_power_3(self):
    return self.assertEqual(
      power(2, 5),
      32
    )

  def test_power_4(self):
    return self.assertEqual(
      power(4, 2),
      16
    )

  def test_power_0(self):
    return self.assertEqual(
      power(1, 0),
      1
    )

  def test_power_power1(self):
    return self.assertEqual(
      power(7, 1),
      7
    )