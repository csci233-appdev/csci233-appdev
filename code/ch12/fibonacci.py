# This program uses recursion to print numbers
# from the Fibonacci series.

def main():
    # print('The first 10 numbers in the')
    # print('Fibonacci series are:')
    # for number in range(1, 11):
    #    print(fib(number))
    num = int(input('Which fibonacci number do you want to calculate: '))
    print(f'The {num}th fibonacci number is: {fib(num)}')


# The fib function returns the nth number
# in the Fibonacci series.
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# Call the main function.
if __name__ == '__main__':
    main()
