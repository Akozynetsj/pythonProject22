def find_min_max(*args):
    if not args:
        return None

    min_value = float('inf')
    max_value = float('-inf')

    for num in args:
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num

    return min_value, max_value
