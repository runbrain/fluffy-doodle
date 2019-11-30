#archive all files from directory to zip archive

import os
import time
import zipfile

#directories
source = 'c:\\fluffy-doodle\\AByteOfPython\\'
target_dir = 'c:\\back'
today_dir = target_dir+os.sep+time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

comment = input('input: ')
if len(comment) == 0:
    target = today_dir + os.sep +now + '.zip'
else:
    target = today_dir + os.sep + now + '_'+\
             comment.replace(' ','_')+'.zip'
if not os.path.exists(today_dir):
    os.mkdir(today_dir)
    print('mkdir')

#make archive
if len(comment) == 0:
    target = today_dir + os.sep +now + '.zip'
else:
    target = today_dir + os.sep + now + '_'+\
             comment.replace(' ','_')+'.zip'
print(os.listdir(source))
zf = zipfile.ZipFile(target, 'w')
for file in os.listdir(source):
    print(source+file)
    zf.write(source+file)
zf.close()