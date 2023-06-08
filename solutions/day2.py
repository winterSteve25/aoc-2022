INPUT: str = INPUT
turns = INPUT.split('\n')
to_win = {
    1: 2,
    2: 3,
    3: 1,
}
to_lose = {
    1: 3,
    2: 1,
    3: 2
}

scores = {
    "A": 1,
    "B": 2,
    "C": 3
}

score = 0

for line in turns:
    if not line:
        continue

    choices = line.split(" ")

    opponent_choice = scores[choices[0]]
    requirement = choices[1]
    mychoice = 0

    match requirement:
        case "X":
            mychoice = to_lose[opponent_choice]
        case "Y":
            mychoice = opponent_choice
            score += 3
        case "Z":
            mychoice = to_win[opponent_choice]
            score += 6

    score += mychoice

print(score)
