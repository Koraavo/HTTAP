def mySqrt(n):
    # your code here
    initial_guess = float(n / 2)
    final = (.5) * ((n / initial_guess) + initial_guess)  # formula main
    for i in range(10):
        final = (0.5 * (final + (n / final)))  # same repition as final but in range
    return final


print(mySqrt(225))