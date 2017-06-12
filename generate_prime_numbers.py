"""
Generate prime numbers from 0 to n with asymtotic analysis

"""

def generate_prime_numbers_asymptotic(last_number):
	prime_number_list = []

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


		return prime_number_list



print(generate_prime_numbers_asymptotic(20))


