# .format function
# .format function in fizz/buzz example
# .looping and modulo operator %
# .https://pyformat.info/

if __name__ == "__main__":
    name = "Martin"
    second_name = "Gic"

    print("{} {}".format(name, second_name))

for x in range(100):
    fizzValue = "fizz" if x % 10 == 0 else ""
    buzzValue = "buzz" if x % 7 == 0 else ""
    dzzzValue = "dzzz" if x % 6 == 0 else ""

    value = fizzValue + buzzValue + dzzzValue

    print("{} {}".format(str(x) + " - ", value or x))

# __str__ in object
class Data(object):
    def __str__(self):
        return "{}".format(self.__class__)

    def __repr__(self):
        return "{}".format('one')


print("{0!s} {0!r}".format(Data()))

# padding left with character
print("{:x>10}".format("Martin"))

# padding right without character
print("{:10}".format("Martin"))

# padding right with character
print("{:x<10}".format("Martin"))

# aligning values into the center
print("{:^10}".format("Martin"))

# aligning values into the center with character
print("{:_^10}".format("Martin"))

# truncating long strings
print("{:.4}".format("This is a long string"))

# truncating long strings with center alignment
print("{:^20.5}".format("ThisIsALongString"))

# truncating long strings with aligning and replacing character
print("{:_<20.5}".format("ThisIsALongString"))

# signed numbers
print("{:+d}".format(43))

# using space character to indicate that negative numbers should be prefixed with a minus symbol
print("{: d}".format(-56))