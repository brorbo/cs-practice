def parse_record(line:str):
    inf = line.split(sep = ';')
    if len(inf) != 3: raise ValueError('number of fields should be 3')
    elif any(i for i in inf = ''): raise ValueError('not enough data')
    else: city, date = inf[0], inf[2]
        try: temp = float(inf[1])
        except: raise ValueError('temperature should be float data type')
    return {
        'city': city
        'temp': temp
        'date': date
        }

def read_valid(lines: list[str]):
    ret = [] 
    for line in lines:
        try: ret += parse_record(line)
        except: ...
    return ret

def warmest_city(records: list[dict]):
    if total in globals():
        mx = max(total, key = lambda x: x[1] / x[2])
    else:
        total = {}
    for city in records:
        try:
            total[city['city']][1] += city['temp']
            total[city['city']][2] += 1
        except:
            total[city['city']] = city['city'], city['temp'], 1
    mx = max(total, key = lambda x: x[1] / x[2])
    return(mx[0])

def average_by_city(records: list[dict])
    if total in globals():
        temps = [
    total = {}
    for city in records:
        try:
            total[city['city']][1] += city['temp']
            total[city['city']][2] += 1
        except:
            total[city['city']] = city['city'], city['temp'], 1
