import sys

try:
    # Does not exist
    file = open('myfile.txt')
    line = file.readline()
    ival = int(line.strip())
    print(ival)

except IOError as ex:
    # File not found error
    print('IOError({0}): {1}'.format(ex.errno, ex.strerror))

except ValueError:
    # Integer conversion error
    print('Unable to convert line to integer')

except:
    # Catch-all
    print('Unexpected exception:', sys.exc_info()[0])
