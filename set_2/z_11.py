def are_digits_ascending(n: int):
    previous_digit = None
    while n > 0:
        current_digit = n % 10
        if previous_digit:
            if current_digit >= previous_digit: return False
        previous_digit = current_digit
        n //= 10
    return True



print(are_digits_ascending(1245))
