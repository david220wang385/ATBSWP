import collatz

# Start of program
print("Enter number to see Collatz Sequence:")
try:
    number = int(input())
    collatz.collatz(number)
except ValueError:
    print("ERROR: Input is not a number, please enter a valid integer")
