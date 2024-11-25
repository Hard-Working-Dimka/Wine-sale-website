ENDINGS_DEPENDENCIES = [
    1,                      # год
    (2, 3, 4),              # года
    (5, 6, 7, 8, 9, 0),     # лет
    (1, 2, 3, 4),           # исключения: 11, 12, 13, 14
]


def get_correct_year_word(year):
    second_last_year_digit = year // 10 % 10
    last_year_digit = year % 10
    if second_last_year_digit == 1 and (last_year_digit == 1 or last_year_digit in ENDINGS_DEPENDENCIES[3]):
        return 'лет'
    elif last_year_digit == ENDINGS_DEPENDENCIES[0]:
        return 'год'
    elif last_year_digit in ENDINGS_DEPENDENCIES[1]:
        return 'года'
    elif last_year_digit in ENDINGS_DEPENDENCIES[2]:
        return 'лет'
