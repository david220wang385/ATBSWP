def stringify_list(list):

    # Trivial cases
    if len(list) == 0:
        return None
    elif len(list) == 1:
        return list[0]
    elif len(list) == 2:
        return list[0] + " and " + list[1]

    # Generalized case
    str = ""
    for i in range(len(list) - 1):
        str += list[i] + ", "
    str += "and " + list[-1]
    return str


# Start of program
shopping_cart = ['apples', 'cereal', 'milk', 'cookies']
single_elem = ['one']
two_elem = ['one', 'two']
test_cases = [shopping_cart, single_elem, two_elem]
for i in test_cases:
    print(stringify_list(i))
