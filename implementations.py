#
#   The Collatz conjecture describes a phenomenon that is easily apprehended,
#   but impossible to solve even by top mathematicians.
#   The conjecture states that given a positive number n, iteratively following these rules:
#       if n is even, n = n/2
#       if n is odd, n = 3n + 1
#   will lead n eventually, to 1.
#   Examples:
#   2 -> 1
#   3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
#   4 -> 2 -> 1
#   5 -> 16 -> 8 -> 4 -> 2 -> 1
#   ... and so on ...
#
#   The sequence of numbers from n to 1 can be called a Collatz-path, or path for short in this context.
#   Below are four implementations of code to calculate the length of a path for n.

def simple_collatz(n):
    """Simple implemenation, expects a number n > 0"""
    path_length = 0
    while(n > 1):
        path_length += 1
        if(n % 2 == 0):
            n //= 2
        else:
            n = 3 * n + 1
    return path_length

#   As was pointed out in this video where I learned of the conjecture (https://www.youtube.com/watch?v=5mFpVDpKX70)
#   if n > 1 and n is odd, then we can bundle the 3n+1 step with the n/2 step, removing a check of the while condition.

def collatz(n):
    """Slightly improved implemenation, expects a number n > 0"""
    path_length = 0
    while(n > 1):
        if(n % 2 == 1):
            n = (3 * n + 1) / 2
            path_length += 2
        else:
            n //= 2
            path_length += 1
    return path_length

#   Notice that in the examples above, 5 and 4 tread the same path from 4 to 1
#   We can store the previously calculated path lengths and stop calculation
#   when a non-zero path is found

def quick_collatz(n, lookup = {}):
    starting_number = n
    path_length = 0
    while(n > 1):
        if n in lookup:
            path_length += lookup[n]
            break
        if n % 2 == 1:
            n = (3 * n + 1) // 2
            path_length += 2
        else:
            n //= 2
            path_length += 1
    lookup[starting_number] = path_length
    return path_length

#   That stores the path lengths of the starting number, but the path can cover much more ground.
#   To store the intermediate values, we will use recursion to compute the path length at every step.

def recursive_collatz(n, lookup = {}):
    if(n < 2):
        return 0
    elif n in lookup:
        return lookup[n];
    elif n % 2 == 0:
        lookup[n] = 1 + recursive_collatz(n // 2, lookup)
    else:
        lookup[n] = 2 + recursive_collatz((3 * n + 1) // 2, lookup)
    return lookup[n]

