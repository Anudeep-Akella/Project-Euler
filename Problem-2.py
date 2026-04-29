def even_fibonacci_sum(number):
    """Finds the fibonacci numbers and sums the even numbers from the fibonacci series upto the given number.""" 
    even_sum = 0
    first_digit,second_digit = 1,2 # The first two digits of the fibonacci series are 1 and 2 respectively.
    print(first_digit)
    print(second_digit)

    for i in range(number-2):   # Loop continues until the second digit is less than or equal to the given number.
        if second_digit % 2 == 0:
            even_sum += second_digit
        first_digit,second_digit = second_digit,first_digit + second_digit # The Fibonacci condition is satisfied in this line
        print(second_digit)

    return even_sum

def main():
    try:
        n = int(input('The range upto which the sum of even fibonacci numbers are to be calculated: ')) # Takes input from the user
    except ValueError:
        print("INVALID INPUT! Please enter a valid number.") # Raises value error if the input is not a valid number
        return

    print('Sum of even numbers in fibonacci series: ',even_fibonacci_sum(n))
    
if __name__ == "__main__":
    main()