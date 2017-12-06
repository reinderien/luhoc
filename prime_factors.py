import math
import timeit


def main():
    input_number = input("Enter a number to find the prime factors of: ")  # Get number to check prime factors of
    start_time = timeit.default_timer()  # Start timer
    prime_factor_array = prime_factors(input_number)  # Calculate Prime Factors
    elapsed = round((timeit.default_timer() - start_time) * 1000, 2)  # End Timer
    print_array(prime_factor_array, elapsed)  # Print out prime factors and elapsed code time


def prime_factors(number):
    # Initialize empty array to contain prime factors.
    # Add things to array with prime_factor_array.append(10)
    prime_factor_array = []

    ##### Your Code Here #####

    return prime_factor_array  # Return array of prime factors


def print_array(array_to_print, elapsed_time):
    print ', '.join(map(str, array_to_print))
    print str(elapsed_time) + 'ms' + '\n'


main()
