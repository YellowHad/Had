import datetime
import time

datetime_1970 = datetime.datetime(1970, 2, 1, 0, 0, 0, 0)
print(datetime_1970)
print(datetime.datetime.now())

time_since_1970 = datetime.datetime.now() - datetime.datetime(1970, 1, 1, 0, 0, 0, 0)
print(time_since_1970.total_seconds())

dateOfBirth = datetime.datetime(1990, 4, 18, 0, 0, 0, 0)
print("Date of birth " + dateOfBirth.__str__())

diffFromBirth = datetime.datetime.now() - dateOfBirth
print("Difference between now and birth date " + diffFromBirth.total_seconds().__str__())

print(dateOfBirth + datetime.timedelta(days=20000))

print(datetime.datetime.strptime('2018 02 01', "%Y %m %d"))
