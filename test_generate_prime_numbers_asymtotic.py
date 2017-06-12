import unittest
from generate_prime_numbers import generate_prime_numbers_asymptotic

class TestPrimeNumberGeneration(unittest.TestCase):

	def test_one_is_not_prime_number(self):
		
		self.assertEqual(generate_prime_numbers_asymptotic(1), 1, "1 is not a prime number")
