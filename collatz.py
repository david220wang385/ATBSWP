# Sequence that will always eventually converge to 1
def collatz(number):
    if number != 1:
        if number % 2 == 0:
            print(number // 2)
            return collatz(number // 2)
        else:
            print(number * 3 + 1)
            return collatz(number * 3 + 1)
    print("Collatz Sequence Complete")
