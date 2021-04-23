WEEKDAYS = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
]


def get_weekday(weekday, days):
    idx = WEEKDAYS.index(weekday) + 1
    idx += days
    weekday = f", {WEEKDAYS[(idx % len(WEEKDAYS))-1]}"
    return weekday


def add_time(start, duration, weekday=None):
    result = {
      'hours': '',
      'minutes': '',
      'tod': '',
      'weekday': '',
      'duration': '',
    }

    if weekday:
        weekday = weekday.lower().title()

    SWITCH = {
      'AM': 'PM',
      'PM': 'AM'
    }

    days = 0
    hours, prefix = start.split(':')
    minutes, tod = prefix.split()
    dur_hours, dur_minutes = map(int, duration.split(':'))
    minutes = int(minutes)
    hours = int(hours)

    additional_hours = (dur_minutes + minutes) // 60
    minutes_result = (dur_minutes + minutes) % 60

    if add_days := (hours + dur_hours) // 24:
        days += add_days
        dur_hours = dur_hours % 24

    hours += additional_hours + dur_hours
    minutes = minutes_result

    if hours >= 12:
        tod = SWITCH[tod]
        if hours > 12:
            hours -= 12
        if tod == 'AM':
            days += 1

    result['hours'] = hours
    result['minutes'] = str(minutes).zfill(2)
    result['tod'] = tod

    if days:
        result['weekday'] = get_weekday(weekday, days) if weekday else ''
        result['duration'] = f' ({days} days later)' if days > 1 else ' (next day)'

    if weekday and not result['weekday']:
        result['weekday'] = f", {weekday}"

    timestamp = f"{result['hours']}:{result['minutes']} {result['tod']}"
    return timestamp + f"{result['weekday']}" + f"{result['duration']}"