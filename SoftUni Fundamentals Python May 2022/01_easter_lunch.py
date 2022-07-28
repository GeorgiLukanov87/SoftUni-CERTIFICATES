count_sweet_bread = int(input())
count_pack_eggs = int(input())
count_cookies_kg = int(input())

sum_sweet_break = count_sweet_bread * 3.20
sum_eggs = count_pack_eggs * 4.35
sum_cookies = count_cookies_kg * 5.40

sum_paint = (count_pack_eggs * 12) * 0.15

total_sum = sum_sweet_break + sum_eggs + sum_cookies + sum_paint

print(f"{total_sum:.2f}")