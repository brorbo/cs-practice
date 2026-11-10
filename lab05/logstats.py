def parse_event(line: str):
    inf = line.split(maxsplit=2)
    
    if len(inf) != 3:
        raise ValueError('invalid format')
    inf[2] = inf[2].strip()
    
    if inf[1] not in ('DEBUG', 'INFO', 'WARNING', 'ERROR'):
        raise ValueError('invalid level')

    return {'time': inf[0], 'level': inf[1], 'message': inf[2]}

def count_levels(lines: list[str]):
    cnt = {'BROKEN': 0, 'DEBUG': 0, 'ERROR' : 0, 'INFO': 0, 'WARNING': 0}
    for line in lines:
        if line.strip():
            try: cnt[parse_event(line)['level']] += 1
            except: cnt['BROKEN'] += 1
    cnt = {k: v for k, v in cnt.items() if v != 0}
    return cnt

def top_errors(lines: list[str], n: int):
    cnt = {}

    for line in lines:
        if line.strip():
            try:
                inf = parse_event(line)

                if inf['level'] == 'ERROR':
                    if inf['message'] not in cnt:
                        cnt[inf['message']] = 0

                    cnt[inf['message']] += 1

            except ValueError:
                pass

    cnt = dict(sorted(cnt.items()))
    top = []

    for i in range(min(n, len(cnt))):
        err = max(cnt, key=lambda x: cnt[x])
        top.append([err, cnt.pop(err)])

    return top
   

def format_report(counts: dict, errors: list[list]):
    report = 'Отчёт по журналу\n\n'
    for i in sorted(counts):
        report += f'{i}: {counts[i]}\n'
    report += '\nЧастые ошибки:\n'
    for i in errors:
        report += f'- {i[0]} — {i[1]}\n'
    return report 
     
        
        
