from decimal import Decimal, ROUND_DOWN
from collections import defaultdict
from pathlib import Path
paths = ["docs/report.PDF", "notes.txt", "docs/img/logo.png", "Makefile"]

def count_by_extension(lstpaths: list[str]):
    files = [f('.')[-1] for f in lstpaths]
    ret = defaultdict(int)
    for file in files:
        ret[file] += 1
    ret = dict(ret)
    return ret

def deepest_path(paths: list[str]):
    return max(paths, key = lambda x: count(x, '/'))

def human_size(n_bytes: int):
    types = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']
    ret = f'{n_bytes}Б'; k = 0
    while n_bytes >= 1024:
        n_bytes /= 1024
        k += 1
    ret = f'{Decimal(str(n_bytes)).quantize(Decimal("0.1"),  rounding=ROUND_DOWN)}{types[k]}'
    return ret


count_by_extension(paths)   # {"pdf": 1, "txt": 1, "png": 1, "": 1}
deepest_path(paths)         # "docs/img/logo.png"

human_size(900)             # "900 Б"
human_size(1536)            # "1.5 КБ"
human_size(5 * 1024 * 1024) # "5.0 МБ"

