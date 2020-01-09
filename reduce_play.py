def add(num1, num2):
    """Return the sum of the two inputs."""

    return num1 + num2


def identify_prefix(tolkens):
    """ Calls correct function based on user input """

    num1 = int(tolkens[1])
    
    if len(tolkens) > 2:
        num2 = int(tolkens[2])

    if tolkens[0] == "+":
        output = add(num1, num2)

    return output


def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value


while True:

    user_input = input()

    tolkens = user_input.split(" ")

    if tolkens[0] == "q":
        break

    numbers = tolkens[1:]

    for i, num in enumerate(numbers):
        numbers[i] = int(num)

    answer = identify_prefix(tolkens)
    reduce_answer = reduce(add, numbers)
    print(reduce_answer)
    print(answer)