def phonebook():
    print("Hello!, how many people would you like to register?")
    n = int(input())
    name_numbers = [input().split() for _ in range(n)]
    print(name_numbers)
    phone_book = {k: v for k,v in name_numbers}
    while True:
        try:
            name = input()
            if name in phone_book:
                print('%s=%s' % (name, phone_book[name]))
            else:
                print('Not found')
        except:
            break

# Decorated
def phonebook():
    print("Hello!, how many people would you like to register?")
    num_of_register = int(input())
    print(f"Proceed with {num_of_register} people")
    name_number = [input().split() for i in range(num_of_register)]
    phone_book = {k:v for k, v in name_number}
    while True:
        try:
            print("Retrieve your name here")
            name = input()
            if name in phone_book:
                print("Your registration number is: ")
                print( phone_book[name] )
                print("Would you like to continue?")
                answer = input()
                if answer == "yes":
                    continue
                else:
                    break
        except:
            break