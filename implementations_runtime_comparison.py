#
#   This module makes use of timeit to time various Collatz path length
#   calculation implementations
#

import timeit
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--upto', default=10000)
args = parser.parse_args()

simple_collatz_time = timeit.Timer('for n in range(test_upto): simple_collatz(n)', 'from implementations import simple_collatz; test_upto = {}'.format(args.upto)).timeit(number = 1)
collatz_time = timeit.Timer('for n in range(test_upto): collatz(n)', 'from implementations import collatz; test_upto = {}'.format(args.upto)).timeit(number = 1)
quick_collatz_time = timeit.Timer('for n in range(test_upto): quick_collatz(n, lookup)', 'from implementations import quick_collatz; test_upto = '+str(args.upto)+'; lookup = {}').timeit(number = 1)
recursive_collatz_time = timeit.Timer('for n in range(test_upto): recursive_collatz(n, lookup)', 'from implementations import recursive_collatz; test_upto = '+str(args.upto)+'; lookup = {}').timeit(number = 1)

print("Simple: {}, Collatz: {}, Lookup: {}, Recursive: {}".format(simple_collatz_time, collatz_time, quick_collatz_time, recursive_collatz_time))
