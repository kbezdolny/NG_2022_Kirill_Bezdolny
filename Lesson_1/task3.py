secondsCount = int(input("Input second count: "))
data = []

# calculate seconds
data.append(secondsCount % 60)
# calculate minutes
data.append((secondsCount % 3600) // 60)
# calculate hours
data.append(secondsCount // 3600)
# calculate days
data.append(data[2] // 24)

# set max 23 hours
if data[2] > 23:
    data[2] = data[2] % data[3]

# add deco zero
for i in range(0, len(data)-1):
    if data[i] < 10:
        data[i] = f"0{data[i]}"

print(f"Day {data[3]} {data[2]}:{data[1]}:{data[0]}")