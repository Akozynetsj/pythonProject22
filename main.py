def calculate_squares(**kwargs):
    result = {}
    for key, value in kwargs.items():
        result[key] = value ** 2
    return result
