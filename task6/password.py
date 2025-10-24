def has_digit(users_password):
    return any(symbol.isdigit() for symbol in users_password)


def is_very_long(users_password):
    min_password_len = 12
    users_password_len = len(users_password)
    return users_password_len > min_password_len


def has_upper_letters(users_password):
    return any(symbol.isupper() for symbol in users_password)


def has_lower_letters(users_password):
    return any(symbol.islower() for symbol in users_password)


def has_symbols(users_password):
    return any(
        not symbol.isdigit() and not symbol.isalpha() for symbol in users_password)


def main():
    users_password = input("Введите пароль: ")

    score = 0

    check_password = [
        has_digit,
        is_very_long,
        has_lower_letters,
        has_upper_letters,
        has_symbols,
    ]

    for single_check in check_password:
        if single_check(users_password):
            score += 2

    print(f"Рейтинг пароля: {score}", end="")


if __name__ == "__main__":
    main()
