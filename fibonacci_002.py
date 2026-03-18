def even_fibonacci_sum(number):

    
    even_sum = 0
    


    return even_sum

def main():

    n = int(input('The range upto which the sum of even fibonacci numbers are to be calculated: '))

    if n < 0:
        raise ValueError('INVALID NUMBER!')
    print('Sum of even numbers in fibonacci series: ',even_fibonacci_sum(n))


main()