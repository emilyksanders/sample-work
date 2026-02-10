#! /usr/bin/env python3

import argparse
import time
import sys


def setup_args():
    """Initialize command line arguments"""

    # Create a parser object
    parser = argparse.ArgumentParser(
        description="Get list of prime numbers up to value N"
    )

    # Add an argument to accept a list of integers
    parser.add_argument(
        dest="num_list",
        metavar="N",
        type=int,
        nargs="+",
        help="A list of integers for the process",
    )

    # Add a string argument just for fun
    parser.add_argument(
        "--fun_string",
        "-f",
        dest="funString",
        metavar="FUNSTUFF",
        type=str,
        default=None,
        required=False,
        help="Sample of how to pass a string argument into a script",
    )

    # Add a string argument just for fun
    parser.add_argument(
        "--my_switch",
        "-s",
        dest="mySwitch",
        action="store_true",
        default=False,
        required=False,
        help="Sample of how to pass Boolean flag into script",
    )

    my_choice = parser.add_mutually_exclusive_group(required=False)
    my_choice.add_argument(
        "-a",
        dest="myA",
        action="store_true",
        default=False,
        required=False,
        help="Sample of how to pass Boolean flag A into script",
    )
    my_choice.add_argument(
        "-b",
        dest="myB",
        action="store_true",
        default=False,
        required=False,
        help="Sample of how to pass Boolean flag B into script",
    )

    # Parse the arguments
    args = parser.parse_args()

    return args


def get_prime_list(num_max):
    """Return a list of prime numbers up to the maximum number passed to function"""

    # Initialize a list of known prime numbers
    prime_list = [2, 3, 5, 7]

    # Get a list of test candidates up the maximum value
    # Reduce the list by removing multiples of the known primes
    t0 = time.perf_counter()
    test_list = [t for t in range(3, num_max + 1, 2)]
    print(f"Size of test_list: {len(test_list)}")
    for p in prime_list:
        test_list = [t for t in test_list if t % p > 0]
        print(f"Size of test_list after filtering {p}: {len(test_list)}")
    print(f"test_list (sec): {time.perf_counter()-t0}")
    print()

    # The reduction logic above becomes inefficient for larger primes
    # It seems that it becomes more efficient to factorize the remaining test values
    # To do this create a shorter list of test candidates up to sqrt of the maximum
    t0 = time.perf_counter()
    fact_list = [t for t in test_list if t * t <= num_max]
    print(f"fact_list (sec): {time.perf_counter()-t0}")
    print(f"Size of fact_list: {len(fact_list)}")
    print(fact_list)
    print()

    # To be more efficient later on create a list of only prime factors
    t0 = time.perf_counter()
    prime_factor_list = []
    while len(fact_list) > 0:
        prime_factor_list.append(fact_list[0])
        fact_list = [f for f in fact_list if f % prime_factor_list[-1] != 0]
    print(f"prime_factor_list (sec): {time.perf_counter()-t0}")
    print(f"Size of prime_factor_list: {len(prime_factor_list)}")
    print(f"Prime factor list:\n{prime_factor_list}")
    print()

    # Create final primes list by eliminating test values that are factorable
    t0 = time.perf_counter()
    for t in test_list:
        if not any((t % f == 0) for f in [p for p in prime_factor_list if p * p <= t]):
            prime_list.append(t)
    print(f"new_primes (sec): {time.perf_counter()-t0}")
    print(f"Size of final primes list: {len(prime_list)}")
    print()

    # Return results
    return [p for p in prime_list if p <= num_max]


def main():
    """This is the main code excution entry point"""

    # Initialize command line arguments
    print(sys.argv)
    args = setup_args()
    print(sys.argv)

    print(f"List: {args.num_list}")
    print()

    print(f"Fun String: [{args.funString}]")
    print()

    print(f"My Switch: [{args.mySwitch}]")
    print()

    print(f"My A: [{args.myA}]")
    print()

    print(f"My B: [{args.myB}]")
    print()

    # Determine max absolute value
    num_max = max([abs(n) for n in args.num_list])
    print(f"Max Abs Value: {num_max}")
    print()

    # Get the prime list
    # prime_list = get_prime_list(num_max)
    # if len(prime_list) < 300:
    #     print(f"Primes:\n{prime_list}")


if __name__ == "__main__":
    main()
