import datetime

secondCount = int(input("Input second count: "))
dateTime = datetime.datetime.fromtimestamp(secondCount, tz=datetime.timezone.utc)
print(dateTime.strftime("%d %H:%M:%S"))