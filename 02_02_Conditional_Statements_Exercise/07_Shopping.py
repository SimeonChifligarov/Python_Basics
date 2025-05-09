budget = float(input())
video_cards = int(input())
processors = int(input())
ram_units = int(input())

video_card_price = 250
total_video_card_cost = video_cards * video_card_price
processor_price = total_video_card_cost * 0.35
ram_price = total_video_card_cost * 0.1

total_cost = total_video_card_cost + processors * processor_price + ram_units * ram_price

if video_cards > processors:
    total_cost *= 0.85

remaining = budget - total_cost

if remaining >= 0:
    print(f'You have {remaining:.2f} leva left!')
else:
    print(f'Not enough money! You need {abs(remaining):.2f} leva more!')
