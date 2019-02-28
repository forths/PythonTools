import sys
import os
import re
fpath = sys.argv[1]
pat = sys.argv[2]
changeto = sys.argv[3]
#pat = u"[\u4E00-\u9FA5]+"
count = 0
print('input path is',fpath)
if fpath.startswith('/'):
    files = os.listdir(fpath)
    for dirname in files:
        if os.path.isdir(fpath + dirname):
            df = os.listdir(fpath + dirname)
            for name in df:
                srcname = fpath+dirname+'/'+name
                newname = re.sub(pat,changeto,srcname.decode('utf-8'))
                print(newname)
                os.rename(srcname,newname)
                count += 1
else:
    print('please use absolute path')
print(count)
