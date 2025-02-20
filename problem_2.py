import sys
sys.set_int_max_str_digits(20000)

def fibonacci(number):
    first = 1
    second = 2
    even_sum = 0

    while second < number:
        if second % 2 == 0:
            even_sum += second
        first = second
        second = first + second

    return even_sum



def main():
    num = int(input('Enter the number upto which the fibonacci series are to be calculated: '))
    if num < 0:
        print("Please enter a valid positive number!")
    else:
        print(f'The sum of the even numbers in fibomnacci is {fibonacci(num)}')


main()
