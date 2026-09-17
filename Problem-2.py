# Problem Sum of Even Valued Terms in Fibonacci series less than 4 million. Where the series start from 1 and 2. 

def even_fibonacci_sum(limit: int) -> int:
    """Return the sum of even Fibonacci numbers below the given limit."""

    first_digit, second_digit = 1, 2
    even_sum = 0

    while second_digit < limit:
        if second_digit % 2 == 0:
            even_sum += second_digit
        first_digit, second_digit = second_digit, first_digit + second_digit

    return even_sum

def main():
    while True:
        try:
            n = input('The range upto which the sum of even fibonacci numbers are to be calculated:') # Takes input from the user
            if int(n) <= 0:
                print("Please Enter Positive Number!")
                continue
            if int(n) == 1:
                print("The first fibonacci Number: 1")
                break
            if int(n) == 2:
                print("The Second Fibonacci Number: 2")
                break
            print('\nSum of even numbers in fibonacci series: ',even_fibonacci_sum(int(n)))
            break
        except ValueError:
            print("INVALID INPUT! Please enter a valid number.") # Raises value error if the input is not a valid number

    
if __name__ == "__main__":
    main()