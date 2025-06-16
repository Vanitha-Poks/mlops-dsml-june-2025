from base_file import a, b, add, subtract, multiply, divide


print(f"a: {a}, b: {b}, sum: {a + b}")


print(f"add: {add(a, b)}")
print(f"subtract: {subtract(a, b)}")
print(f"multiply: {multiply(a, b)}")
try:
	print(f"divide: {divide(a, b)}")	
except ValueError as e:
	print(f"Error: {e}")
