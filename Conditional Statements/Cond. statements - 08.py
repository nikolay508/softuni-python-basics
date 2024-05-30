name_movie = input()
episode_time = float(input())
brake_time = float(input()) 

lunch_time = 0.125 * brake_time
otdih_time = 0.25 * brake_time

time_for_episode = brake_time - (lunch_time + otdih_time)

first = time_for_episode - episode_time
second = episode_time - time_for_episode

import math

if episode_time <= time_for_episode:
    print(f"You have enough time to watch {name_movie} and left with {math.ceil(first)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_movie}, you need {math.ceil(second)} more minutes.")
