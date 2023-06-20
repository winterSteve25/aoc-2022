INPUT: str = INPUT
lines: list[str] = INPUT.split('\n')
# lines = [ "ZZ" ]

sum = 0

def priority_of(char) -> int:
    return ord(char) - 38 if char.isupper() else ord(char) - 96

for index in range(len(lines)):
    elf1 = set(lines[index])
    elf2 = set(lines[index + 1])
    elf3 = set(lines[index + 2])
    index += 2

    common12 = elf1.intersection(elf2)
    common = common12.intersection(elf3)
    sum += priority_of(common)

print(sum)
