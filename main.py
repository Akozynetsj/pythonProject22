def get_odd_numbers(*args):
    odd_numbers = [num for num in args if num % 2 != 0]
    return odd_numbers
