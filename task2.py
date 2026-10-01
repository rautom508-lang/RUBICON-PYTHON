def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

times_three = make_multiplier(3)
times_five = make_multiplier(5)

print(times_three(10))
print(times_five(10))