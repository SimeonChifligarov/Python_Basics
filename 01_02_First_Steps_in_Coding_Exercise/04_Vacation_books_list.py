pages_total = int(input())
pages_hourly = int(input())
days_total = int(input())

# total_hours = pages_total // pages_hourly
# daily_hours = total_hours // days_total
daily_hours = (pages_total // pages_hourly) // days_total

print(daily_hours)
