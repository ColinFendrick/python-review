def sortLogic(ref):
    return len(ref)


data = {"First": "John", "Last": "Doe",
        "Phone": "123-456-7800", "Email": "foo@bar.com"}

keys = list(data.keys())
# Sort based on logic
keys.sort(key=sortLogic)

for key in keys:
    print("%10s:[%-20s]" % (key, data[key]))

print(data.items())
