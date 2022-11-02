# How many diferent numbers, for example divisible by 7 can we get from deleting specific igits in this number?
# Ex: for 2315 we can get 21, 35, 231, 315

# To solve it, we need to use binary mask


def solve(n: int, divider: int = 7):
    for mask in range(2 ** len(str(n))):
        k = n
        new_num = 0
        multiplier = 1
        while mask > 0:
            digit = k % 10
            k //= 10
            rest = mask % 2
            if rest == 1:
                new_num += multiplier * digit
                multiplier *= 10
            mask //= 2
        if new_num % divider == 0 and new_num > 0:
            print(new_num)


solve(2315, 7)
