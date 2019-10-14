
def isSpecial():
    option = input('Press any key, then tap "enter": ')

    if option.isalnum():
        print('is punctuation')
    else:
        print('is alnum')

    print('option="' + option + '"')


isSpecial()
