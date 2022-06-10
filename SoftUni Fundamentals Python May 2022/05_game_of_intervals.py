all_steps = int(input())
result = 0
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
count_invalid = 0
for step in range(1, all_steps + 1):
    new_step = int(input())

    if new_step < 0 or new_step > 50:
        result = result / 2
        count_invalid += 1
    elif new_step >= 0 and new_step <= 9:
        result += new_step * 0.20
        p1 += 1
    elif new_step >= 10 and new_step <= 19:
        result += new_step * 0.30
        p2 += 1
    elif new_step >= 20 and new_step <= 29:
        result += new_step * 0.40
        p3 += 1
    elif new_step >= 30 and new_step <= 39:
        result += 50
        p4 += 1
    elif new_step >= 40 and new_step <= 50:
        result += 100
        p5 += 1

print(f"{result:.2f}")

print(f"From 0 to 9: {p1 / all_steps * 100:.2f}%")
print(f"From 10 to 19: {p2 / all_steps * 100:.2f}%")
print(f"From 20 to 29: {p3 / all_steps * 100:.2f}%")
print(f"From 30 to 39: {p4 / all_steps * 100:.2f}%")
print(f"From 40 to 50: {p5 / all_steps * 100:.2f}%")

print(f"Invalid numbers: {count_invalid / all_steps * 100:.2f}%")
