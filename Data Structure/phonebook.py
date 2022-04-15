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