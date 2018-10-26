# list comprehensions in Python
# list comprehension of a class variables of a list

# list
list_1 = range(10)
print(list_1)

# multiplying each element of the list with 2
list_2 = [elem * 2 for elem in list_1]
print list_2

# dividing each element from the list
list_3 = [float(elem) / 5 for elem in list_2]
print list_3

# power to 2 with **
list_4 = [elem ** 2 for elem in list_1]
print list_4

# condition on the list
list_5 = [elem for elem in list_1 if elem % 2 == 0]
print list_5


# declare a class
class T:
    def __init__(self, transaction_name, transaction_amount):
        self.transaction_name = transaction_name
        self.transaction_amount = transaction_amount

listOfTransactions = [T('L1', 100), T('L2', 300), T('D1', 400), T('D2', 456), T('D3', 879)]

t = [trans.transaction_name for trans in listOfTransactions if trans.transaction_amount >= 300]

print(t)
