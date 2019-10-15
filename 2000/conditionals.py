# if True and False:
#     print('This will never run')

# if True or False:
#     print('This will print')

# if not (True and False):
#     print('Will print with not inversion')

if True and False:
    print('Won\'t print')

elif True and False:
    print('Or condition will print')

elif True:
    # Won't print
    print('Just true printing')

elif not (True and False):
    # Won't print
    print('Negated union printing')

else:
    # Won't print
    print('Finally')
