def analyze_exam_arrival(exam_hour: int, exam_minute: int, arrival_hour: int, arrival_minute: int) -> str:
    """
    Determines the student's arrival status for an exam based on the scheduled and actual arrival time.

    Args:
        exam_hour: Hour of the exam start time.
        exam_minute: Minute of the exam start time.
        arrival_hour: Hour of the student's arrival.
        arrival_minute: Minute of the student's arrival.

    Returns:
        A message indicating if the student is early, on time, or late, with the time difference.
    """
    exam_total: int = exam_hour * 60 + exam_minute
    arrival_total: int = arrival_hour * 60 + arrival_minute
    time_difference: int = arrival_total - exam_total

    status: str
    timing_info: str = ''

    if time_difference > 0:
        status = 'Late'
        if time_difference < 60:
            timing_info = f'{time_difference} minutes after the start'
        else:
            hours: int = time_difference // 60
            minutes: int = time_difference % 60
            timing_info = f'{hours}:{minutes:02d} hours after the start'
    elif time_difference >= -30:
        status = 'On time'
        if time_difference != 0:
            timing_info = f'{abs(time_difference)} minutes before the start'
    else:
        status = 'Early'
        if abs(time_difference) < 60:
            timing_info = f'{abs(time_difference)} minutes before the start'
        else:
            hours: int = abs(time_difference) // 60
            minutes: int = abs(time_difference) % 60
            timing_info = f'{hours}:{minutes:02d} hours before the start'

    if timing_info:
        return f'{status}\n{timing_info}'
    return status


if __name__ == '__main__':
    exam_hour_input: int = int(input())
    exam_minute_input: int = int(input())
    arrival_hour_input: int = int(input())
    arrival_minute_input: int = int(input())

    result: str = analyze_exam_arrival(
        exam_hour=exam_hour_input,
        exam_minute=exam_minute_input,
        arrival_hour=arrival_hour_input,
        arrival_minute=arrival_minute_input
    )
    print(result)
