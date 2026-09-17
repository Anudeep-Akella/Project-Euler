# Problem: Sum of Multiples of 3 or 5 below 1000

def multiples(num)-> int:
    """Finds the multiples of 3 or 5 and returns their sum."""
    sum = 0
    for i in range(1,num):
        if i % 3 == 0 or i % 5 == 0:                           
            sum += i

    return sum                                                 

def main():

    #Takes the input from the user
    while True:
        try:
            num = input('The number upto which the multiples of 3 or 5 to be calculated and to find their sum:')
            if int(num) <= 0:
                print("Enter a Valid positive number.")
                continue
            print('Sum of multiples of 3 or 5: ',multiples(int(num)))
            break
        except ValueError:
            print("Invalid! Please Enter a valid number.")                     #Raises Value Error if the number is below 0.

if __name__ == "__main__":
    main()