def csv_to_records(text):
    tb = text.split('\n'); keys = [key for key in tb.pop(0).split(',')]
    k = len(keys)
    ret = [{keys[i]: znach.split(',')[i] for i in range(k)} for znach in tb]
    return ret

def parse_settings(lines):
    ret = {}
    for line in lines:
        if line[0] ! = '#':
            if line.split(
