import unittest
from generate_prime_numbers import generate_prime_numbers_asymptotic

class TestPrimeNumberGeneration(unittest.TestCase):

	def test_one_is_not_prime_number(self):

		self.assertEqual(generate_prime_numbers_asymptotic(1),
		 "Numbers below the number you have entered do not have prime numbers", 
		 "0, 1 are not prime numbers")

	def test_prime_number_result(self):
		self.assertEqual(generate_prime_numbers_asymptotic(10), [2,3,5,7], "prime numbers 0 to 10: 2,3,5,7")
