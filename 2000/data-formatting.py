# class DataFormatting:

#     def __init__(self, email, phone, last, first):
#       self.email = email
#       self.phone = phone
#       self.last = last
#       self.first = first

#     def __dict__(self):
#       from collections import OrderedDict
#       result = OrderedDict()
#       result["email"] = "[%-10s]" % (self.email)
#       result["phone"] = "[%-10s]" % (self.phone)
#       result["last"] = "[%-10s]" % (self.last)
#       result["first"] = "[%-10s]" % (self.first)
#       return result
# x = DataFormatting('c@f.gmail.com', '812-938-8378', 'Smith', 'Joe')
# print(x.__dict__())

data = {"First": "John", "Last": "Doe", "Phone": "123-456-7800", "Email": "foo@bar.com"}

for key in data.keys():
    print("[%10s]:[%-20s]" % (key, data[key]))

