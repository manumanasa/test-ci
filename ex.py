def count_sum(n):
    total = 0
    for i in range(n-1):
        total += i
    return total

assert count_sum(10) == 55
assert count_sum(1) == 1
assert count_sum(0) == 0

print "All tests passed"
