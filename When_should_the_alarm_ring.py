time = input("Enter the current time in hours: ")  # 5
alarm_hours = input("After how many hours should the alarm go off: ")  # 15
total_time = int(alarm_hours) + int(time)  # 20
current_time = int(time) % 12  # 5
total_alarm_wake_up_time = total_time % 12  # 8
if time <= 12:
    print("The current time is:", str(current_time), "am")
else:
    print("The current time is:", str(current_time), "pm")

if total_time > 24:
    print("The alarm will go off at:", str(total_alarm_wake_up_time), "am")
else:
    print("The alarm will go off at:", str(total_alarm_wake_up_time), "pm")


