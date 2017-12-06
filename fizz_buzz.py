# Write a program that prints the numbers from 1 to 100.
# For multiples of three print “Fizz” instead of the number
# For the multiples of five print “Buzz”.
# For numbers which are multiples of both three and five print “FizzBuzz”.

# For Loop
for i in range(1, 101):
    print(i)

# While Loop
i = 1
while (i < 101):
    print(i)
    i = i + 1


# Simple Recursion
def recursive_fizzbuzz(i):
    if (i > 100):
        return
    recursive_fizzbuzz(i + 1)


recursive_fizzbuzz(1)

# Which of these solutions is best?
# Can you Combine a for loop with a function (def)?

# Some solutions are hidden below. There is more than one right answer!
























































































































































# For Loop
for i in range(1, 101):

    if (i % 15 == 0):
        print
        "FizzBuzz"

    elif (i % 3 == 0):
        print
        "Fizz"

    elif (i % 5 == 0):
        print
        "Buzz"

    else:
        print
        i

# While Loop
i = 1
while (i < 101):

    if (i % 15 == 0):
        print("FizzBuzz")

    elif (i % 3 == 0):
        print("Fizz")

    elif (i % 5 == 0):
        print("Buzz")

    else:
        print(i)

    i = i + 1


# Simple Recursion
def recursive_fizzbuzz(i):
    if i > 100: return

    if (i % 15 == 0):
        print("FizzBuzz")

    elif (i % 3 == 0):
        print("Fizz")

    elif (i % 5 == 0):
        print("Buzz")

    else:
        print(i)

    recursive_fizzbuzz(i + 1)


recursive_fizzbuzz(1)


# Optimal Solution
def fizzbuzz(i):
    if (i % 15 == 0):
        return "FizzBuzz"
    elif (i % 3 == 0):
        return "Fizz"
    elif (i % 5 == 0):
        return "Buzz"
    else:
        return i


for i in range(1, 101):
    print(fizzbuzz(i))
    #