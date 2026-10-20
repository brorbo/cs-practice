from stats import average_by_city, read_valid, warmest_city, total
import sys

lines = sys.stdin.read().splitlines()

data = read_valid(lines)

avgs = average_by_city(data)

suc, den, avg = len(data), len(lines) - len(data), avgs[warmest_city(data)]

print(suc, den, '%4.1f' % avg, sep = '\n')
