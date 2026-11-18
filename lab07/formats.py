def csv_to_records(text): ## --> list(dict)
    if not text.strip(): return []
    tb = text.strip().split('\n'); keys = [key.strip() for key in tb.pop(0).split(',')]; k = len(keys)
    ret = [{keys[i]: znach.split(',')[i].strip() for i in range(k)} for znach in tb if znach.strip()]
    return ret

def parse_settings(lines: list[str]):  ## --> dict
    ret = {}; flag = 0; lst = []
    for line in lines:
        line = line.split('#', maxsplit=1)[0].strip()
        if not line: continue
        if flag:
            if line[0] == '-':
                lst += [line[1:].strip()]
                continue
            else:
                flag = 0; ret[lstnam] = lst; lst = []
        if ':' in line:
            parts = line.split(':', maxsplit=1)
            if parts[1].strip():
                ret[parts[0].strip()] = parts[1].strip()
            else:
                flag = 1; lstnam = parts[0].strip()
    if flag: ret[lstnam] = lst
    for i in ret:
        if isinstance(ret[i], str):
            if ret[i] in ('true', 'yes'): ret[i] = True
            elif ret[i] in ('false', 'no'): ret[i] = False
            else:
                try: ret[i] = int(ret[i])
                except:
                    try: ret[i] = float(ret[i])
                    except:
                        try: ret[i] = float(ret[i].replace(',', '.'))
                        except:
                            ...
    return ret
        
def merge_by_key(rows: list[dict], extra: dict, key: str = 'id'):  # -> list[dict]
    for i in range(len(rows)):
        if key in sorted(rows[i]) and rows[i][key] in extra:
            extradict = [extra[f] for f in extra if f == rows[i][key]][0]
            for d in extradict:
                try: rows[i][d]
                except:
                    rows[i][d] = extradict[d]
    return rows

def records_to_json(records: list[dict]): # -> str
    if not records: return '[]'
    ret = '[\n'
    keys = [sorted(d) for d in records]
    for dct in range(len(keys)):
        ret += '  {\n'
        for elem in keys[dct]:
            val = records[dct][elem]
            if isinstance(val, (int, float)) and not isinstance(val, bool):
                ret += f'    "{elem}": {val},\n'
            else:
                ret += f'    "{elem}": "{val}",\n'.replace('"True"', 'true').replace('"False"', 'false')
        ret = ret[:-2] + '\n  },\n'
    ret = ret[:-2] + '\n]'
    return ret
