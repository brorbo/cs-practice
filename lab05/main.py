from logstats import parse_event, count_levels, top_errors, format_report
import sys

path = sys.stdin.readline().strip()

with open(path, encoding="utf-8") as log:
    total = count_levels(log)

with open(path, encoding="utf-8") as log:
    errors = top_errors(log, 3)

strcnt = sum(total.values())
errcnt = total.get('ERROR', 0)
brkncnt = total.get('BROKEN', 0)

print(strcnt, errcnt, brkncnt, sep = '\n')

rprt = format_report(total, errors)

with open('report.txt', 'w', encoding="utf-8") as report:
    report.write(rprt)
