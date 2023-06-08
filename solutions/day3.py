INPUT: str = INPUT
lines: list[str] = INPUT.split('\n')
# lines = [ "ZZ" ]

sum = 0

def priority_of(char) -> int:
    return ord(char) - 38 if char.isupper() else ord(char) - 96
