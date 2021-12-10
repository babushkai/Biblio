#If i is multiple of both 3 amd 5. print Buzz
#If i is a multiple of 3 print Fizz
#If i is a multiple of 5, print Buzz
#If i is not a multiple of 3 or 5 print i
def fizzbuzz(n):

    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return str(n)