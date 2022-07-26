serial_name = input()
count_seasons = int(input())
count_episodes = int(input())
episode_minutes = int(input())
total_time = 0
advertising_time = episode_minutes * 0.20
episode_minutes += advertising_time
last_episode_time = count_seasons*10
total_time = episode_minutes * count_episodes * count_seasons + last_episode_time
print(f"Total time needed to watch the {serial_name} series is {total_time:.0f} minutes.")