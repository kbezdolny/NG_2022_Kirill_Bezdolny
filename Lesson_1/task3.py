secondsCount = int(input("Input second count: "))

# calculate seconds
seconds = ((secondsCount % 86400) % 3600) % 60
# calculate minutes
minutes = ((secondsCount % 86400) % 3600) // 60
# calculate hours
hours = (secondsCount % 86400) // 3600
# calculate days
days = secondsCount // 86400

# output the datetime
print(f"Day {days} {hours}:{minutes}:{seconds}")