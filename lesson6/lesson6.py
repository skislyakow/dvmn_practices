PASSWORD = input('Введите пароль: ')


def has_digit(PASSWORD):
	return any(symbol.isdigit() for symbol in PASSWORD)


def is_very_long(PASSWORD):
	return len(PASSWORD) > 12


def has_upper_letters(PASSWORD):
	return any(symbol.isupper() for symbol in PASSWORD)


def has_lower_letters(PASSWORD):
	return any(symbol.islower() for symbol in PASSWORD)
	

def has_symbols(PASSWORD):
	return any(not symbol.isalnum() for symbol in PASSWORD 
		if has_lower_letters(PASSWORD) 
			or has_upper_letters(PASSWORD) or PASSWORD)


def main(PASSWORD):

	functions = [
		has_digit,
		is_very_long,
		has_upper_letters,
		has_lower_letters,
		has_symbols,
	]

	score = 0
	for funcion in functions:
		if funcion(PASSWORD):
			score = score + 2
	return score

if __name__ == '__main__':
	print(main(PASSWORD))