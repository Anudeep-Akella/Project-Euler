# The function that calculates the multiples and returns their sum
def multiples(number):
	
	sum = 0
	for i in range(1,number):            #The logic for multiples of 3 or 5
		if i % 3 == 0 or i % 5 == 0:
			sum += i
	return sum

#This is a main function
def main():
	num = int(input('Enter a valid number upto which the multiples of 3 or 5 to be calculated and to find their sum: '))
	if num < 0:
		raise ValueError('Enter a valid number')
	print('Sum of multiples of 3 or 5 upto ',num,' is: ',multiples(num))  # Here the multiples function is called for calulating the sum
	

main()