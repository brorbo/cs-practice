def csv_to_records(text): ## --> dict
    tb = text.split('\n'); keys = [key for key in tb.pop(0).split(',')]
    k = len(keys)
    ret = [{keys[i]: znach.split(',')[i] for i in range(k)} for znach in tb]
    return ret

def parse_settings(lines: list[str]):  ## --> dict
    ret = {}; flag = 0; lst = []
    for line in lines:
        if flag:
            line = line.split('#', maxsplit = 1)[0] 
            if line.strip()[0] == '-':
                lst += [line.strip()[1:].strip()]
            else:
                flag = 0; ret[lstnam] = lst; lst = []
        else:    
            line = line.split('#', maxsplit = 1)[0].split(':')
                if line:
                    if line[1]:
                        ret[line[0]] = line[1]
                    else:
                        flag = 1; lstnam = line[0]
    return ret

def merge_by_key(rows: list[dict], extra: dict, key: str = 'id'):  # -> list[dict]
    for dct in rows:
         
        
    
    
                
                    
                    
                


