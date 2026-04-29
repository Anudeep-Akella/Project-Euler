# Sum Square Difference

def sum(number):
    """A function for finding the sum of the given range of numbers"""
    sum = 0

    if number <= 0:
        return "Enter a valid number!"

    for i in range(1,number+1):
        sum += i

    return sum ** 2

def square_sum(number):
    """A function for finding the sum of squares of the given range of numbers"""
    if number <= 0:
        return "Enter a valid number!"
    
    squared_sum = 0

    for i in range(1,number+1):
        squared_sum += (i*i)
    
    return squared_sum

def main():
    number = int(input("Enter the number up to which to find sum square and square sum difference: "))

    sum_square = sum(number)
    squared_sum = square_sum(number)
    print(f"The Difference between sum square {sum_square} and square sum {squared_sum} is: {sum_square - squared_sum}")


if __name__ == "__main__":
    main()
