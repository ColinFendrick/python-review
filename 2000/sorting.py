prices = {'Apple': 1.99, 'Banana': 0.99,
          'Orange': 1.49, 'Cantaloupe': 3.99, 'Grapes': 0.39, 'FibFruit': 12358.13}

print('Unsorted: ', prices)
print('Sorted by keys alphabetically (default): ', sorted(prices))
print('Sorted by values lowest => highest (default): ', sorted(prices.values()))
print('Sorted by values (and return keys): ', sorted(prices, key = prices.__getitem__))
print('Sort by keys (and return values): ', [value for (key, value) in sorted(prices.items())])
print('Sort by valies highest => lowest and return everything: ', sorted(prices.items(), key = lambda x: x[1], reverse = True))
print('Sort by whether or not the value is divisible by 3: ', sorted(prices.items(), key = lambda price: (price[1] * 100) % 3))


def countFibs(val):
    count = 0
    fibs = [1, 2, 3, 5, 8]

    # Remove decimal and rejoin into string
    s = ''.join(str(val[1]).split('.'))

    # Get each digit
    digits = [int(d) for d in str(s)]
    for digit in digits:
        if int(digit) in fibs:
            count += 1

    return count


print('Count digits present in fibonnaci sequence: ',
      sorted(prices.items(), key=countFibs, reverse=True))
