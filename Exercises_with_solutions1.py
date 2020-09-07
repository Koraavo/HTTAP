class User:
    """
    The datetime module supplies classes for manipulating dates and"
    "times in both simple and complex ways.\n"
    " datetime.now(tz=None) returns the current local date and time.\n"
    "If optional argument tz is None or not specified, this is like today().\n"
    "date.strftime(format) returns a string representing the date,"
    "controlled by an explicit format string."
    "Format codes referring to hours, minutes or seconds will see 0 values."""
    pass

# import datetime
# now = datetime.datetime.now()
# day_on_my_birthday = datetime.datetime(2018, 6, 25)
# print("Current date and time: ")
# print(now.strftime("%d-%m-%Y %H:%M:%S\n"))
# print(day_on_my_birthday.strftime("%A"))
#
# help(User)

import sys
print ("Python version")
print(sys.version)
print ("Version Info")
print(sys.version_info)
