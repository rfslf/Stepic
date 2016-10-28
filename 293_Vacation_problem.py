weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
leave = input()
d = int(input())
l = weekdays.index(leave)
r = (l + d) % 7
print("If you leave on {} and return {} days later, you will return on {}.".format(leave, d, weekdays[r]))
