#simple function to return the nth fibonacci value when given n

def fibo (n):
    list = [0,1,1]
    if n == 0:
        x = 'This is not a valid value, enter a number above one....'
    elif n < 3:
        x = list[n-1]
    else:
        while n > len(list):
            list.append(list[-2] + list[-1])
        else:
            x = list[-1]
    return x

while True:
    try:
        input_n = int(input('This script will return the nth number in the fibnacci sequence when given n, please enter n: \n'))
    except ValueError:
        print('Sadly not understood, enter a number.')
    else:
        print('The number in place {} of the fibonacci sequence is: '.format(int(input_n)) + str(fibo(input_n)))
        break
