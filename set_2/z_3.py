def reverse(n):
    reversed_num = 0
    while n > 0:
        reversed_num *= 10
        reversed_num += n % 10
        n //= 10

    return reversed_num


def is_palindrome(n):
    return n == reverse(n)

print(f"IS 11223 PALINDROME: {is_palindrome(11223)}")
print(f"IS 55555 PALINDROME: {is_palindrome(55555)}")
