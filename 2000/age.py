name = input('What is your name? ')
print('Hello', name)
while True:
    try:
        age = input('What is your age? ')
        intAge = int(age)
        print('%s is %d years old!' % (name, intAge))
    except ValueError:
        print('Sorry, that age is not a number')
    else:
        print('\t What else happens?')
        break
    finally:
        print('Data entry completed')
