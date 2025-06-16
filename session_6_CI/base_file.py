#a = 5
#b = 10


def add(x, y):
	"""Add two numbers."""
	return x + y

def subtract(x, y):
	"""Subtract two numbers."""
	return x - y

def multiply(x, y):
	"""Multiply two numbers."""
	return x * y

def divide(x, y):
	"""Divide two numbers."""
	if y == 0:
		raise ValueError("Cannot divide by zero.")
	return x / y

#print("This is the base file being executed, outside of the main block.")

if __name__ == "__main__":
	# This block will only run if this file is executed directly
	# It won't run if this file is imported as a module in another file
	print("This is the base file being executed directly.")

	print(f"a: {a}, b: {b}, sum: {a + b}, coming from base_file.py")