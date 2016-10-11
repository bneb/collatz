#
#   This serves as a unit test module for collatz implementations
#

from implementations import simple_collatz, collatz, quick_collatz, recursive_collatz

for t in range(100):
    v1 = simple_collatz(t)
    v2 = collatz(t)
    v3 = quick_collatz(t)
    v4 = recursive_collatz(t)
    print(v1, v2, v3, v4)
    assert(v1 == v2 and v2 == v3 and v3 == v4)
