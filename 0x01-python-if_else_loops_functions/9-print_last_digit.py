def print_last_digit(number):
    if (number < 0):
        print("{}".format((-1 * number) % 10), end="")
        return ((-1 * number) % 10)
    print("{}".format(number % 10), end="")
    return (number % 10)
