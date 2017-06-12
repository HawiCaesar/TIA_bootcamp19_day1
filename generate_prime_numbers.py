def generate_prime_numbers_asymptotic(last_number):
	prime_number_list = []

	if(last_number == 1):
		return 1
	else:

		for number in range(2, last_number + 1):

			if last_number % number != 0:
				

