tournaments_played = int(input())
started_points = int(input())

points = 0
wins = 0

for _ in range(tournaments_played):
    result = input()
    if result == "W":
        wins += 1
        points += 2000
        started_points += 2000
    elif result == "F":
        points += 1200
        started_points += 1200
    elif result == "SF":
        points += 720
        started_points += 720

import math
sredno = math.floor(points / tournaments_played)

print(f"Final points: {started_points}")
print(f"Average points: {sredno}")
print(f"{(wins / tournaments_played) * 100:.2f}%")
