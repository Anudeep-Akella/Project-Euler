# Function for finding the multiples of 3 and 5 
def multiples(num):

    sum = 0
    for i in range(1,num):
        if i % 3 == 0 or i % 5 == 0:                           #Adding the multiples of 3 and 5.
            sum += i

    return sum                                                  #Returns the sum

def main():

    #Takes the input from the user
    n = int(input('The number upto which the multiples of 3 or 5 to be calculated and to find their suum: '))

    if n < 0:
        raise ValueError('INVALID NUMBER!')                     #Raises Value Error if the number is below 0.
    print('Sum of multiples of 3 or 5: ',multiples(n))

main()