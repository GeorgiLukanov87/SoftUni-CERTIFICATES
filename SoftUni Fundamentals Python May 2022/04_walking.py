steps = input()
current_steps = 0
step_goal = 10000

while True:
    if steps == "Going home":
        steps = int(input())
        current_steps += steps
        if current_steps >= step_goal:
            print(f'Goal reached! Good job!')
            print(f'{current_steps-step_goal} steps over the goal!')
        else:
            print(f'{step_goal-current_steps} more steps to reach goal.')
        break

    steps = int(steps)
    current_steps += steps

    if current_steps >= 10000:
        print(f"Goal reached! Good job!")
        print(f'{current_steps - step_goal} steps over the goal!')
        break
    steps = input()
