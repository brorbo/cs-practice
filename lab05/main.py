from logstats import parse_event, count_levels, top_errors, format_report

path = input()

with open(path, encoding="utf-8") as log:
    total = count_levels(log)

with open(path, encoding="utf-8") as log:
    errors = top_errors(log, 3)

strcnt, errcnt, brkncnt = sum(total[i] for i in total), \
                          total['ERROR'], total['BROKEN']
print(strcnt, errcnt, brkncnt, sep = '\n')

rprt = format_report(total, map(lambda x: [x[0][:-1], x[1]], errors))

with open('report.txt', 'w', encoding="utf-8") as report:
    report.write(rprt)
