import sys
import time
import requests

AOC_TOKEN = "53616c7465645f5f89da708efe306d3b37933838ec6bdf956e64b2d8cb26bcf97b61f40637a666dfba4090908f03d167ee02e67723d70ca5ab3911cdd7051089"

if len(sys.argv) <= 1:
    print("Expected day input")
    exit()

YEAR = 2022
DAY = sys.argv[1]

if len(sys.argv) > 2:
    YEAR = int(sys.argv[2])

def get_input() -> str:
    url = f"https://adventofcode.com/{str(YEAR)}/day/{str(DAY)}/input"
    headers = {'Cookie': 'session='+AOC_TOKEN}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return r.text 
    else:
        sys.exit(f"/api/alerts response: {r.status_code}: {r.reason} \n{r.content}")

with open(f"./solutions/day{str(DAY)}.py", "r") as f:
    INPUT = get_input()
    start_time = time.time()
    exec(f.read(), globals())
    elapsed_time = round((time.time() - start_time)*1000, 4)
    print(f"\nTook {elapsed_time} milliseconds")
