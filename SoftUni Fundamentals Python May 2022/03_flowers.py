count_chrysanthemums = int(input())
count_roses = int(input())
count_tulips = int(input())
season = input()
holiday = input()

if season == "Spring" or season == "Summer":
    chrysanthemums = 2
    roses = 4.10
    tulips = 2.50
    flowers_sum = (count_chrysanthemums * chrysanthemums) + (count_roses * roses) + (count_tulips * tulips)
    if holiday == "Y":
        flowers_sum += flowers_sum * 0.15
    if count_tulips > 7:
        flowers_sum -= flowers_sum * 0.05

if season == "Autumn" or season == "Winter":
    chrysanthemums = 3.75
    roses = 4.50
    tulips = 4.15
    flowers_sum = (count_chrysanthemums * chrysanthemums) + (count_roses * roses) + (count_tulips * tulips)
    if holiday == "Y":
        flowers_sum += flowers_sum * 0.15
    if count_roses >= 10 and season == "Winter":
        flowers_sum -= flowers_sum * 0.10

if count_roses+count_tulips+count_tulips > 20:
    flowers_sum -= flowers_sum*0.20

print(f"{(flowers_sum + 2):.2f}")
