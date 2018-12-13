def count_sum(n):
    total = 0
    for i in range(n+1):
        total += i
    return total

def add_one(a):
    return a + 1

assert count_sum(10) == 55
assert count_sum(1) == 1
assert count_sum(0) == 0

assert add_one(10) == 11
assert add_one(0) == 1

print "All tests passed"
