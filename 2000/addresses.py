data = {'First': 'John',
        'Last': 'Smith',
        'Phone': '123-456-7890'
        }

byVal = data['Phone']
byRef = id(data['Phone'])
print(byVal, byRef)

# Update the phone number and the refs change
data['Phone'] = '987-654-3210'
# ... but not yet!
print(byVal, byRef) # This is the same as the ones listed above
print(data['Phone'], id(data['Phone'])) # This data is new!
byVal = data['Phone']
byRef = id(data['Phone'])
print(byVal, byRef)

