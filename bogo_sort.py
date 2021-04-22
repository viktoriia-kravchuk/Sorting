import random
import sys
from load import load_numbers

# The function that randomizes the order of the list is kept in the
# "random" module, so we need to import that here.
# the most terrible sort )))

numbers = load_numbers(sys.argv[1])

def is_sorted(values):
    for index in range(len(values) - 1):
        if values[index] > values[index+1]:
            return False
    return True

def bogo_sort(values):
    attemps = 0
    while not is_sorted(values):
        print(attemps)
        random.shuffle(values)
        attemps += 1
    return values

print(bogo_sort(numbers))
