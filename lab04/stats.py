def parse_record(line:str):
    inf = line.split(sep = ';')
    if len(inf) != 3: raise ValueError('number of fields should be 3')
    elif any(i == '' for i in inf): raise ValueError('not enough data')
    else: city, date = inf[0], inf[2]
    try: temp = float(inf[1])
    except: raise ValueError('temperature should be float data type')
    return {
        'city': city,
        'temperature': temp,
        'date': date,
        }


def read_valid(lines: list[str]):
    ret = [] 
    for line in lines:
        try: ret += [parse_record(line)]
        except: ...
    return ret

def total(records: list[dict]):
    totals = {}
    for city in records:
        try:
            totals[city['city']][1] += city['temperature']
            totals[city['city']][2] += 1
        except:
            totals[city['city']] = [city['city'], city['temperature'], 1]
    return totals

def warmest_city(records: list[dict]):
    tot = total(records)
    mx = tot[max(tot, key = lambda x: tot[x][1] / tot[x][2])]
    return(mx[0]) ## в mx город, сумма темп-ры и кол-во строк

def average_by_city(records: list[dict]):
    tot = total(records)
    avtemps = {i: tot[i][1] / tot[i][2] for i in tot}
    return avtemps
