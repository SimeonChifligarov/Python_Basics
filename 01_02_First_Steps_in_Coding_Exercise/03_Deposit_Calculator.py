deposit_value = float(input())
months_value = int(input())
interest_value = float(input())

monthly_interest = (deposit_value * interest_value / 100) / 12

final_amount = deposit_value + months_value * monthly_interest

print(final_amount)
