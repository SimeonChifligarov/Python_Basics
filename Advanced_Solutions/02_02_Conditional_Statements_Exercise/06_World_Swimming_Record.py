from math import floor


def check_swimming_record(
        current_record: float,
        distance_meters: float,
        time_per_meter: float
) -> str:
    """
    This checks if the swimmer breaks the world record considering swimming time and water resistance.

    Args:
        current_record: The world record time in seconds.
        distance_meters: The distance to swim in meters.
        time_per_meter: Time taken to swim 1 meter in seconds.

    Returns:
        A message stating whether the record was broken or how much slower the swimmer was.
    """
    base_time: float = distance_meters * time_per_meter
    resistance_delays: int = floor(distance_meters / 15)
    total_time: float = base_time + resistance_delays * 12.5
    time_difference: float = current_record - total_time

    if time_difference <= 0:
        return f'No, he failed! He was {abs(time_difference):.2f} seconds slower.'
    return f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.'


if __name__ == '__main__':
    record_seconds: float = float(input())
    swim_distance: float = float(input())
    seconds_per_meter: float = float(input())

    result: str = check_swimming_record(
        current_record=record_seconds,
        distance_meters=swim_distance,
        time_per_meter=seconds_per_meter
    )
    print(result)
