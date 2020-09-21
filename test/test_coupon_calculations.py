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
        self.assertAlmostEqual(12.74, coupon.calculate_price(12.54, 5, 15), 2)
        self.assertAlmostEqual(14.76, coupon.calculate_price(14.23, 5, 10), 2)
        self.assertAlmostEqual(16.03, coupon.calculate_price(16.89, 5, 20), 2)
        self.assertAlmostEqual(19.17, coupon.calculate_price(22.45, 10, 15), 2)
        self.assertAlmostEqual(24.02, coupon.calculate_price(26.84, 10, 10), 2)
        self.assertAlmostEqual(23.40, coupon.calculate_price(28.22, 10, 20), 2)

    def test_price_under_between_thirty_fifty(self):
        self.assertAlmostEqual(33.75, coupon.calculate_price(33.64, 5, 15), 2)
        self.assertAlmostEqual(38.32, coupon.calculate_price(36.83, 5, 10), 2)
        self.assertAlmostEqual(35.80, coupon.calculate_price(37.84, 5, 20), 2)
        self.assertAlmostEqual(35.30, coupon.calculate_price(40.35, 10, 15), 2)
        self.assertAlmostEqual(45.57, coupon.calculate_price(45.24, 10, 10), 2)
        self.assertAlmostEqual(45.12, coupon.calculate_price(49.12, 10, 20), 2)

    def test_price_over_including_fifty(self):
        self.assertAlmostEqual(56.68, coupon.calculate_price(54.64, 5, 15), 2)
        self.assertAlmostEqual(62.77, coupon.calculate_price(58.27, 5, 10), 2)
        self.assertAlmostEqual(57.30, coupon.calculate_price(72.57, 5, 20), 2)
        self.assertAlmostEqual(57.31, coupon.calculate_price(60.34, 10, 15), 2)
        self.assertAlmostEqual(69.20, coupon.calculate_price(82.54, 10, 10), 2)
        self.assertAlmostEqual(47.59, coupon.calculate_price(52.03, 10, 20), 2)


if __name__ == '__main__':
    unittest.main()
