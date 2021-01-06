def hand_dif(hour, minute):
    percent_minute = 100 * minute / 60
    distance_from_hour = 5 * percent_minute / 100
    hour_in_minute = (hour * 5) + distance_from_hour
    dif_in_minutes = hour_in_minute - minute
    angle = 360 * dif_in_minutes / 60
    if angle > 0:
        return 360 - angle
    return abs(angle)

#12345