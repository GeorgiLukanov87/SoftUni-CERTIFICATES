w = float(input())
h = float(input())

w_meters = w * 100
h_meters = (h * 100) - 100

h_seats = h_meters // 70
w_seats = w_meters // 120

total_seat = h_seats * w_seats - 3

print(total_seat)
