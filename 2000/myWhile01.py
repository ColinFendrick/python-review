while True:
    try:
        age = input('How old are you? ')
        intAge = int(age)
        print('You are %s years old!' % (intAge))
        break
    except ValueError:
        print('Sorry, that is not a number')
    finally:
        print('myWhile01.py has run')
