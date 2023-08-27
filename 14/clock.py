hour = int(input("Enter the hour: "))
minute = int(input("Enter the minute: "))
second = int(input("Enter the second: "))

clock = {"hour": hour, "minute": minute, "second": second}

def add_time(clock, hours, minutes, seconds):
    clock["second"] += seconds
    if clock["second"] >= 60:
        clock["second"] -= 60
        clock["minute"] += 1
    clock["minute"] += minutes
    if clock["minute"] >= 60:
        clock["minute"] -= 60
        clock["hour"] += 1
    clock["hour"] = (clock["hour"] + hours) % 24

def subtract_time(clock, hours, minutes, seconds):
    clock["second"] -= seconds
    if clock["second"] < 0:
        clock["second"] += 60
        clock["minute"] -= 1
    clock["minute"] -= minutes
    if clock["minute"] < 0:
        clock["minute"] += 60
        clock["hour"] -= 1
    clock["hour"] = (clock["hour"] - hours) % 24

hours = int(input("Enter the number of hours to add or subtract: "))
minutes = int(input("Enter the number of minutes to add or subtract: "))
seconds = int(input("Enter the number of seconds to add or subtract: "))

add_time(clock, hours, minutes, seconds)
print(f"The time after adding {hours} hours, {minutes} minutes and {seconds} seconds is {clock['hour']}:{clock['minute']}:{clock['second']}")

hours = int(input("Enter the number of hours to add or subtract: "))
minutes = int(input("Enter the number of minutes to add or subtract: "))
seconds = int(input("Enter the number of seconds to add or subtract: "))

subtract_time(clock, hours, minutes, seconds)
print(f"The time after subtracting {hours} hours, {minutes} minutes and {seconds} seconds is {clock['hour']}:{clock['minute']}:{clock['second']}")
