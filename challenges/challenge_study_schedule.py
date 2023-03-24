def count_periods(permanence_period, target_time):
    contador = 0
    for (period_start, period_end) in permanence_period:
        if not isinstance(period_start, int) or not isinstance(
            period_end, int
        ):
            return None
        if target_time >= period_start and target_time <= period_end:
            contador += 1
    return contador


def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    if not isinstance(permanence_period, list) or len(permanence_period) == 0:
        return None
    return count_periods(permanence_period, target_time)
