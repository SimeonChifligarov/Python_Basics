length_value = int(input())
width_value = int(input())
height_value = int(input())
percent_value = float(input())

volume_total = length_value * width_value * height_value / 1000
water_volume = volume_total * (1 - percent_value / 100)

print(water_volume)
