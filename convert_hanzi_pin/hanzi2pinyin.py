#-*- coding:utf-8 -*-
# python3
from pypinyin import pinyin, lazy_pinyin,Style

def getHanziFromFiles(filename):
    if filename is None:
        print("Filename is None.")
        return []
    res = []
    try:
        with open(filename,'r',encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                l = line.strip()
                if l:
                    res.append(l)
    except Exception as e:
        print(str(e))
    finally:
        return res

names = getHanziFromFiles("names.txt")
pyname = []
for name in names:
    pyname.append(''.join(lazy_pinyin(name)))

for ind,val in enumerate(pyname):
    print(ind+1,val)