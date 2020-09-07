from colors import color

print(color.BLUE + "Write a Python program to display the current date and time.\n" + color.END)

print(color.YELLOW + "The datetime module supplies classes for manipulating dates and" 
"times in both simple and complex ways.\n"
" datetime.now(tz=None) returns the current local date and time.\n"
"If optional argument tz is None or not specified, this is like today().\n"
"date.strftime(format) returns a string representing the date,"
"controlled by an explicit format string."
"Format codes referring to hours, minutes or seconds will see 0 values.\n" + color.END)

import datetime
now = datetime.datetime.now()
day_on_my_birthday = datetime.datetime(2018, 6, 25)
print ("Current date and time: ")
print(now.strftime("%d-%m-%Y %H:%M:%S\n"))
print(day_on_my_birthday.strftime("%A"))

print(color.YELLOW + "A reference of all the legal format codes:\n"
      "%a = weekday, short-version (Wed)\n"
                     "%A = full version\n"
                     "%w = weekday as a day (0=Sunday and 6 = Saturday\n"
                     "%d = day of the month(0-31)\n"
                     "%b = month name short\n"
                     "%B = monthname_full\n"
                     "%m = month as number\n"
                     "%y = year short version(18)\n"
                     "%Y = year full (2018)\n"
                     "%H = hour (0-23)\n"
                     "%I = hour(0-12)\n"
                     "%p = AM/PM\n"
                     "%M = minute\n"
                     "%S = seconds\n"
                     "%f = microseconds\n"
                     "%z = UTC offset\n"
                     "%Z = timezone(IST)\n"
                     "%j = day number of year (00-365)\n"
                     "%U = Week number of year (Sunday as first day 00-53)\n"
                     "%W = week number with monday as first day\n"
                     "%c = local version of date and time\n"
                     "%x = local version of date\n"
                     "%X = local version of time\n"
                     "%% = a % character" + color.END )