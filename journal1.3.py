import numpy as np   # import numpy as np

def f(x):
	return x**3+8

def main():     #define main program
	x=9
	result = f(x)
	print(f"f({x}) is: {result}")

	if result>27:
		print("YAY!")

#if the main() function exists, run it
if __name__ == "__main__":
	main()

#you can add other instructions below
#will be executed after the main() program