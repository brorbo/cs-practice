def parse_event(line: str):
    inf = line.split(maxsplit = 2)
    if not(inf[1] in ('DEBUG, INFO, WARNING, ERROR')):
        raise ValueError('invalid level')
    elif any(i == '' for i in inf):
        raise ValueError('empty part(s) in string')
    else: ret = {'time': inf[0],'level': inf[1], 'message': inf[2],} \
                if len(inf) == 3 else {'time': inf[0], 'level': inf[1],}
    return ret

def count_levels(lines: list[str]):
    cnt = {'BROKEN': 0, 'DEBUG': 0, 'ERROR' : 0, 'INFO': 0, 'WARNING': 0}
    for line in lines:
        if line != '':
            try: cnt[parse_event(line)['level']] += 1
            except: cnt['BROKEN'] += 1
    cnt = {k: v for k, v in cnt.items() if v != 0}
    return cnt

def top_errors(lines: list[str], n: int):
    top = [['', 0]] * n; cnt = {};
    if lines == []: return top
    for line in lines:
        if line != '':
            try:
                inf = parse_event(line)
                if inf['level'] == 'ERROR':
                    try: cnt[inf['message']] += 1
                    except: cnt[inf['message']] = 1
            except:
                ...
    cnt = dict(sorted(cnt.items()))
    for i in range(n):
        err = max(cnt, key = lambda x: cnt[x])
        top[i] = [err, cnt.pop(err)] 
    return top

def format_report(counts: dict, errors: list[list]):
    report = 'Отчёт по журналу\n\n'
    for i in counts:
        report += f'{i}: {counts[i]}\n'
    report += '\nЧастые ошибки:\n'
    for i in errors:
        report += f'— {i[0]} — {i[1]}\n'
    return report 
     
        
        
