lines = INPUT.split('\n')
calories = []
n = 0

for line in lines:
    if line and line != "\n":
        if len(calories) <= n:
            calories.append(int(line))
        else:
            calories[n] += int(line)
    else:
        n += 1

calories.sort(reverse=True)
print(calories[0] + calories[1] + calories[2])
