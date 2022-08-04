import re

pattern = r"\d+"
result = ""
while True:
    text = input()
    if not text:
        break

    result += " " + text

result = re.findall(pattern, result)
print(*result)

