# left stones odd alcie wins else bob

n = int(input())

def is_even(n):
    if n % 2 ==0:
        return True


if is_even(n):
    print('Bob')
else:
    print('Alice')