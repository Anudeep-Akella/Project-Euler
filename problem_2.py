# Problem 2 in Project Euler

# Even Fibonacci numbers

import sys

sys.set_int_max_str_digits( 400000 )

def fibonacci(num):

	next = [1,2]

	for i in range(next[1],num):                  # Creates the fibonacci series until the given number
		next.append( next[-1] + next[-2] )
		
	sum = 0

	for num in next:			      # Checks if the number is even or not
		if num % 2 == 0 :
			sum  += num
			
	return sum				      # Returns the sum of the Even numbers

def main():
	fib = int(input("Enter the range until where the fibonacci series to be written: "))
	print(f" The sum of the even fibonacci series upto given nnumber: {fib} is: {fibonacci(fib)}",end='.\n')
	
	
main()