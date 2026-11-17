def csv_to_records(text): ## --> list(dict)
    tb = text.split('\n'); keys = [key for key in tb.pop(0).split(',')]; k = len(keys)
    if tb[-1] == '': tb = tb[:-1]
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
            if line[0]:
                if line[1]:
                    ret[line[0]] = line[1].strip()
                else:
                     flag = 1; lstnam = line[0].strip()
    if lst: ret[lstnam] = lst
    for i in ret:
        if ret[i] in ('true', 'yes'): ret[i] = True
        elif ret[i] in ('false', 'no'): ret[i] = False
        else:
            try: ret[i] = int(ret[i])
            except:
                try: ret[i] = float(ret[i])
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
    ret = '[\n'
    keys = [sorted(d) for d in records]
    for dct in range(len(keys)):
        ret += '  {\n'
        for elem in keys[dct]:
            ret += f'    "{elem}": "{records[dct][elem]}",\n'.replace('"True"', 'true').replace(\
                '"False"', 'false')
        ret = ret[:-2] + '\n  },\n'
    ret = ret[:-2]
    return ret


csv_to_records("""id,город
1,Азов
2,Шахты
""")
# [{"id": "1", "город": "Азов"}, {"id": "2", "город": "Шахты"}]

parse_settings(["# отчёт", "title: Отчёт за март", "decimals: 1", "active: true",
                "columns:", "  - город", "  - цена"])
# {"title": "Отчёт за март", "decimals": 1, "active": True, "columns": ["город", "цена"]}

merge_by_key([{"id": "1", "город": "Азов"}], {"1": {"регион": "Ростовская"}}, "id")
# [{"регион": "Ростовская", "id": "1", "город": "Азов"}]       
                


