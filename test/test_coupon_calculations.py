import unittest
from store import coupon_calculations as coupon


class MyTestCase(unittest.TestCase):
    def test_price_under_ten(self):
        self.assertAlmostEqual(6.84, coupon.calculate_price(5.99, 5, 15), 2)
        self.assertAlmostEqual(5.64, coupon.calculate_price(4.68, 5, 10), 2)
        self.assertAlmostEqual(8.49, coupon.calculate_price(7.99, 5, 20), 2)
        self.assertAlmostEqual(1.65, coupon.calculate_price(5.23, 10, 15), 2)
        self.assertAlmostEqual(0.19, coupon.calculate_price(3.96, 10, 10), 2)
        self.assertAlmostEqual(2.75, coupon.calculate_price(6.23, 10, 20), 2)

    def test_price_under_between_ten_thirty(self):
        self.assertAlmostEqual(6.84, coupon.calculate_price(12.54, 5, 15), 2)
        self.assertAlmostEqual(5.64, coupon.calculate_price(14.23, 5, 10), 2)
        self.assertAlmostEqual(8.49, coupon.calculate_price(16.89, 5, 20), 2)
        self.assertAlmostEqual(1.65, coupon.calculate_price(22.45, 10, 15), 2)
        self.assertAlmostEqual(0.19, coupon.calculate_price(26.84, 10, 10), 2)
        self.assertAlmostEqual(2.75, coupon.calculate_price(28.22, 10, 20), 2)


if __name__ == '__main__':
    unittest.main()
