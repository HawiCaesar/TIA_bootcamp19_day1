import unittest
from generate_prime_numbers import generate_prime_numbers_asymptotic

class TestPrimeNumberGeneration(unittest.TestCase):

	# Check if 1 is not a prime number
	def test_one_is_not_prime_number(self):
		self.assertEqual(generate_prime_numbers_asymptotic(1),
		 "Numbers below 2 are not prime numbers", 
		 "1 is not a prime number")

	# Check if a correct result is return of prime numbers from 0 - 10
	def test_prime_number_result(self):
		self.assertEqual(generate_prime_numbers_asymptotic(10), [2,3,5,7], "Prime numbers 0 - 10: [2,3,5,7]")

	# Check if an error is thrown for negative values
	def test_negative_values_in_input_returns_error(self):
		with self.assertRaises(ValueError):
			generate_prime_numbers_asymptotic(-20)

	# Check if error is thrown for non-integer values
	def test_input_must_be_integer(self):
		with self.assertRaises(TypeError):
			generate_prime_numbers_asymptotic("example")

	# Check if list is returned on from prime number generation
	def test_result_returned_is_list(self):
		self.assertIsInstance(generate_prime_numbers_asymptotic(30), list, "Prime numbers must be in a list")


if __name__ == '__main__':
	unittest.main()


