import calendar


def calendar_module(ip):
    month, day, year = map(int, ip.split())
    day_index = calendar.weekday(year, month, day)
    days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
    return days[day_index]

