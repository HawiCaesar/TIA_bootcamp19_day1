"""
Generate prime numbers from 0 to n with asymtotic analysis

An assumption with this analysis is that each time their is an iteration, a constant time taken is presumed
Say there will be 20 iterations, 20 units of time will be executed

Worst case scenario for nested loops is O(N^2) meaning the performance of this algotrithm is 
directly propotional to the square of the input

"""

def generate_prime_numbers_asymptotic(last_number):
	
	prime_number_list = []

	if isinstance(last_number, int):
		if last_number < 0:
			raise ValueError("Only postive integers are allowed")

		elif last_number < 2:
			return "Numbers below 2 are not prime numbers"

		else:

			for number in range(2, last_number + 1):
				for i in range(2, number):

					## If not a prime number
					if number%i == 0:
						break
				## All others are prime
				else:
					prime_number_list.append(number)

	else:
		raise TypeError("Please enter Integers only. Strings/Characters are not allowed with this function.")


	return prime_number_list



print(generate_prime_numbers_asymptotic(20))


