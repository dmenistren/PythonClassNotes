from error import ApiError


def name(a):
    if not isinstance(a, int):
        raise ApiError("Input must be an integer.")
    return a * 2


name("Hello")  # This will raise CustomError
