age_input = float(input())
gender_input = input()

title = ''
if gender_input == 'm':
    if age_input >= 16:
        title = 'Mr.'
    else:
        title = 'Master'

elif gender_input == 'f':
    if age_input >= 16:
        title = 'Ms.'
    else:
        title = 'Miss'

print(title)
