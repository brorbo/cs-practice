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
    return re
        
